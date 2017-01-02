function index_loaded()
{
	alert("index_loaded");
}

$(document).ready(
	function() {
		$("#status").addClass("test");
		$("a").click(
			function()
			{
				//alert("so");
				//$.get("index.htm", index_loaded);
				$("#status").text("Neuer Status");
			});
	}
);

