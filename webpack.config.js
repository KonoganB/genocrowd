const webpack = require('webpack');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

let config = {
    entry: [
        './genocrowd/react/src/index.jsx'
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                loader: ['style-loader', 'css-loader']
            }
        ]
    },
    output: {
        path: __dirname + '/genocrowd/static/js',
        filename: 'genocrowd.js'
    },
    resolve: {
        extensions: ['.js', '.jsx'],
    },
    // plugins: [
    //   new webpack.DefinePlugin({
    //     'process.env': {
    //       'NODE_ENV': JSON.stringify('production')
    //     }
    //   }),
    //   new UglifyJsPlugin({
    //     cache: true,
    //     parallel: true,
    //     uglifyOptions: {
    //       compress: true,
    //       ecma: 6,
    //       mangle: true
    //     },
    //     sourceMap: true
    //   })
    // ]


};

module.exports = config;
