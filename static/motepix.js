
$(document).ready(
	function() {
		console.log("document ready");
		$.get("/my_data", data_received);
		
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

function data_received(response)
{
	console.log("data_received:" + response);
	$("#pixel").attr("style", "width:100px;height:100px;background-color:black");
	//$("#status").text("Daten empfangen");
	//$.get("/my_data", data_received)
}
