import re, json, shutil, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, 'site/docs/.vitepress/dist')
out = sys.argv[1] if len(sys.argv) > 1 else '/workspace/learn-edgeone/out'
shutil.rmtree(out, ignore_errors=True)
shutil.copytree(src, out)
os.remove(os.path.join(out, '_worker.js'))

w = open(os.path.join(root, 'site/docs/public/_worker.js')).read()
moved = re.findall(r"'(/[^']*)':\s*'(/[^']*)'", w.split('const MOVED')[1].split('}')[0])
red = []
for k, v in moved:
    red.append({'source': k, 'destination': v, 'statusCode': 301})
    if k.count('/') == 1:
        red.append({'source': k + '/', 'destination': v, 'statusCode': 301})
for k in ['/xhs/', '/XHS', '/XHS/', '/Xhs', '/Xhs/']:
    red.append({'source': k, 'destination': '/xhs', 'statusCode': 301})
if len(red) > 100:
    sys.exit(f'too many redirects: {len(red)}')

cfg = {
    'redirects': red,
    'headers': [
        {'source': '/assets/*', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]},
        {'source': '/*', 'headers': [{'key': 'Strict-Transport-Security', 'value': 'max-age=31536000'}]},
        {'source': '/*.mp4', 'headers': [{'key': 'Accept-Ranges', 'value': 'bytes'}]}
    ]
}
sec = [{'key': 'X-Content-Type-Options', 'value': 'nosniff'}, {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'}, {'key': 'X-Frame-Options', 'value': 'SAMEORIGIN'}]
cfg['headers'][1]['headers'] += sec
html = [{'key': 'Content-Type', 'value': 'text/html; charset=utf-8'}]
for src in ['/', '/part1/:slug', '/part2/:slug', '/part3/:slug', '/part4/:slug', '/cases/:slug', '/cases/', '/bots/', '/ecosystem/', '/ecosystem/grok-bot-clipper', '/changelog/', '/tools/', '/tools/:slug', '/group', '/about', '/xhs']:
    cfg['headers'].append({'source': src, 'headers': html})
cfg['headers'].append({'source': '/*.md', 'headers': [{'key': 'Content-Type', 'value': 'text/markdown; charset=utf-8'}]})
cfg['headers'].append({'source': '/llms.txt', 'headers': [{'key': 'Content-Type', 'value': 'text/plain; charset=utf-8'}]})
cfg['headers'].append({'source': '/llms-full.txt', 'headers': [{'key': 'Content-Type', 'value': 'text/plain; charset=utf-8'}]})
json.dump(cfg, open(os.path.join(out, 'edgeone.json'), 'w'), ensure_ascii=False, indent=1)

fn = os.path.join(out, 'edge-functions/s')
os.makedirs(fn, exist_ok=True)
open(os.path.join(fn, '[[default]].js'), 'w').write('''const SCRIPT = 'https://cloud.umami.is/script.js'
const SEND = 'https://gateway.umami.is/api/send'

async function script() {
  const up = await fetch(SCRIPT)
  return new Response(up.body, {
    status: up.status,
    headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'public, max-age=3600' }
  })
}

async function send(req) {
  if (req.method !== 'POST') return new Response(null, { status: 405 })
  const h = new Headers({ 'Content-Type': 'application/json', 'User-Agent': req.headers.get('User-Agent') || '' })
  const ip = req.headers.get('EO-Connecting-IP') || (req.headers.get('X-Forwarded-For') || '').split(',')[0].trim()
  if (ip) {
    h.set('X-Forwarded-For', ip)
    h.set('X-Real-IP', ip)
  }
  const lang = req.headers.get('Accept-Language')
  if (lang) h.set('Accept-Language', lang)
  const up = await fetch(SEND, { method: 'POST', headers: h, body: await req.text() })
  return new Response(up.body, {
    status: up.status,
    headers: { 'Content-Type': up.headers.get('Content-Type') || 'application/json', 'Cache-Control': 'no-store' }
  })
}

export async function onRequest(context) {
  const path = new URL(context.request.url).pathname
  if (path === '/s/a.js') return script()
  if (path === '/s/api/send') return send(context.request)
  return new Response('Not Found', { status: 404 })
}
''')
print(len(red), 'redirects ->', out)
