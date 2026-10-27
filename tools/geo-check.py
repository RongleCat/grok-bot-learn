#!/usr/bin/env python3
import argparse, hashlib, json, os, re, sys, time
from datetime import datetime, timezone, timedelta
from urllib import robotparser
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

SGT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (compatible; GeoCheck/1.0; +https://bot.fmcat.top/)'
AI_TOKENS = {
    'OAI-SearchBot': 'search', 'ChatGPT-User': 'user', 'GPTBot': 'training',
    'Claude-SearchBot': 'search', 'Claude-User': 'user', 'ClaudeBot': 'training',
    'PerplexityBot': 'search', 'Perplexity-User': 'user',
    'Google-Extended': 'control', 'Googlebot': 'search', 'Bingbot': 'search',
    'Applebot': 'search', 'Applebot-Extended': 'control', 'Baiduspider': 'search',
    'Bytespider': 'training', 'CCBot': 'training', 'Amazonbot': 'search',
    'meta-externalagent': 'training', 'DuckAssistBot': 'user', 'YisouSpider': 'search',
}
UA_PROBES = {
    'GPTBot': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)',
    'OAI-SearchBot': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot)',
    'ClaudeBot': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)',
    'Claude-SearchBot': 'Mozilla/5.0 (compatible; Claude-SearchBot/1.0; +https://www.anthropic.com)',
    'PerplexityBot': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)',
    'Googlebot': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Bingbot': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Baiduspider': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Bytespider': 'Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; Bytespider; spider-feedback@bytedance.com)',
}
DEPRECATED = {'HowTo': 'Google 2023-09 起不再展示 HowTo 富结果', 'SpecialAnnouncement': '2025-07 已弃用',
              'CourseInfo': '2025-06 已退役', 'EstimatedSalary': '2025-06 已退役', 'LearningVideo': '2025-06 已退役'}
INFO_TYPES = {'FAQPage': 'Google 2026-05 起不再展示 FAQ 富结果，AI 引用收益未经证实'}
ARTICLE = {'Article', 'TechArticle', 'BlogPosting', 'NewsArticle'}
CJK = re.compile(r'[\u3400-\u9fff\uf900-\ufaff]')


def get(url, ua=UA, timeout=30):
    try:
        r = requests.get(url, headers={'User-Agent': ua, 'Accept-Language': 'zh-CN,zh;q=0.9'}, timeout=timeout, allow_redirects=False)
        r.encoding = 'utf-8'
        return r
    except Exception as e:
        return e


def units(text):
    cjk = len(CJK.findall(text))
    latin = len(re.findall(r'[A-Za-z0-9][A-Za-z0-9.\-+/]*', text))
    return cjk / 1.7 + latin


