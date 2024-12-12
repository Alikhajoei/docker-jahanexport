// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/i18n','@nuxtjs/sitemap', '@pinia/nuxt','@nuxt/image'],
  image: {
    domains: ['jahanexport.com'],  // Add your domains here
  },
  css: ['~/public/assets/css/main.css'],
  sitemap: {
    hostname: 'https://yourdomain.com',
    gzip: true,
    routes: ['/product/slug', '/about', '/contact'] // List dynamic routes here
  },
  i18n: {
    vueI18n: './i18n.config.ts' // if you are using custom path, default
  },
  app: {
    head: {
      title: '',
      meta: [
        { name: 'description', content: 'Jahan, ambassador of superior products in global markets' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { property: 'og:title', content: 'Jahan Export' },
        { property: 'og:description', content: 'Jahan, ambassador of superior products in global markets' },
        { property: 'og:image', content: '/assets/images/siteLogo.png' },
        { property: 'og:url', content: 'https://www.jahanexport.com' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Jahan Export' },
        { name: 'twitter:description', content: 'Jahan, ambassador of superior products in global markets' },
        { name: 'twitter:image', content: '/assets/images/siteLogo.png' },
      ],
      link: [
        { rel: 'canonical', href: 'https://www.jahanexport.com' },
        { rel: 'icon', type: 'image/png',href: '/assets/images/siteLogo.png' }
      ],
    }
  }
})