export function rich(s: string) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
}

export function tidy(s: string) {
  return s.replace(/([A-Za-z0-9.+]) (?=[A-Za-z0-9])/g, '$1\u00a0')
}
