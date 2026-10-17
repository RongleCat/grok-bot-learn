const SCRIPT = 'https://cloud.umami.is/script.js'
const SEND = 'https://gateway.umami.is/api/send'

async function script(request, ctx) {
  const cache = caches.default
  const key = new Request(new URL('/s/a.js', request.url).toString())
  let res = await cache.match(key)
  if (!res) {
    const up = await fetch(SCRIPT, { cf: { cacheTtl: 3600 } })
    res = new Response(up.body, up)
    res.headers.set('Cache-Control', 'public, max-age=3600')
    res.headers.set('Content-Type', 'application/javascript; charset=utf-8')
    if (up.ok) ctx.waitUntil(cache.put(key, res.clone()))
  }
  return res
}

async function send(request) {
  if (request.method !== 'POST') return new Response(null, { status: 405 })
  const ip = request.headers.get('CF-Connecting-IP') || ''
  const h = new Headers({
    'Content-Type': 'application/json',
    'User-Agent': request.headers.get('User-Agent') || ''
  })
  if (ip) {
    h.set('X-Forwarded-For', ip)
    h.set('X-Real-IP', ip)
  }
  const lang = request.headers.get('Accept-Language')
  if (lang) h.set('Accept-Language', lang)
  const up = await fetch(SEND, { method: 'POST', headers: h, body: await request.text() })
  return new Response(up.body, {
    status: up.status,
    headers: { 'Content-Type': up.headers.get('Content-Type') || 'application/json', 'Cache-Control': 'no-store' }
  })
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url)
    const proto = request.headers.get('x-forwarded-proto') || url.protocol.replace(':', '')
    if (proto === 'http') {
      url.protocol = 'https:'
      return Response.redirect(url.toString(), 301)
    }
    if (url.pathname === '/s/a.js') return script(request, ctx)
    if (url.pathname === '/s/api/send') return send(request)
    const res = await env.ASSETS.fetch(request)
    if (url.hostname === 'bot.tiezhu.si') {
      const h = new Headers(res.headers)
      h.set('Strict-Transport-Security', 'max-age=31536000')
      return new Response(res.body, { status: res.status, statusText: res.statusText, headers: h })
    }
    return res
  }
}
