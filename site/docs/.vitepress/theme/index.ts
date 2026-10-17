import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import GrokOrb from './GrokOrb.vue'
import Home from './Home.vue'
import PartBadge from './PartBadge.vue'
import SiteFooter from './SiteFooter.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'nav-bar-title-before': () => h(GrokOrb, { size: 30, class: 'nav-orb' }),
      'doc-before': () => h(PartBadge),
      'layout-bottom': () => h(SiteFooter)
    }),
  enhanceApp({ app }) {
    app.component('GrokOrb', GrokOrb)
    app.component('Home', Home)
  }
}
