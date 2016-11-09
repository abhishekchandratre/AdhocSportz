/*
*
 * Created by sampu on 10/31/16.

var userControllers = angular.module('sportsApp',[]);
userControllers.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
userControllers.controller('userControl',['$scope','$http', '$attrs',
    function ($scope,$http,$attrs) {
        alert("coming");
        var userID = $attrs.something;
        alert(userID);
        $http.get('/core/api/user/' + userID).success(function(data) {
            $scope.userDetail = data;
        });
    }
    ]);

sportsApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

sportsApp.controller('userControl',['$scope','$http',
    function ($scope,$http) {
        alert("coming");
        var userID = $scope.$id;
        alert(userID);
        $http.get('/core/api/user/'+userID).success(function(data) {
            $scope.userDetail = data;
        });
    }
    ]);

var eventControllers = angular.module('sportsApp',[]);
eventControllers.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


eventControllers.controller('eventControl',['$scope','$http',
    function ($scope,$http) {
        $http.get('/core/api/event/').success(function(data) {
            $scope.events = data;
        });
    }
    ]);



*/
