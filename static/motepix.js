
function ask_for_data()
{
	// in 'http://192.168.178.49:8088/show/0/0' fetch part after show
	// and split the coordinates afterwards
	var x_y = window.location.href.split("/show/")[1].split("/");
	var x = x_y[0];
	var y = x_y[1];
	// fetch pixel data async.
	$.get("/data/px/"+x+"/"+y, data_received);
}

function data_received(response)
{
	// console.log("data_received:" + response);
	// TODO move styles to css
	var style = "position:absolute;top:0px;bottom:0px;width:99%";
	$("#pixel").attr("style", style + ";background-color:" + response);
	// wait for some ms and ask for data again
	window.setTimeout(ask_for_data, 10);
}

function ask_for_all_data()
{
	$.get("/data/pixels", all_data_received);
}

function all_data_received(pixel_array)
{
	// Convert json string into pixel 2dim-array
	pixels = jQuery.parseJSON(pixel_array)
	
	// create the table statement
	var table = "<table border=1>";
	for(var x=0; x<pixels[0].length; x++)
	{
		table += "<tr>";
		for(var y=0; y<pixels.length; y++)
		{
			if(pixels[y][x])
			{
				var color = "gray"
			}
			else
			{
				var color = "black";
			}
			// TODO move styles to css
			table += "<td bgcolor='"+ color + "'>O</td>";
		}
		table += "</tr>";
	}

	// clean the div container and insert the new table array
	$("#preview").empty()
	$("#preview").append(table);

	// wait some time and do it again
	window.setTimeout(ask_for_all_data, 10);
}
