// Gruntfile.js

module.exports = function(grunt) {

    // ===========================================================================
    // CONFIGURE GRUNT ===========================================================
    // ===========================================================================
    grunt.initConfig({
        sass: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'static/styles/main.css': 'static/styles/main.scss'
                }
            }
        },
        shell: {
            target: {
                command: 'python manage.py runserver'
            }
        },
        watch: {
            css: {
                files: ['static/styles/**/*.scss'],
                tasks: ['sass']
            }
        },
        concurrent: {
            options: {
                logConcurrentOutput: true
            },
            tasks: ['watch', 'shell']
        }
    });

    // ===========================================================================
    // LOAD GRUNT PLUGINS ========================================================
    // ===========================================================================
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-shell');

    grunt.registerTask('serve', ['sass', 'concurrent']);
};
