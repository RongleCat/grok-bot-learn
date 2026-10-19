import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import GrokOrb from './GrokOrb.vue'
import Home from './Home.vue'
import EcoIndex from './EcoIndex.vue'
import ClipperLanding from './ClipperLanding.vue'
import BotHire from './BotHire.vue'
import JoinCard from './JoinCard.vue'
import DocEndCard from './DocEndCard.vue'
import NavGroupPill from './NavGroupPill.vue'
import PartBadge from './PartBadge.vue'
import SiteFooter from './SiteFooter.vue'
import { watchGroupClicks } from './track'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'nav-bar-title-before': () => h(GrokOrb, { size: 30, class: 'nav-orb' }),
      'nav-bar-content-after': () => h(NavGroupPill),
      'doc-before': () => h(PartBadge),
      'doc-footer-before': () => h(DocEndCard),
      'layout-bottom': () => h(SiteFooter)
    }),
  enhanceApp({ app, router }) {
    app.component('GrokOrb', GrokOrb)
    app.component('Home', Home)
    app.component('JoinCard', JoinCard)
    app.component('EcoIndex', EcoIndex)
    app.component('ClipperLanding', ClipperLanding)
    app.component('BotHire', BotHire)
    if (typeof window !== 'undefined') watchGroupClicks(router)
  }
}
