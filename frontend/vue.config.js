const { defineConfig } = require('@vue/cli-service');
const path = require('path');

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    // Add an alias for easier imports
    config.resolve.alias.set('@i18n', path.resolve(__dirname, 'src/i18n'));
  },
  pluginOptions: {
    i18n: {
      locale: 'en', // Set the default locale
      fallbackLocale: 'en', // Set the fallback locale
      localeDir: 'locales', // Directory where your locale files are located
      enableInSFC: true, // Enable i18n support in Single File Components
    },
  },
});