def score_block(text, heading):
    u = units(text)
    sents = [s for s in re.split(r'[。！？!?；;\n]+', text) if s.strip()]
    s = {'answer': 0, 'self': 0, 'structure': 0, 'stats': 0, 'unique': 0}
    head = text[:110]
    if re.search(r'(是|指|即|意思是|定义为|就是|本质上|简单说)', head):
        s['answer'] += 15
    if re.search(r'\d|是|指|可以|需要|必须|不能|支持', head):
        s['answer'] += 10
    if heading and re.search(r'[？?]|什么|怎么|如何|为什么|哪些|哪个|能不能|是否|多少', heading):
        s['answer'] += 10
    if sents:
        good = sum(1 for x in sents if 8 <= len(x.strip()) <= 60)
        s['answer'] += int(good / len(sents) * 5)
    if re.search(r'(根据|据|官方(文档|说明|公告)|帮助中心|xAI 表示|文档显示)', text):
        s['answer'] += 5
    s['answer'] = min(s['answer'], 30)
    if 134 <= u <= 167: s['self'] += 10
    elif 100 <= u <= 200: s['self'] += 7
    elif 80 <= u <= 250: s['self'] += 4
    elif 30 <= u <= 400: s['self'] += 2
    pron = len(re.findall(r'(它们|它|这些|那些|这个|那个|此|其|他们|她们)', text))
    ratio = pron / max(u, 1)
    s['self'] += 8 if ratio < 0.02 else 5 if ratio < 0.04 else 3 if ratio < 0.06 else 0
    names = len(set(re.findall(r'\b[A-Z][A-Za-z0-9\-]+(?:\s+[A-Z][A-Za-z0-9\-]+)*', text)))
    s['self'] += 7 if names >= 3 else 4 if names >= 1 else 0
    s['self'] = min(s['self'], 25)
    if sents:
        avg = sum(len(x) for x in sents) / len(sents)
        s['structure'] += 8 if 15 <= avg <= 45 else 5 if 10 <= avg <= 60 else 2
    if re.search(r'(首先|其次|然后|最后|第一|第二|另外|此外)', text): s['structure'] += 4
    if re.search(r'(^|\n)\s*\d+[\.、）)]|步骤\s*\d|第\s*\d+\s*步', text): s['structure'] += 4
    if '\n' in text: s['structure'] += 4
    s['structure'] = min(s['structure'], 20)
    s['stats'] += min(len(re.findall(r'\d+(?:\.\d+)?\s*%', text)) * 3, 6)
    s['stats'] += min(len(re.findall(r'[$¥￥]\s?\d|\d+\s*(美元|元|刀)', text)) * 3, 5)
    s['stats'] += min(len(re.findall(r'\d+(?:\.\d+)?\s*(个|次|小时|分钟|秒|天|周|月|倍|万|GB|MB|x|X|档|步|位)', text)) * 2, 4)
    if re.search(r'20(2[3-9]|1\d)', text): s['stats'] += 2
    if re.search(r'(xAI|Cursor|OpenAI|Google|官方|帮助中心|status\.)', text): s['stats'] += 2
    s['stats'] = min(s['stats'], 15)
    if re.search(r'(实测|我们发现|我们测试|亲测|我的做法|我用|作者称)', text): s['unique'] += 5
    if re.search(r'(案例|例如|比如|举例)', text): s['unique'] += 3
    if re.search(r'(Grok Bot|Cursor|飞书|微信|Slack|Notion|GitHub|X )', text): s['unique'] += 2
    s['unique'] = min(s['unique'], 10)
    return sum(s.values()), s, round(u)


def blocks_of(main):
    out, head, buf = [], None, []
    for el in main.find_all(['h1', 'h2', 'h3', 'p', 'li', 'td', 'blockquote', 'pre'], recursive=True):
        if el.name in ('h1', 'h2', 'h3'):
            if buf: out.append((head, '\n'.join(buf)))
            head, buf = el.get_text(' ', strip=True).replace('\u200b', ''), []
        elif el.name in ('li', 'td') and el.find_parent(['li', 'td']) is not None:
            continue
        elif el.name == 'p' and el.find_parent(['li', 'td', 'blockquote']) is not None:
            continue
        else:
            t = el.get_text(' ', strip=True)
            if t: buf.append(t)
    if buf: out.append((head, '\n'.join(buf)))
    return [(h, t) for h, t in out if units(t) >= 20]


def flat_types(node, acc):
    if isinstance(node, list):
        for n in node: flat_types(n, acc)
    elif isinstance(node, dict):
        t = node.get('@type')
        if t: acc.append(node)
        for k, v in node.items():
            if k != '@type' and isinstance(v, (dict, list)): flat_types(v, acc)


def check_schema(blocks):
    nodes, errors = [], []
    for raw in blocks:
        try:
            d = json.loads(raw)
        except Exception as e:
            errors.append(f'JSON-LD 解析失败: {e}')
            continue
        ctx = d.get('@context', '') if isinstance(d, dict) else ''
        if ctx and ctx != 'https://schema.org': errors.append(f'@context 应为 https://schema.org（现为 {ctx}）')
        flat_types(d, nodes)
    types = []
    for n in nodes:
        t = n['@type'] if isinstance(n['@type'], list) else [n['@type']]
        types += t
        for k in ('url', 'item', 'image', 'mainEntityOfPage', 'contentUrl', 'thumbnailUrl'):
            v = n.get(k)
            if isinstance(v, str) and v and not v.startswith('http'): errors.append(f'{t[0]}.{k} 不是绝对地址: {v}')
        for k in ('datePublished', 'dateModified', 'uploadDate'):
            v = n.get(k)
            if v and not re.match(r'^\d{4}-\d{2}-\d{2}', str(v)): errors.append(f'{t[0]}.{k} 不是 ISO 8601: {v}')
        if set(t) & ARTICLE:
            for k in ('headline', 'author', 'datePublished', 'dateModified'):
                if not n.get(k): errors.append(f'{t[0]} 缺少 {k}')
        if 'VideoObject' in t:
            for k in ('name', 'description', 'thumbnailUrl', 'uploadDate'):
                if not n.get(k): errors.append(f'VideoObject 缺少 {k}')
        if re.search(r'\[[^\]]*(Name|名称)\]', json.dumps(n, ensure_ascii=False)): errors.append('疑似占位文本')
    warn = [f'{t}: {DEPRECATED[t]}' for t in set(types) if t in DEPRECATED]
    info = [f'{t}: {INFO_TYPES[t]}' for t in set(types) if t in INFO_TYPES]
    return sorted(set(types)), errors, warn, info


