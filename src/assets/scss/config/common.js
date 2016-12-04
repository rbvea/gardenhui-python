var clrs = require('colors.css/js/colors.js')
var objectAssign = require('object-assign')

module.exports = objectAssign({}, clrs, {
  desktop: '(min-width: 80em)',
  handheld: '(max-width: 48em)'
})
