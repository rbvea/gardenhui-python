var OpenBrowserWebpackPlugin = require('open-browser-webpack-plugin')
var path = require('path')

module.exports = {
  output: {
    publicPath: 'http://localhost:8080/assets/',
    path: path.resolve('../assets/bundles'),
    filename: "[name]-[hash].js"
  },
  plugins: [
    new OpenBrowserWebpackPlugin({
      url: 'http://localhost:8000'
    })
  ]
}
