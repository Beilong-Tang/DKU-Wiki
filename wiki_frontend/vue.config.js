const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// to export to the server
// module.exports = {
//   publicPath: './',
//   lintOnSave: false
// }
