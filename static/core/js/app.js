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
            $scope.errorFlag = false;
        });
        $scope.eventOptions = ['Public Events', 'Private Events'];
        $scope.getEventDetails = function () {
        if($scope.event == 'Public Events') {
            $http.get('/core/api/publicEvent/').success(function (data) {
                $scope.events = data;
                $scope.errorFlag = false;
            });
        }else if($scope.event == 'Private Events') {
            $http.get('/core/api/privateEvent/').success(function (data) {
                    $scope.events = data;
            }).catch(function (data) {
                $scope.events = "";
                $scope.errorFlag = true;
                //$scope.errorMessage = "There are no Private events to show";
            });
        }else{
            $http.get('/core/api/event/').success(function (data) {
                $scope.events = data;
                $scope.errorFlag = false;
            });
        }
        }

        $scope.submit = function(value1,value2){

            $.ajax({
            type: 'POST',
            url: '/core/event/join',
            data: {
                eventName: value1,
                eventID: value2,
                //csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function () {
                var element = document.querySelector("#eventButton"+value2);
                element.setAttribute("disabled","disabled");
            }
        });
        }
    }
    ]);

sportsApp.controller('approveControl',['$scope','$http',
    function approveControl ($scope,$http) {
        $scope.submit = function (value, value2) {
            $.ajax({
                type: 'POST',
                url: '/core/event/approve',
                data: {
                    eventPlayerID: value,
                    approval: value2,
                    //csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function () {
                    alert("Email sent to the user!!")
                    if (value2 == "approve") {
                        var element = document.querySelector("#approve" + value);
                        element.setAttribute("disabled", "disabled");
                    } else {
                        var element = document.querySelector("#reject" + value);
                        element.setAttribute("disabled", "disabled");
                    }
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
        $scope.acceptUser = function (value) {
            $.ajax({
                type: 'POST',
                url: 'core/user/accept',
                data: {
                    id: value,
                },
                success: function () {
                    location.reload();
                }
            });
        }
        $scope.rejectUser = function (value) {
            $.ajax({
                type: 'POST',
                url: 'core/user/reject',
                data: {
                    id: value,
                },
                success: function () {
                    location.reload();
                }
            });
        }
    }
    ]);




sportsApp.controller('searchControl',['$scope','$http', '$attrs',
    function searchControl ($scope,$http,$attrs) {
        var string = $attrs.something;
        $http.get('core/api/searchUsers/' + string).success(function(data) {
            $scope.searchUsers = data;
        });
        $scope.submit = function(value){
            $.ajax({
            type: 'POST',
            url: '/core/user/connect',
            data: {
                friends: value,
            },
            success: function () {
                var element = document.querySelector("#connect"+value);
                element.setAttribute("disabled","disabled");
            }
        });
        }
    }
]);

sportsApp.controller('ratingControl',['$scope','$http',
    function ratingControl ($scope,$http) {
        $scope.ratingValue = function (user) {
          $('#stars'+user).on('starrr:change', function(e, value){
                $.ajax({
            type: 'POST',
            url: '/core/user/rating',
            data: {
                rating: value,
                user: user,
            },
            success: function () {
            }
        });
          })
        }
}
]);

/*
$( document ).ready(function() {
  $('#stars').on('starrr:change', function(e, value){
       alert("rating");
      alert(value)
       $.ajax({
            type: 'POST',
            url: '/core/user/rating',
            data: {
                rating: value,
            },
            success: function () {
                alert("rating success");
            }
        });
        $('#count').html(value);
  });
});
*/

/*
sportsApp.controller('ratingControl',['$scope','$http',
    function ratingControl ($scope,$http) {
        $scope.ratingValue = function (value) {
            var element = document.getElementById("stars");
            alert(element);
        alert($scope.rating)
        alert(value)
        }
}
]);*/
