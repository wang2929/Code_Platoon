const { defineConfig } = require("cypress");

module.exports = defineConfig({
    // e2e is a custom config object
    // baseURL defines where app will run
    // supportFile to false disables custom support files
    e2e: {
        baseUrl: "http://localhost:5173/",
        supportFile: false,
    },
    // window size and disable video recording
    viewportWidth:1024,
    viewportHeight:768,
    video:false,
})