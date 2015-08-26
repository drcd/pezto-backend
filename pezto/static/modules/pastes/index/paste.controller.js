(function () {
	'use strict';

	angular
		.module('pastorino')
		.controller('Pasto', Pasto);

	/* @ngInject */
	function Pasto(PasteFactory, $state) {
		/*jshint validthis: true */
		var vm 			= this;
		vm.makePaste	= makePaste;
        vm.pass         = false;

		activate();


		function activate() {

		}

		function makePaste() {
			PasteFactory.addPaste({
				title: vm.title,
				content: vm.content,
                password: vm.password
			}).then(function(result) {
				console.log(result);
				$state.go('application.pasteview', {id: result.data.uid });
			});
		}

	}

})();