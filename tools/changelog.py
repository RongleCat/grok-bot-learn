#!/usr/bin/env python3
import json, re, sys, html, os, subprocess, urllib.request, xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'site/docs/.vitepress/theme/changelog.json')
RAW = os.path.join(ROOT, '.changelog/raw.json')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'
PC_RSS = 'https://x.ai/changelog/bot/rss.xml'
IOS_PAGE = 'https://apps.apple.com/us/app/grok-bot/id6794501026'
IOS_LOOKUP = 'https://itunes.apple.com/lookup?id=6794501026'
PLAY = 'https://play.google.com/store/apps/details?id=ai.x.grok.bot&hl=en'
MODEL = 'gemini-3.8-flash-high'


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8', 'replace')


def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', ' ', s)).strip()


def fetch_pc():
    root = ET.fromstring(get(PC_RSS))
    out = []
    for it in root.iter('item'):
        title = it.findtext('title') or ''
        m = re.search(r'\(([\d.]+)\)\s*$', title)
        ver = m.group(1) if m else ''
        desc = html.unescape(it.findtext('description') or '')
        sections, cur = {}, 'Notes'
        for tag, body in re.findall(r'<(h3|li)>(.*?)</\1>', desc, re.S):
            if tag == 'h3':
                cur = strip(body)
            else:
                sections.setdefault(cur, []).append(strip(body))
        out.append({
            'id': f'pc-{ver}', 'platform': 'pc', 'version': ver,
            'date': parsedate_to_datetime(it.findtext('pubDate')).strftime('%Y-%m-%d'),
            'url': it.findtext('link'), 'title': re.sub(r'\s*\([\d.]+\)\s*$', '', title),
            'sections': sections,
        })
    return out


def fetch_ios():
    s = get(IOS_PAGE)
    out = []
    for m in re.finditer(r'\{"\$kind":"TitledParagraph","text":"((?:[^"\\]|\\.)*)","style":"detail","wantsCollapsedNewlines":true,"primarySubtitle":"([^"]+)","secondarySubtitle":"([^"]+)"', s):
        text = json.loads('"' + m.group(1) + '"')
        d = datetime.strptime(' '.join(m.group(3).split()[1:4]), '%b %d %Y')
        out.append({'id': f'ios-{m.group(2)}', 'platform': 'ios', 'version': m.group(2), 'date': d.strftime('%Y-%m-%d'),
                    'url': IOS_PAGE, 'title': '', 'sections': {'Notes': [l.lstrip('-• ').strip() for l in text.split('\n') if l.strip()]}})
    if not out:
        r = json.loads(get(IOS_LOOKUP))['results'][0]
        out.append({'id': f"ios-{r['version']}", 'platform': 'ios', 'version': r['version'], 'date': r['currentVersionReleaseDate'][:10],
                    'url': IOS_PAGE, 'title': '', 'sections': {'Notes': [l.lstrip('-• ').strip() for l in r.get('releaseNotes', '').split('\n') if l.strip()]}})
    return out


def fetch_android():
    s = get(PLAY)
    m = re.search(r'Updated on</div><div[^>]*>([A-Z][a-z]{2} \d{1,2}, \d{4})', s)
    n = re.search(r'itemprop="description">(.*?)</div>', s, re.S)
    if not m:
        return []
    d = datetime.strptime(m.group(1), '%b %d, %Y').strftime('%Y-%m-%d')
    notes = [x.strip() for x in strip((n.group(1) if n else '').replace('<br>', '\n')).split('\n') if x.strip()]
    return [{'id': f'android-{d}', 'platform': 'android', 'version': '', 'date': d, 'url': PLAY, 'title': '', 'sections': {'Notes': notes}}]


PROMPT = """你在给一个非官方的 Grok Bot 中文学习站写更新日志摘要。下面是官方英文更新记录（JSON 数组）。
对每一条，用你自己的话写简体中文摘要，不要逐句翻译：
- title：不超过 16 个字的中文标题，概括这一版最值得关心的变化
- points：最多 4 条，每条不超过 32 个字，挑普通用户最在意的新功能和改进，按重要程度排序；只有通用修复时写一条概括
- 不用「我们」，不加 emoji，不加句号以外的装饰，产品名保留 Grok Bot、Bot、Mac、Windows、iOS、Android 等英文
只输出 JSON 对象，键是每条的 id，值是 {"title": "...", "points": ["..."]}，不要任何其他文字。

"""


SECTION = {'New': '新功能', 'Improved': '改进', 'Fixed': '修复', 'Notes': ''}

