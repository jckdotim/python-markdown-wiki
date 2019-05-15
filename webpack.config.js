var webpack = require("webpack");
var path = require("path");

module.exports = {
  entry:   "./entry.js",
  output:  {
    path:     __dirname + "/static/bundles",
    filename: "bundle.js"
  },
  module:  {
    rules: [
      {test: /\.css$/, loader: "style-loader!css-loader"},
      {test: /\.(woff|svg|ttf|eot)([\?]?.*)$/, loader: "file-loader?name=[name].[ext]"}
    ]
  },
  resolve: {
      modules: ["bower_components", "node_modules"]
  },
  plugins: [
    new webpack.ProvidePlugin({
      $:      "jquery",
      jQuery: "jquery"
    })
  ]
};
