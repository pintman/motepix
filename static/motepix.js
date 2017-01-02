
$(document).ready(
	function() {
		console.log("document ready");
		$.get("http://localhost:8088/show", data_received);
		
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
	console.log("data_received");
	$("#status").text("Daten empfangen");
}
