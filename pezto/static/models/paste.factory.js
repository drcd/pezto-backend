(function () {
	'use strict';

	angular
		.module('pastorino')
		.factory('PasteFactory', PasteFactory);

	/* @ngInject */
	function PasteFactory($http, $q) {

		var service = {
			getPaste: 	getPaste,
			getSingle:		getSingle,
			addPaste:	addPaste
		};

		return service;

		function addPaste(article) {
			var deferred = $q.defer();

			var url = '/api/pastes';

			$http.post(url,article).then(function(results) {
				deferred.resolve(results);
			}, function(err) {
				deferred.reject(err);
			});
			return deferred.promise;
		}

		function getSingle(id) {
			var deferred = $q.defer();

			var url = '/api/paste/' + id;

			var pastePromise = $http.get(url, id);

			pastePromise.then(function(results) {
				deferred.resolve(results);
			}, function(err) {
				deferred.reject(err);
			});

			return deferred.promise;
		}

		function getPaste() {
			var deferred = $q.defer();

			var url = '/api/pastes';

			var storesPromise = $http.get(url);

			storesPromise.then(function(results) {

				deferred.resolve(results);
			}, function(err) {
				deferred.reject(err);
			});

			return deferred.promise;
		}

	}

})();