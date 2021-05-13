module.exports = {
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://back:8000',
        ws: false,
      }
    }
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
}

