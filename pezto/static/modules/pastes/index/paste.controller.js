(function () {
	'use strict';

	angular
		.module('pastorino')
		.controller('Pasto', Pasto);

	/* @ngInject */
	function Pasto(PasteFactory, $state, $stateParams) {
		/*jshint validthis: true */
		var vm 			= this;
		vm.makePaste	= makePaste;


		activate();

		function activate() {

		}

		function makePaste() {
			PasteFactory.addPaste({
				header: vm.header,
				body: vm.body
			}).then(function(result) {
				console.log(result.data._id);
				$state.go('application.pasteview', {id: result.data._id });
			});
		}

	}

})();