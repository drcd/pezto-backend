(function() {
	'use strict';

	angular.module('pastorino')
		/* @ngInject */
		.config(function ($stateProvider) {

			var Application = {
				name: 'application',
				abstract: true,
				views : {
					// Wrapping view
					'application': {
						templateUrl: 'static/modules/_application/application.template.html'
					},
					// Topbar
					'topbar@application': {
						templateUrl: 'static/modules/shared/topbar/topbar.template.html',
						controller: 'Topbar',
						controllerAs: 'topbar'
					}
				}
			};


			$stateProvider.state(Application);
		});
})();