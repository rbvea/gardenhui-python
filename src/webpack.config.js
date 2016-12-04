var webpack = require('webpack')
var merge = require('webpack-merge')
var base = require('./webpack/base.js')

if(process.env.NODE_ENV === 'production') {
  var extra = require('./webpack/prod.js')
} else {
  var extra = require('./webpack/dev.js')
}

module.exports = merge(base, extra)
