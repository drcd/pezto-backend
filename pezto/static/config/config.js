var app = angular.module('pastorino', ['ui.router', 'mm.foundation']);

app.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/');
});