def page(url, site):
    r = get(url)
    if isinstance(r, Exception):
        return {'url': url, 'status': None, 'error': str(r)}
    rec = {'url': url, 'status': r.status_code, 'ctype': r.headers.get('content-type', '')}
    if r.status_code != 200:
        rec['location'] = r.headers.get('location')
        return rec
    soup = BeautifulSoup(r.text, 'lxml')
    h = soup.find('html')
    rec['lang'] = h.get('lang') if h else None
    rec['title'] = (soup.title.string or '').strip() if soup.title else ''
    m = soup.find('meta', attrs={'name': 'description'})
    rec['description'] = m.get('content', '') if m else ''
    c = soup.find('link', rel='canonical')
    rec['canonical'] = c.get('href') if c else None
    rb = soup.find('meta', attrs={'name': 'robots'})
    rec['robots'] = rb.get('content') if rb else ''
    rec['hreflang'] = [l.get('hreflang') for l in soup.find_all('link', rel='alternate') if l.get('hreflang')]
    rec['md_alternate'] = bool(soup.find('link', attrs={'rel': 'alternate', 'type': 'text/markdown'}))
    og = soup.find('meta', property='og:title')
    rec['og_title'] = og.get('content') if og else ''
    raw = [s.string or '' for s in soup.find_all('script', type='application/ld+json')]
    rec['schema_types'], rec['schema_errors'], rec['schema_warn'], rec['schema_info'] = check_schema(raw)
    rec['schema_hash'] = hashlib.sha256('\n'.join(raw).encode()).hexdigest()[:12]
    main = soup.select_one('.vp-doc') or soup.select_one('main') or soup.body
    h1 = main.find('h1') if main else None
    rec['h1'] = h1.get_text(' ', strip=True).replace('\u200b', '') if h1 else (soup.find('h1').get_text(' ', strip=True) if soup.find('h1') else '')
    text = main.get_text('\n', strip=True) if main else ''
    rec['ssr_units'] = round(units(text))
    rec['content_hash'] = hashlib.sha256(text.encode()).hexdigest()[:12]
    rec['h2'] = [x.get_text(' ', strip=True).replace('\u200b', '') for x in (main.find_all('h2') if main else [])]
    rec['date_visible'] = bool(soup.select_one('.VPLastUpdated, time'))
    host = urlparse(site).netloc
    links = set()
    for a in (main.find_all('a', href=True) if main else []):
        u = urljoin(url, a['href']).split('#')[0].split('?')[0]
        if urlparse(u).netloc == host: links.add(u.rstrip('/') or u)
    rec['content_links'] = sorted(links)
    bl = blocks_of(main) if main else []
    scored = sorted(((score_block(t, hd), hd, t) for hd, t in bl), key=lambda x: -x[0][0])
    top = [x[0][0] for x in scored[:5]]
    rec['citability'] = round(sum(top) / len(top), 1) if top else 0
    rec['blocks'] = len(bl)
    rec['q_headings'] = sum(1 for hd, _ in bl if hd and re.search(r'[？?]|什么|怎么|如何|为什么|哪些|能不能|是否', hd))
    rec['weakest'] = [{'heading': hd, 'score': sc[0], 'units': sc[2]} for sc, hd, t in scored[-2:]] if scored else []
    return rec


