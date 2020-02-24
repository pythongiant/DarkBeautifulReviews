document.onreadystatechange=function () {
 
    var one = document.getElementById("first")
    var second = document.getElementById("second")
    var third = document.getElementById("third")
    var cara = document.getElementById("cara")

    one.onclick = function(){
        cara.style.backgroundImage = "url('/static/img/1j3bmcxtjl18ihinmrhdbhg.jpg')";
    }
    second.onclick = function(){
        cara.style.backgroundImage = "url('/static/img/test2.jpeg')";
    }
    third.onclick = function(){
        cara.style.backgroundImage = "url('/static/img/test3.jpeg')";
    }   
     
}
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-500px";
  }
}