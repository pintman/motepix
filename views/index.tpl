<!doctype html>
<html>
  <head>
	<meta charset="utf-8">
	<title>motepix {{title}}</title>
  </head>

<body>
  <h1>Motepix</h1>

  <table border='1'>
	% for h in range(height):
	<tr>
	  % for w in range(width):
	  <td><a href="/show/{{w}}/{{h}}"> O </a></td>
	  % end
	</tr>
	% end
  </table>

  <h1>Demos</h1>
  <a href="/run_demo/0">Demo 0</a>: alle Pixel werden der Reihe nach geschaltet<br>
  <a href="/run_demo/1">Demo 1</a>: alle Pixel werden gleichzeitig geschaltet.

</body>

</html>
