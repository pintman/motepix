
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
	// TODO get coordinates from location url
	var x = 0
	var y = 0
	$.get("/px/"+x+"/"+y, data_received);
}

function data_received(response)
{
	// console.log("data_received:" + response);
	$("#pixel").attr("style", "width:100px;height:100px;background-color:" + response);
	// wait for some ms and ask for data again
	window.setTimeout(ask_for_data, 1000);
}
