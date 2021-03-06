 angular.module("componentApp", [])
       .controller("componentController", function($scope) {
         $scope.isShowContent = false;
         $scope.showComponent = function() {
           $scope.isShowContent = !$scope.isShowContent;
           };
       });
      