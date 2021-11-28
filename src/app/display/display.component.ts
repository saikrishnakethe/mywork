import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrls: ['./display.component.css']
})
export class DisplayComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
var app = angular.module('demo', []);
var controllers = {};
var alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
var countriesNotSorted = [],
    countriesArray = countriesNotSorted.sort();



app.directive('searchList', function() {
    return {
        scope: {
            searchModel: '=model'
        },
        link: function(scope, element, attrs) {
            element.on('click', attrs.searchList, function() {
                scope.searchModel = $(this).text();
                scope.$apply();
            });
        }
    };
});

controllers.MainController = function($scope) {
    $scope.setTerm = function(letter) {
        $scope.search = letter;
    };
    $scope.alphabet = {
      letter: alphabet
    }
  
  $scope.countries = {
    country: countriesArray
  }
  $scope.startsWith = function (actual, expected) {
    var lowerStr = (actual + "").toLowerCase();
    return lowerStr.indexOf(expected.toLowerCase()) === 0;
  }
};



app.controller(controllers);


}
