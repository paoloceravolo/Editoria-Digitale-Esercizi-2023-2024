module.exports = function (grunt) {
  grunt.initConfig({
    panda: {
      test3: {
        options: {
          spawnLimit: 3,
        },
        files: [
          {
            expand: true,
            cwd: "test/test3",
            src: "**/*.md",
            dest: "actual/test3",
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