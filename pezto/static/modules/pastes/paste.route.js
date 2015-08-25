(function() {
	'use strict';

	angular.module('pastorino')
		/* @ngInject */
		.config(function ($stateProvider) {

			var Index = {
				name: 'application.pasto',
				url: '/',
				views: {
					'main@application': {
						templateUrl: 'static/modules/pastes/index/paste.template.html',
						controller: 'Pasto',
						controllerAs: 'pasto'
					}
				}
			};

			var View = {
				name: 'application.pasteview',
				url: '/paste/:id',
				views: {
					'main@application': {
						templateUrl : 'static/modules/pastes/view/view.template.html',
						controller  : 'Pasteview',
						controllerAs: 'view'
					}
				}
			};

			var Edit = {
				name: 'application.pasteedit',
				url: '/create',
				views: {
					'main@application': {
						templateUrl: 'static/modules/pastes/edit/edit.template.html',
						controller: 'Pasteedit',
						controllerAs: 'edit'
					}
				}
			};

			$stateProvider.state(Index);
			$stateProvider.state(View);
			$stateProvider.state(Edit);
		});
})();