def robots_report(site):
    r = get(site + '/robots.txt')
    if isinstance(r, Exception) or r.status_code != 200:
        return {'status': getattr(r, 'status_code', None), 'ok': False}
    rp = robotparser.RobotFileParser()
    rp.parse(r.text.splitlines())
    groups = re.findall(r'(?im)^user-agent:\s*(\S+)', r.text)
    access = {t: rp.can_fetch(t, site + '/part1/01-what-is') for t in AI_TOKENS}
    return {'status': 200, 'ok': True, 'named_groups': sorted(set(g for g in groups if g != '*')),
            'content_signal': bool(re.search(r'(?im)^content-signal:', r.text)),
            'sitemap': re.findall(r'(?im)^sitemap:\s*(\S+)', r.text),
            'blocked': [t for t, ok in access.items() if not ok], 's_disallowed': not rp.can_fetch('GPTBot', site + '/s/api/send')}


def ua_probe(site):
    out = {}
    base = get(site + '/')
    size = len(base.content) if not isinstance(base, Exception) else 0
    for name, ua in UA_PROBES.items():
        r = get(site + '/', ua)
        out[name] = {'status': getattr(r, 'status_code', None), 'same_size': (not isinstance(r, Exception)) and abs(len(r.content) - size) < max(500, size * 0.05)}
    return out


def llms_report(site, sitemap_urls):
    r = get(site + '/llms.txt')
    rep = {'status': getattr(r, 'status_code', None)}
    if isinstance(r, Exception) or r.status_code != 200:
        rep['score'] = 0
        return rep
    t = r.text
    rep['ctype'] = r.headers.get('content-type', '')
    rep['h1'] = bool(re.match(r'#\s+\S', t))
    rep['summary'] = bool(re.search(r'(?m)^>\s+\S', t))
    rep['sections'] = len(re.findall(r'(?m)^##\s+\S', t))
    found = set(u.rstrip('/') for u in re.findall(r'\]\((https?://[^)\s]+)\)', t))
    rep['links'] = len(found)
    norm = [u.rstrip('/') for u in sitemap_urls if u.rstrip('/') != site]
    missing = [u for u in norm if u not in found and u.replace('.md', '') not in found and u + '.md' not in found]
    rep['missing_from_llms'] = missing
    rep['coverage'] = round(1 - len(missing) / max(len(norm), 1), 3)
    rep['last_modified'] = r.headers.get('last-modified')
    f = get(site + '/llms-full.txt')
    rep['full_status'] = getattr(f, 'status_code', None)
    rep['full_bytes'] = len(f.content) if not isinstance(f, Exception) and f.status_code == 200 else 0
    ok = rep['h1'] and rep['summary'] and rep['sections'] >= 1 and 'text/' in rep['ctype']
    rep['score'] = 30 if not ok else 50 if rep['coverage'] < 0.5 else 70 if rep['coverage'] < 0.9 else (95 if rep['full_bytes'] else 80)
    return rep


def sitemap(site):
    r = get(site + '/sitemap.xml')
    if isinstance(r, Exception) or r.status_code != 200: return [], {}
    locs = re.findall(r'<loc>([^<]+)</loc>', r.text)
    mods = dict(re.findall(r'<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>', r.text))
    return locs, mods


def drift(cur, base):
    out = []
    for u, b in base.items():
        c = cur.get(u)
        if not c:
            out.append(('WARNING', u, '页面不在本次站点地图', '', ''))
            continue
        if c.get('status') != b.get('status') and (c.get('status') or 0) >= 300:
            out.append(('CRITICAL', u, '状态码变化', b.get('status'), c.get('status')))
        for k, sev, name in (('canonical', 'CRITICAL', 'canonical 变化'), ('title', 'WARNING', '标题变化'), ('description', 'WARNING', '描述变化'), ('og_title', 'WARNING', 'og:title 变化')):
            if (b.get(k) or '') != (c.get(k) or ''):
                if k == 'canonical' and not c.get(k): name = 'canonical 被移除'
                out.append((sev, u, name, b.get(k), c.get(k)))
        if 'noindex' in (c.get('robots') or '') and 'noindex' not in (b.get('robots') or ''):
            out.append(('CRITICAL', u, '新增 noindex', b.get('robots'), c.get('robots')))
        if b.get('h1') and not c.get('h1'):
            out.append(('CRITICAL', u, 'H1 被移除', b.get('h1'), ''))
        lost = set(b.get('schema_types') or []) - set(c.get('schema_types') or [])
        gain = set(c.get('schema_types') or []) - set(b.get('schema_types') or [])
        if lost: out.append(('CRITICAL' if lost & (ARTICLE | {'BreadcrumbList', 'WebSite', 'Person', 'SoftwareApplication', 'VideoObject'}) else 'WARNING', u, '结构化数据类型被移除', sorted(lost), ''))
        if gain: out.append(('INFO', u, '新增结构化数据类型', '', sorted(gain)))
        if not lost and not gain and b.get('schema_hash') != c.get('schema_hash'): out.append(('INFO', u, '结构化数据内容有改动', '', ''))
        if b.get('h2') != c.get('h2'): out.append(('INFO', u, 'H2 结构变化', '', ''))
        if b.get('content_hash') != c.get('content_hash'): out.append(('INFO', u, '正文有更新', '', ''))
    for u in cur:
        if u not in base: out.append(('INFO', u, '新页面', '', ''))
    return out


