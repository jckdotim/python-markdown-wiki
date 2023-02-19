var webpack = require("webpack");
var path = require("path");

module.exports = {
  entry: "./entry.js",
  mode: "production",
  output: {
    path: __dirname + "/static/bundles",
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      },
      {
        test: /\.(woff|svg|ttf|eot)([\?]?.*)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[ext]"
            }
          }
        ]
      }
    ]
  },
  resolve: {
    modules: ["node_modules"]
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ]
};
