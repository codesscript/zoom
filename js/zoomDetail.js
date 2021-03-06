(function(angular) {
  'use strict';

function zoomDetailController($scope, $element, $attrs) {
   var $ctrl=this;
   $ctrl.$onInit = () => {
   $ctrl.meetingUrl='/meeting.html?mn='+$ctrl.meet+'&name='+$ctrl.name+'&email=&pwd='+$ctrl.pwd+'&role=0&lang=en-US&signature='+$ctrl.sign+'&china=0&apiKey=34n5fY-dQAqLjcXZjosfyw';
   };
  }

angular.module('componentApp') .component("zoomMeet", {
         templateUrl: './zoomDetail.html',
         controller: zoomDetailController,
         bindings: {
              meet: '<',
              pwd:'<',
              sign:'<',
              name:'<'
         },
         controllerAs:'$ctrl'
         }
);
})(window.angular);
