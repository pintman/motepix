<!doctype html>
<html>
  <head>
	<meta charset="utf-8">
	<title>motepix {{title}}</title>
  </head>

<body>
  <h1>Motepix</h1>

  <!-- 
  TODO size should be changeable. 
  TODO change to bootstrap for nicer look on mobile devices?
  -->
  <table border='1'>
	% for h in range(height):
	<tr>
	  % for w in range(width):
	  <td><a id="px{{w}}{{h}}" href="/show/{{w}}/{{h}}"> O </a></td>
	  % end
	</tr>
	% end
  </table>

  <h1>Demos</h1>
  <a href="/run_demo/pixel_row">Pixel Row</a>: alle Pixel werden der Reihe nach geschaltet<br>
  <a href="/run_demo/blink">Blink</a>: alle Pixel blinken.<br>
  <a href="/run_demo/blink_fast">Bink Fast</a>: alle Pixel blinken schnell.<br>
  <a href="/run_demo/all_on">All On</a>: alle Pixel anschalten <br>
  <a href="/run_demo/all_off">All Off</a>: alle Pixel ausschalten <br>
  <p>
	<a href="/preview">Vorschau</a>
  </p>
</body>

</html>