SNAP_KEYS = ('status', 'title', 'description', 'canonical', 'robots', 'h1', 'h2', 'og_title', 'schema_types', 'schema_hash', 'content_hash')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--site', default='https://bot.fmcat.top')
    ap.add_argument('--state', default=os.environ.get('GEO_STATE_DIR', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.geo')))
    ap.add_argument('--json', help='write full results to this path')
    ap.add_argument('--rebaseline', action='store_true', help='replace drift baseline with this run')
    ap.add_argument('--no-drift', action='store_true')
    a = ap.parse_args()
    site = a.site.rstrip('/')
    now = datetime.now(SGT)
    urls, mods = sitemap(site)
    rb = robots_report(site)
    probes = ua_probe(site)
    llms = llms_report(site, urls)
    pages = {}
    for u in urls:
        pages[u] = page(u, site)
        time.sleep(0.3)
    ok = [p for p in pages.values() if p.get('status') == 200]
    inbound = {u.rstrip('/'): 0 for u in urls}
    for p in ok:
        for l in p.get('content_links', []):
            if l in inbound and l != p['url'].rstrip('/'): inbound[l] += 1
    art_pages = [p for p in ok if set(p['schema_types']) & ARTICLE]
    issues = {
        'non_200': [(p['url'], p.get('status')) for p in pages.values() if p.get('status') != 200],
        'charset_missing': [p['url'] for p in ok if 'charset' not in p['ctype'].lower()],
        'canonical_mismatch': [p['url'] for p in ok if (p.get('canonical') or '').rstrip('/') != p['url'].rstrip('/')],
        'lang_not_zh': [p['url'] for p in ok if (p.get('lang') or '').lower() != 'zh-cn'],
        'no_description': [p['url'] for p in ok if not p['description']],
        'dup_description': sorted({p['url'] for p in ok for q in ok if p is not q and p['description'] and p['description'] == q['description']}),
        'no_schema': [p['url'] for p in ok if not p['schema_types']],
        'schema_errors': {p['url']: p['schema_errors'] for p in ok if p['schema_errors']},
        'schema_deprecated': {p['url']: p['schema_warn'] for p in ok if p['schema_warn']},
        'schema_info': {p['url']: p['schema_info'] for p in ok if p['schema_info']},
        'article_missing_dates': [p['url'] for p in art_pages if any('date' in e for e in p['schema_errors'])],
        'thin_ssr': [p['url'] for p in ok if p['ssr_units'] < 150],
        'no_content_inlinks': [u for u, n in inbound.items() if n == 0 and u != site],
    }
    cov = {t: sum(1 for p in ok if t in p['schema_types']) for t in ('WebSite', 'Person', 'BreadcrumbList', 'TechArticle', 'ItemList', 'SoftwareApplication', 'VideoObject', 'FAQPage', 'CollectionPage')}
    crawler_score = max(0, 100 - 15 * len([t for t in rb.get('blocked', []) if t in ('GPTBot', 'ClaudeBot', 'PerplexityBot', 'OAI-SearchBot', 'Googlebot')]) - 5 * len([t for t in rb.get('blocked', []) if t not in ('GPTBot', 'ClaudeBot', 'PerplexityBot', 'OAI-SearchBot', 'Googlebot')]) - (0 if rb.get('sitemap') else 10) - 10 * sum(1 for v in probes.values() if v['status'] != 200))
    cit = sorted(((p['citability'], p['url']) for p in ok if p['blocks']), key=lambda x: x[0])
    cit_avg = round(sum(c for c, _ in cit) / len(cit), 1) if cit else 0
    res = {'checked_at': now.isoformat(timespec='seconds'), 'site': site, 'sitemap_count': len(urls), 'robots': rb, 'ua_probe': probes,
           'llms': llms, 'schema_coverage': cov, 'crawler_score': crawler_score, 'citability_avg': cit_avg, 'issues': issues, 'pages': pages,
           'inbound_content_links': inbound}
    drift_rows = []
    if not a.no_drift:
        os.makedirs(os.path.join(a.state, 'history'), exist_ok=True)
        snap = {u: {k: p.get(k) for k in SNAP_KEYS} for u, p in pages.items()}
        bpath = os.path.join(a.state, 'baseline.json')
        if os.path.exists(bpath) and not a.rebaseline:
            base = json.load(open(bpath))
            drift_rows = drift(snap, base['pages'])
            res['drift_base'] = base['taken_at']
        else:
            json.dump({'taken_at': res['checked_at'], 'pages': snap}, open(bpath, 'w'), ensure_ascii=False, indent=1)
            res['drift_base'] = 'new baseline ' + res['checked_at']
        json.dump({'taken_at': res['checked_at'], 'pages': snap}, open(os.path.join(a.state, 'history', now.strftime('%Y-%m-%d') + '.json'), 'w'), ensure_ascii=False, indent=1)
        res['drift'] = drift_rows
    if a.json:
        json.dump(res, open(a.json, 'w'), ensure_ascii=False, indent=1, default=str)
    L = [f'GEO 检查 {site}  {now:%Y-%m-%d %H:%M} SGT  站点地图 {len(urls)} 页']
    blocked = rb.get('blocked', [])
    L.append(f"爬虫：robots {'可读' if rb.get('ok') else '不可读'}，被拦 {', '.join(blocked) if blocked else '无'}；具名组 {len(rb.get('named_groups', []))} 个；Content-Signal {'有' if rb.get('content_signal') else '无'}；UA 实测非 200：{', '.join(k for k, v in probes.items() if v['status'] != 200) or '无'}；爬虫分 {crawler_score}")
    if llms['status'] == 200:
        L.append(f"llms.txt：200 {llms.get('ctype')}，{llms['sections']} 节 {llms['links']} 链接，覆盖站点地图 {llms['coverage']:.0%}，llms-full {llms.get('full_status')} {llms.get('full_bytes', 0) // 1024}KB，得分 {llms['score']}")
        if llms['missing_from_llms']: L.append('  llms.txt 缺：' + ', '.join(u.replace(site, '') or '/' for u in llms['missing_from_llms'][:10]))
    else:
        L.append(f"llms.txt：缺失（{llms['status']}）")
    L.append('结构化数据覆盖：' + '，'.join(f'{k} {v}/{len(ok)}' for k, v in cov.items()))
    for k, name in (('schema_errors', '结构化数据错误'), ('schema_deprecated', '已弃用类型'), ('schema_info', '提示')):
        if issues[k]: L.append(f'{name}：' + '；'.join(f"{u.replace(site, '') or '/'} {', '.join(v[:3])}" for u, v in list(issues[k].items())[:6]))
    L.append(f'可引用度（中文适配版，0-100）：均值 {cit_avg}；最低：' + '，'.join(f"{u.replace(site, '') or '/'} {c}" for c, u in cit[:5]))
    tech = [(k, v) for k, v in issues.items() if k in ('non_200', 'charset_missing', 'canonical_mismatch', 'lang_not_zh', 'no_description', 'dup_description', 'no_schema', 'article_missing_dates', 'thin_ssr') and v]
    L.append('技术项：' + ('；'.join(f'{k} {len(v)}' for k, v in tech) if tech else '全部通过'))
    if issues['no_content_inlinks']: L.append('正文无站内入链：' + ', '.join(u.replace(site, '') or '/' for u in issues['no_content_inlinks'][:8]))
    if not a.no_drift:
        cnt = {s: sum(1 for r in drift_rows if r[0] == s) for s in ('CRITICAL', 'WARNING', 'INFO')}
        L.append(f"漂移（对比 {res['drift_base']}）：CRITICAL {cnt['CRITICAL']} / WARNING {cnt['WARNING']} / INFO {cnt['INFO']}")
        for r in [r for r in drift_rows if r[0] != 'INFO'][:10]:
            L.append(f"  {r[0]} {r[1].replace(site, '') or '/'} {r[2]}：{str(r[3])[:60]} → {str(r[4])[:60]}")
    print('\n'.join(L))


if __name__ == '__main__':
    main()
