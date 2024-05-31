


var ip = location.hostname
alert(ip);

//var connection = new WebSocket('ws://10.190.25.29:8889/ws/display');
var connection = new WebSocket('ws://' + ip +  ':8889/ws/display');
connection.onmessage = function (e) {
    document.getElementById("display1").textContent = JSON.parse(e.data)["data1"];
    document.getElementById("display2").textContent = JSON.parse(e.data)["data2"];
};