TPROMPT = """把下面 Grok Bot 官方英文更新记录完整翻译成简体中文。要求：
- 逐条忠实翻译，不删、不并、不加，条目数量和顺序与原文完全一致
- 语言自然通顺，像中文软件更新说明
- 产品名和专有名词保留英文：Grok Bot、Bot、Mac、Windows、iOS、Android、Slack、GitHub、Outlook、Gmail、Figma、Notion、X、Webhook、Secure Form、Auto-review 等
- 界面上的按钮、菜单、提示文字保留英文原文，用「」括起来，例如「Contact Support」
- 固定译法：routine 译为触发器，computer 指 Bot 的电脑时译为 Bot 的电脑，skill 译为技能，plugin 译为插件，connector 译为连接器，Team Bot 译为团队 Bot，approval card 译为审批卡片，question card 译为提问卡片
只输出 JSON 对象，键是每条的 id，值是对象：键为原文分组名（如 New、Improved、Fixed、Notes），值为与原文一一对应的中文字符串数组。不要任何其他文字。

"""


def translate(items):
    prompt = TPROMPT + json.dumps([{'id': i['id'], 'sections': i['sections']} for i in items], ensure_ascii=False)
    for attempt in range(5):
        env = dict(os.environ)
        if attempt >= 2:
            env['GEMINI_FORCE_FILE_STORAGE'] = 'true'
        try:
            r = subprocess.run(['agy', '--model', MODEL, '-p', prompt], capture_output=True, text=True, timeout=900, env=env)
            t = r.stdout
            data = json.loads(t[t.find('{'):t.rfind('}') + 1])
            if all(i['id'] in data and all(len(data[i['id']].get(k, [])) == len(v) for k, v in i['sections'].items()) for i in items):
                return {i['id']: [[SECTION.get(k, k), data[i['id']][k]] for k in i['sections']] for i in items}
        except Exception as e:
            print('agy retry', attempt, e, file=sys.stderr)
    raise SystemExit('agy translate failed')


def batches(items, cap=60):
    out, cur, n = [], [], 0
    for i in items:
        c = sum(len(v) for v in i['sections'].values())
        if cur and n + c > cap:
            out.append(cur)
            cur, n = [], 0
        cur.append(i)
        n += c
    return out + ([cur] if cur else [])


def summarize(items):
    payload = [{'id': i['id'], 'platform': i['platform'], 'version': i['version'], 'title': i['title'], 'sections': i['sections']} for i in items]
    prompt = PROMPT + json.dumps(payload, ensure_ascii=False)
    for attempt in range(4):
        env = dict(os.environ)
        if attempt >= 2:
            env['GEMINI_FORCE_FILE_STORAGE'] = 'true'
        try:
            r = subprocess.run(['agy', '--model', MODEL, '-p', prompt], capture_output=True, text=True, timeout=600, env=env)
            t = r.stdout
            data = json.loads(t[t.find('{'):t.rfind('}') + 1])
            if all(i['id'] in data for i in items):
                return data
        except Exception as e:
            print('agy retry', attempt, e, file=sys.stderr)
    raise SystemExit('agy failed')


def main():
    args = sys.argv[1:]
    cur = json.load(open(OUT)) if os.path.exists(OUT) else {'updated': '', 'official': [], 'ours': []}
    if args[:1] == ['add-tweet']:
        _, url, date, title, summary, *plat = args
        tid = url.rstrip('/').split('/')[-1]
        cur['ours'] = [t for t in cur['ours'] if t['id'] != tid] + [{'id': tid, 'date': date, 'url': url, 'title': title, 'summary': summary, 'platform': plat[0] if plat else ''}]
        cur['ours'].sort(key=lambda t: t['date'], reverse=True)
        json.dump(cur, open(OUT, 'w'), ensure_ascii=False, indent=1)
        return
    raw = []
    for f in (fetch_pc, fetch_ios, fetch_android):
        try:
            raw += f()
        except Exception as e:
            print(f.__name__, 'failed', e, file=sys.stderr)
    os.makedirs(os.path.dirname(RAW), exist_ok=True)
    json.dump(raw, open(RAW, 'w'), ensure_ascii=False, indent=1)
    have = {e['id']: e for e in cur['official']}
    todo = [r for r in raw if r['id'] not in have]
    if '--resummarize' in args:
        todo = raw
    for k in range(0, len(todo), 8):
        batch = todo[k:k + 8]
        res = summarize(batch)
        for r in batch:
            have[r['id']] = {'id': r['id'], 'platform': r['platform'], 'version': r['version'], 'date': r['date'], 'url': r['url'],
                             'title': res[r['id']]['title'], 'points': res[r['id']]['points'][:4], **({'full': have[r['id']]['full']} if r['id'] in have and have[r['id']].get('full') else {})}
        print(f'summarized {k + len(batch)}/{len(todo)}', file=sys.stderr)
    tl = [r for r in raw if '--retranslate' in args or not have[r['id']].get('full')]
    with ThreadPoolExecutor(4) as ex:
        for res in ex.map(translate, batches(tl)):
            for k, v in res.items():
                have[k]['full'] = v
            print('translated', len(res), file=sys.stderr)
    cur['official'] = sorted(have.values(), key=lambda e: (e['date'], e['version']), reverse=True)
    cur['updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    json.dump(cur, open(OUT, 'w'), ensure_ascii=False, indent=1)
    print(f"new {len(todo)}, translated {len(tl)}, total {len(cur['official'])}")


main()
