(function () {
	'use strict';

	angular
		.module('pastorino')
		.controller('Pasteview', Pasteview);

	/* @ngInject */
	function Pasteview(PasteFactory, $stateParams) {
		/*jshint validthis: true */
		var vm 		= this;
		vm.isEdit	= false;
		vm.setEdit	= setEdit;


		activate();

		function activate() {
			PasteFactory.getSingle($stateParams.id).then(function (results) {
				vm.paste = results.data;
				console.log(vm.paste);
			});
		}

		function setEdit() {
			PasteFactory.editSingle($stateParams.id, {
				title: vm.title,
				content: vm.content,
				password: vm.password
			}).then(function(result) {
				console.log(result);
			});
		}

	}

})();
