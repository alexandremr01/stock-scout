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
    scope: '/',
    start_url: 'index.html',
    themeColor: '#889399',
    msTileColor: '#47545D',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    workboxPluginMode: 'GenerateSW',
    sw: 'static/service-worker.js',

    workboxOptions: {
      navigateFallback: '/index.html',
    },
    iconPaths: {
        favicon32: 'img/icons/icon.png',
        favicon16: 'img/icons/icon.png',
        appleTouchIcon: 'img/icons/icon.png',
        maskIcon: 'img/icons/icon.svg',
        msTileImage: 'img/icons/icon.png'
      },
    manifestOptions: {
      icons: [
        {
          src: '/static/img/icons/icon.png',
          sizes: '256x256',
          type: 'image/png'
        },
      ]
    },
  },

  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: '',
  publicPath: 'static',
}

