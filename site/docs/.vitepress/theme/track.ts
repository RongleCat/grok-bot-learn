type Props = Record<string, string>

export function track(name: string, data: Props) {
  const u = (window as unknown as { umami?: { track: (n: string, d: Props) => void } }).umami
  if (u) u.track(name, data)
}

export function lastFrom() {
  try {
    return sessionStorage.getItem('tz-from') || 'direct'
  } catch {
    return 'direct'
  }
}

function sourceOf(a: Element) {
  const tagged = a.closest('[data-from]') as HTMLElement | null
  if (tagged?.dataset.from) return tagged.dataset.from
  if (a.closest('.VPNav, .VPNavScreen')) return 'nav'
  if (a.closest('.tz-footer')) return 'footer'
  return 'link'
}

export function watchGroupClicks() {
  document.addEventListener(
    'click',
    (e) => {
      const a = (e.target as Element | null)?.closest?.('a[href]') as HTMLAnchorElement | null
      if (!a) return
      const url = new URL(a.href, location.href)
      if (url.origin !== location.origin || url.pathname.replace(/\.html$/, '') !== '/group') return
      const from = sourceOf(a)
      try {
        sessionStorage.setItem('tz-from', from)
      } catch {}
      track('group-click', { from, page: location.pathname })
    },
    true
  )
}
