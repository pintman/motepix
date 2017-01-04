<!doctype html>
<html>
  <head>
	<meta charset="utf-8">
	<title>motepix {{title}}</title>
  </head>

<body>
  <h1>Motepix</h1>

  <!-- TODO size should be changeable. -->
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
  <a href="/run_demo/0">Demo 0</a>: alle Pixel werden der Reihe nach geschaltet<br>
  <a href="/run_demo/1">Demo 1</a>: alle Pixel werden gleichzeitig
  geschaltet.<br>
  <a href="/run_demo/2">Demo 2</a>: alle Pixel anschalten <br>
  <a href="/run_demo/3">Demo 3</a>: alle Pixel ausschalten <br>
  <p>
	<a href="/preview">Vorschau</a>
  </p>
</body>

</html>
