module.exports = {
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://back:8000',
        ws: false,
      },
      '^/auth/': {
        target: 'http://back:8000',
        ws: false,
      },
    }
  },
  pwa: {
    name: 'Stock Scout',
    themeColor: '#889399',
    msTileColor: '#47545D',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    workboxPluginMode: 'GenerateSW',
    iconPaths: {
        favicon32: 'static/img/icons/favicon-32x32.png',
        favicon16: 'static/img/icons/favicon-16x16.png',
        appleTouchIcon: 'static/img/icons/apple-touch-icon-152x152.png',
        maskIcon: 'static/img/icons/safari-pinned-tab.svg',
        msTileImage: 'static/img/icons/msapplication-icon-144x144.png'
      },
    manifestOptions: {
      icons: [
        {
          src: '/static/img/icons/favicon-32x32.png',
          sizes: '32x32',
          type: 'image/png'
        },
        {
          src: '/static/img/icons/favicon-16x16.png',
          sizes: '16x16',
          type: 'image/png'
        },
        {
          src: '/static/img/icons/apple-touch-icon-152x152.png',
          sizes: '152x152',
          type: 'image/png'
        },
        {
          src: 'static/img/icons/msapplication-icon-144x144.png',
          sizes: '144x144',
          type: 'image/png'
        },
      ]
    }
  },

  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
}

