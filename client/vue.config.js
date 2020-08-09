
const portfinder = require('portfinder')

const proxy = require('http-proxy-middleware');

module.exports = {
  baseUrl: "/",
  outputDir: "../server/static",
  assetsDir: "static",
  devServer: {
    proxy: {
      "/api": {
        target: 'http://localhost:8000',
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          "^/api": "/api"
        }
      }
    },
    host: "0.0.0.0",
    port: 8025,
    https: false,
    hotOnly: false
  },

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false
    }
  }
};