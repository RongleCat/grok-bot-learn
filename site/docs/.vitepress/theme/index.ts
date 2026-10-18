import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import GrokOrb from './GrokOrb.vue'
import Home from './Home.vue'
import JoinCard from './JoinCard.vue'
import DocEndCard from './DocEndCard.vue'
import PartBadge from './PartBadge.vue'
import SiteFooter from './SiteFooter.vue'
import { watchGroupClicks } from './track'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'nav-bar-title-before': () => h(GrokOrb, { size: 30, class: 'nav-orb' }),
      'doc-before': () => h(PartBadge),
      'doc-footer-before': () => h(DocEndCard),
      'layout-bottom': () => h(SiteFooter)
    }),
  enhanceApp({ app, router }) {
    app.component('GrokOrb', GrokOrb)
    app.component('Home', Home)
    app.component('JoinCard', JoinCard)
    if (typeof window !== 'undefined') watchGroupClicks(router)
  }
}
