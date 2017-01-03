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
	  <td><a href="/show/{{w}}/{{h}}">({{w}} {{h}})</a></td>
	  % end
	</tr>
	% end
  </table>

</body>

</html>
