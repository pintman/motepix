
$(document).ready(
	function() {
		// console.log("document ready");
		ask_for_data();
	}
);

function ask_for_data()
{
	//console.log("ask for data");
	console.log(window.location.href);
	// in 'http://192.168.178.49:8088/show/0/0' fetch part after show
	// and split the coordinates afterwards
	var x_y = window.location.href.split("/show/")[1].split("/");
	var x = x_y[0];
	var y = x_y[1];
	//console.log(x_y + " " + x + "|" + y);
	$.get("/px/"+x+"/"+y, data_received);
}

function data_received(response)
{
	// console.log("data_received:" + response);
	$("#pixel").attr("style", "position:absolute;top:0px;bottom:0px;width:99%;background-color:" + response);
	// wait for some ms and ask for data again
	window.setTimeout(ask_for_data, 1000);
}
