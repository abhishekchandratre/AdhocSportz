/**
 * Created by sampu on 10/31/16.
 */
'use strict';

var sportsApp = angular.module('sportsApp',[]);

sportsApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

sportsApp.config([
    '$httpProvider',function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

sportsApp.controller('userControl',['$scope','$http', '$attrs',
    function userControl ($scope,$http,$attrs) {
        var userID = $attrs.something;
        alert(userID);
        $http.get('/core/api/user/' + userID).success(function(data) {
            $scope.userDetail = data;
        });
    }
    ]);

sportsApp.controller('eventControl',['$scope','$http',
    function eventControl ($scope,$http) {
        $http.get('/core/api/event/').success(function(data) {
            $scope.events = data;
        });
    }
    ]);

sportsApp.controller('eventView',['$scope','$http',
    function eventView ($scope,$http) {
        $http.get('/core/api/myevent/').success(function(data) {
            $scope.myEvents = data;
        });
    }
    ]);