module.exports = function (grunt) {
  grunt.initConfig({
    panda: {
      test4: {
        options: {
          spawnLimit: 2,
          stripMeta: '````',
          metaDataPath: "test/meta.yaml",
          pandocOptions: "-t html5 --standalone --smart --section-divs --mathjax"
        },
        files: [
          {
            expand: true,
            cwd: "test/test4",
            src: "**/*.md",
            dest: "actual/test4",
            ext: ".html"
          }
        ]
      }
    }
  });

  // Load the grunt-panda plugin
  grunt.loadNpmTasks('grunt-panda');

  // Default task
  grunt.registerTask('default', ['panda']);
};