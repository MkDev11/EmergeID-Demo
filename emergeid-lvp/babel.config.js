module.exports = function (api) {
    api.cache(true);
  
    const presets = [
      [
        "@babel/preset-env",
        {
          targets: "> 0.25%, not dead",
          useBuiltIns: "entry",
          corejs: 3,
        },
      ],
      "@babel/preset-react",
    ];
  
    const plugins = [
      "@babel/plugin-transform-runtime",
      "@babel/plugin-syntax-dynamic-import",
      "@babel/plugin-proposal-class-properties",
      "react-hot-loader/babel",
    ];
  
    return {
      presets,
      plugins,
    };
  };
  