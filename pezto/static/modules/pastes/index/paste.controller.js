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
				title: vm.title,
				content: vm.content
			}).then(function(result) {
				console.log(result)
			});
		}

	}

})();