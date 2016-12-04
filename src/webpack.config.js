var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var path = require('path')
var atImport = require('postcss-import')

module.exports = {
  context: __dirname,
  entry: './assets/js/index',
  output: {
    path: path.resolve('./assets/bundles'),
    filename: "[name]-[hash].js"
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      },
      {
        test: /\.scss$/,
        loader: 'style!css!sass!postcss?syntax=postcss-scss'
      }
    ]
  },
}
