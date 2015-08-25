(function () {
	'use strict';

	angular
		.module('pastorino')
		.factory('PasteFactory', PasteFactory);

	/* @ngInject */
	function PasteFactory($http, $q) {

		var service = {
			getSingle:		getSingle,
			addPaste:		addPaste
		};

		return service;

		function addPaste(content) {
			var deferred = $q.defer();

			var url = '/paste';


			$http.post(url, content, {
				headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
			}).then(function(results) {
				deferred.resolve(results);
			}, function(err) {
				deferred.reject(err);
			});
			return deferred.promise;
		}

		function getSingle(id) {
			var deferred = $q.defer();

			var url = '/paste/' + id;

			var pastePromise = $http.get(url, id);

			pastePromise.then(function(results) {
				deferred.resolve(results);
			}, function(err) {
				deferred.reject(err);
			});

			return deferred.promise;
		}

	}

})();