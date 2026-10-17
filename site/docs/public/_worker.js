export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    const proto = request.headers.get('x-forwarded-proto') || url.protocol.replace(':', '')
    if (proto === 'http') {
      url.protocol = 'https:'
      return Response.redirect(url.toString(), 301)
    }
    const res = await env.ASSETS.fetch(request)
    if (url.hostname === 'bot.tiezhu.si') {
      const h = new Headers(res.headers)
      h.set('Strict-Transport-Security', 'max-age=31536000')
      return new Response(res.body, { status: res.status, statusText: res.statusText, headers: h })
    }
    return res
  }
}
