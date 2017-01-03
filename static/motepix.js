
$(document).ready(
	function() {
		// console.log("document ready");
		ask_for_data();
		//$.get("/pixel_color", data_received);
		
		/*
		$("a").click(
			function()
			{
				//alert("so");
				//$.get("index.htm", index_loaded);
				$("#status").text("Neuer Status");
			});
		*/
	}
);

function ask_for_data()
{
	//console.log("ask for data");
	$.get("/pixel_color", data_received);
}

function data_received(response)
{
	// console.log("data_received:" + response);
	$("#pixel").attr("style", "width:100px;height:100px;background-color:" + response);
	window.setTimeout(ask_for_data, 100);
}
