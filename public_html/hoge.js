var phonecatApp = angular.module('phonecatApp', ["ngResource"]);

phonecatApp.controller('PhoneListCtrl', ["$scope", "$resource", function ($scope, $resource) {
    var contents = $resource("./data.json");
    $scope.phones = contents.query();
}]);
