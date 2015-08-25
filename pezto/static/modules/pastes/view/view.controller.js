(function () {
	'use strict';

	angular
		.module('pastorino')
		.controller('Pasteview', Pasteview);

	/* @ngInject */
	function Pasteview(PasteFactory, $state, $stateParams) {
		/*jshint validthis: true */
		var vm 		= this;

		activate();

		function activate() {
			PasteFactory.getSingle($stateParams.id).then(function (results) {
				vm.paste = results.data;
				console.log(vm.paste);
			});
		}

	}

})();