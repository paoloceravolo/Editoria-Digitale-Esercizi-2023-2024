# Esercizi con grunt-panda

## Getting Started

[Grunt-panda](https://github.com/gmp26/grunt-panda) is a [Grunt](https://gruntjs.com) plugin for converting documetns using [Pandoc](https://pandoc.org)

If you haven't used [Grunt](https://gruntjs.com) before, be sure to check out the Getting Started guide, as it explains how to install Grunt, create a Gruntfile as well as install and use Grunt plugins. 

To use this plugin you have to install it

```
npm install grunt-panda --save-dev
```

## A simple example

A simple example of a Gruntfile executing grunt-panda is 

```
module.exports = function (grunt) {
  grunt.initConfig({
    panda: {
      test4: {
        options: {
          spawnLimit: 3
        },
        files: [
          {
            expand: true,
            cwd: "test/fixtures/test4",
            src: "**/*.md",
            dest: "test/actual/test4",
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
```

 Running ``grunt`` in the terminal will execute the Gruntfile and the default panda task. The command ``grunt taskName`` will execute another task.

Adjust the paths and options as needed for your project.

The spawnLimit option in the grunt-panda configuration controls the maximum number of concurrent subprocesses (spawns) that can be used to process the markdown files. This option is particularly useful when you are processing a large number of files concurrently.

When you run tasks in Grunt, it may spawn multiple subprocesses to parallelize the execution of tasks. The spawnLimit option allows you to limit the number of concurrent subprocesses, preventing the system from being overloaded with too many simultaneous operations.

But be careful! If you are concatenating markdown, the order is likely to matter and can only be guaranteed when the spawnLimit is 1.