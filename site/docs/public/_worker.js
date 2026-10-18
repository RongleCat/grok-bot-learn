const SCRIPT = 'https://cloud.umami.is/script.js'
const SEND = 'https://gateway.umami.is/api/send'

const MOVED = {
  '/guide/00-what-is': '/part1/01-what-is',
  '/guide/00b-compare': '/part1/01-what-is',
  '/guide/01-plans': '/part1/02-plans',
  '/guide/02-install': '/part1/03-install',
  '/guide/03-handoff': '/part1/04-handoff',
  '/guide/04-messaging': '/part3/22-feishu-wechat',
  '/guide/05-bots': '/part1/09-group-team',
  '/guide/06-computer': '/part1/05-computer',
  '/guide/07-memory': '/part1/06-memory',
  '/guide/08-apps': '/part1/07-apps',
  '/guide/09-routines': '/part1/08-skills-routines',
  '/guide/10-team': '/part1/09-group-team',
  '/guide/11-usage': '/part1/10-usage',
  '/guide/12-safety': '/part1/11-safety',
  '/guide/13-backup': '/part3/21-backup',
  '/guide/14-faq': '/part4/25-faq',
  '/start/what-is': '/part1/01-what-is',
  '/start/compare': '/part1/01-what-is',
  '/start/plans': '/part1/02-plans',
  '/start/quickstart': '/part1/03-install',
  '/start/first-handoff': '/part1/04-handoff',
  '/start/faq': '/part4/25-faq',
  '/core/bots': '/part1/09-group-team',
  '/core/computer': '/part1/05-computer',
  '/core/group-chats': '/part1/09-group-team',
  '/core/memory': '/part1/06-memory',
  '/core/messaging': '/part3/22-feishu-wechat',
  '/core/plugins': '/part1/07-apps',
  '/core/skills-routines': '/part1/08-skills-routines',
  '/advanced/automation': '/part3/20-automation',
  '/advanced/backup': '/part3/21-backup',
  '/advanced/im': '/part3/22-feishu-wechat',
  '/advanced/security': '/part1/11-safety',
  '/advanced/team-orchestration': '/part3/19-orchestration',
  '/advanced/usage': '/part1/10-usage',
  '/appendix/a-orchestration': '/part3/19-orchestration',
  '/appendix/b-automation': '/part3/20-automation',
  '/appendix/c-im': '/part3/22-feishu-wechat',
  '/appendix/d-enterprise': '/part4/23-enterprise',
  '/appendix/e-resources': '/cases/',
  '/admin': '/part4/23-enterprise',
  '/resources': '/cases/',
  '/zz-bots': '/',
  '/cases/outdated': '/part1/02-plans',
  '/guide': '/part1/01-what-is',
  '/start': '/part1/01-what-is',
  '/core': '/part1/01-what-is',
  '/advanced': '/part3/19-orchestration',
  '/appendix': '/part3/19-orchestration',
  '/part1': '/part1/01-what-is',
  '/part2': '/part2/12-content',
  '/part3': '/part3/19-orchestration',
  '/part4': '/part4/23-enterprise'
}

function moved(pathname) {
  const p = pathname.replace(/\/index(\.html)?$/, '').replace(/\.html$/, '').replace(/\/+$/, '')
  return MOVED[p]
}

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

async function ranged(request, res) {
  const m = /^bytes=(\d*)-(\d*)$/.exec(request.headers.get('Range') || '')
  const buf = new Uint8Array(await res.arrayBuffer())
  const size = buf.byteLength
  const h = new Headers(res.headers)
  h.set('Accept-Ranges', 'bytes')
  let start = m && m[1] !== '' ? Number(m[1]) : NaN
  let end = m && m[2] !== '' ? Number(m[2]) : size - 1
  if (m && m[1] === '' && m[2] !== '') {
    start = Math.max(0, size - Number(m[2]))
    end = size - 1
  }
  end = Math.min(end, size - 1)
  if (!m || isNaN(start) || start > end || start >= size) {
    h.set('Content-Range', `bytes */${size}`)
    h.delete('Content-Length')
    return { body: null, status: 416, headers: h }
  }
  h.set('Content-Range', `bytes ${start}-${end}/${size}`)
  h.set('Content-Length', String(end - start + 1))
  return { body: buf.subarray(start, end + 1), status: 206, headers: h }
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
    if (/^\/xhs\/?$/i.test(url.pathname) && url.pathname !== '/xhs') {
      return Response.redirect(new URL('/xhs' + url.search, url.origin).toString(), 301)
    }
    const to = moved(url.pathname)
    if (to) return Response.redirect(new URL(to, url.origin).toString(), 301)
    const res = await env.ASSETS.fetch(request)
    if (/\.mp4$/i.test(url.pathname) && res.status === 200) {
      const r = request.headers.has('Range') && request.method === 'GET' ? await ranged(request, res) : { body: res.body, status: 200, headers: new Headers(res.headers) }
      r.headers.set('Accept-Ranges', 'bytes')
      if (url.hostname === 'bot.tiezhu.si') r.headers.set('Strict-Transport-Security', 'max-age=31536000')
      else if (url.hostname.endsWith('.pages.dev')) r.headers.set('X-Robots-Tag', 'noindex')
      return new Response(r.body, { status: r.status, headers: r.headers })
    }
    const h = new Headers(res.headers)
    if (url.hostname === 'bot.tiezhu.si') {
      h.set('Strict-Transport-Security', 'max-age=31536000')
    } else if (url.hostname.endsWith('.pages.dev')) {
      h.set('X-Robots-Tag', 'noindex')
    }
    return new Response(res.body, { status: res.status, statusText: res.statusText, headers: h })
  }
}
