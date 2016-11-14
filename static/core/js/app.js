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
        $scope.submit = function(value){
            $.ajax({
            type: 'POST',
            url: '/core/user/connect',
            data: {
                friends: value,
            },
            success: function () {
                $scope.disabled = true
            }
        });
        }
    }
    ]);

sportsApp.controller('eventControl',['$scope','$http',
    function eventControl ($scope,$http) {
        $http.get('/core/api/event/').success(function(data) {
            $scope.events = data;
        });
        $scope.eventOptions = ['Public Events', 'Private Events', 'Both'];
        $scope.getEventDetails = function () {
        if($scope.event == 'Public Events') {
            $http.get('/core/api/publicEvent/').success(function (data) {
                $scope.events = data;
            });
        }else if($scope.event == 'Private Events') {
            $http.get('/core/api/privateEvent/').success(function (data) {
                $scope.events = data;
            });
        }else{
            $http.get('/core/api/event/').success(function (data) {
                $scope.events = data;
            });
        }
        }

        $scope.submit = function(value){
            $.ajax({
            type: 'POST',
            url: '/core/event/join',
            data: {
                event: value,
                //csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function () {
                var element = document.querySelector("#eventButton"+value);
                element.setAttribute("disabled","disabled");
            }
        });
        }
    }
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

sportsApp.controller('friendsControl',['$scope','$http', '$attrs',
    function friendsControl ($scope,$http,$attrs) {
        var userID = $attrs.something;
        $http.get('/core/api/friends/' + userID).success(function(data) {
            $scope.userFriendsDetail = data;
        });
    }
    ]);

sportsApp.controller('searchControl',['$scope','$http', '$attrs',
    function searchControl ($scope,$http,$attrs) {
        var string = $attrs.something;
        $http.get('core/api/searchUsers/' + string).success(function(data) {
            $scope.searchUsers = data;
        });
        $scope.submit = function(value){
            alert("control"+value)
            $.ajax({
            type: 'POST',
            url: '/core/user/connect',
            data: {
                friends: value,
            },
            success: function () {
                $scope.disabled = true
            }
        });
        }
    }
]);
