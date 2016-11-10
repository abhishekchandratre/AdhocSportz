/**
 * Created by sampu on 10/31/16.
 */
'use strict';

var sportsApp = angular.module('sportsApp',['ngMap']);

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
        $http.get('/core/api/user/' + userID).success(function(data) {
            $scope.userDetail = data;
        });
    }
    ]);

sportsApp.controller('eventControl',['$scope','$http',
    function eventControl ($scope,$http) {
        $scope.disable = "";
        $http.get('/core/api/event/').success(function(data) {
            $scope.events = data;
        });

        $scope.submit = function(value){
            $.ajax({
            type: 'POST',
            url: '/core/event/join',
            data: {
                event: value,
                //csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function () {
                $scope.disable = true;
                $scope.$apply();
            }
        });
        }}
    ]);

sportsApp.controller('eventView',['$scope','$http',
    function eventView ($scope,$http) {
        $http.get('/core/api/myevent/').success(function(data) {
            $scope.myEvents = data;
        });
    }
    ]);

sportsApp.controller('mapEvent',['$scope','$http',
    function mapEvent ($scope,$http,NgMap) {
        $http.get('/core/api/event/').success(function (data) {
            $scope.mapEvents = data;
        });
    }

    ]);
