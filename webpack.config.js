var webpack = require("webpack");
var path = require("path");
var BowerWebpackPlugin = require('bower-webpack-plugin');

module.exports = {
  entry:   "./entry.js",
  output:  {
    path:     __dirname + "/static/bundles",
    filename: "bundle.js"
  },
  module:  {
    loaders: [
      {test: /\.css$/, loader: "style!css"},
      {test: /\.(woff|svg|ttf|eot)([\?]?.*)$/, loader: "file-loader?name=[name].[ext]"}
    ]
  },
  resolve: {
      root: [path.join(__dirname, "bower_components")]
  },
  plugins: [
    new webpack.ResolverPlugin(
      new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
    ),
    new webpack.ProvidePlugin({
      $:      "jquery",
      jQuery: "jquery"
    })
  ]
};
