(function () {
	'use strict';

	angular
		.module('pastorino')
		.controller('Topbar', Topbar);

	/* @ngInject */
	function Topbar($state) {
		/*jshint validthis: true */
		var vm 		= this;
		vm.setView  = setView;

		vm.view	= false;
		vm.showView	= showView;

		activate();

		function activate() {

		}

        function showView() {
            if(!vm.view) {
                vm.view = true;
            } else {
                vm.view = false;
            }
        }


		function setView() {
			$state.go('application.pasteedit', {id: vm.id });
		}

	}

})();
