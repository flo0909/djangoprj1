/* Code for changing innerText learned from  https://www.w3schools.com/jsref/event_onmouseover.asp*/

var1 = document.getElementById("landing-card-button-01").onmouseover = function() {overFunc1()};
var2 = document.getElementById("landing-card-button-01").onmouseout = function() {outFunc1()};

var3 = document.getElementById("landing-card-button-02").onmouseover = function() {overFunc2()};
var4 = document.getElementById("landing-card-button-02").onmouseout = function() {outFunc2()};

function overFunc1() {
  document.getElementById("landing-card-button-01").innerText="Fix a bug for free!";
}
function outFunc1() {
    document.getElementById("landing-card-button-01").innerText="Go to Requests";
  }

function overFunc2() {
    document.getElementById("landing-card-button-02").innerText="Ask for a Feature";
}
function outFunc2() {
    document.getElementById("landing-card-button-02").innerText="Go to Features";
}
/* Code for hiding the messages */

var5 = document.getElementById("message-container")

function hideMessage(){
    var time01 = setTimeout(function(){var5.style.display = 'none';time01.clearTimeout}, 2000)
}
hideMessage()