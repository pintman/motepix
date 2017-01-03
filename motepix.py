"""Ein server für motepix clients."""

import bottle

on_off = [[False, False, False]]

def color_at(x, y):
    """Return the color at the given position."""

    if on_off[x][y]:
        return "grey"
    else:
        return "black"

@bottle.route("/show/<x:int>/<y:int>")
def show(x, y):
    global on_off
    on_off[x][y] = not on_off[x][y]
    return bottle.template("show", status=on_off[x][y], title=str(x)+"|"+str(y))


@bottle.route("/px/<x:int>/<y:int>")
def px_color(x, y):
    print(x, y)
    global on_off
    on_off[x][y] = not on_off[x][y]
    return color_at(x, y)

@bottle.route("/static/<filename>")
def serve_static(filename):
    """Serving static filed like js, css or images."""
    return bottle.static_file(filename, root="./static")


if __name__ == "__main__":
    bottle.run(host="localhost", port=8088, debug=True, reloader=True)
    
