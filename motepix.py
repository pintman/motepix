"""Ein server für motepix clients."""

import bottle
import threading
import time

on_off = [[False, False, False]]


def color_at(x, y):
    """Return the color at the given position."""
    global on_off

    if on_off[x][y]:
        return "grey"
    else:
        return "black"

def swap_all_colors():
    global on_off
    for x in range(len(on_off)):
        for y in range(len(on_off[0])):
            on_off[x][y] = not on_off[x][y]

@bottle.route("/show/<x:int>/<y:int>")
def show(x, y):
    global on_off
    return bottle.template("show", status=color_at(x, y), title=str(x)+"|"+str(y))

@bottle.route("/px/<x:int>/<y:int>")
def px_color(x, y):
    return color_at(x, y)

@bottle.route("/static/<filename>")
def serve_static(filename):
    """Serving static filed like js, css or images."""
    return bottle.static_file(filename, root="./static")

def worker():
    """Worker Thread that is changing the display data."""
    global on_off
    while True:
        swap_all_colors()
        time.sleep(2)


if __name__ == "__main__":
    # TODO Add parameter for ip

    th = threading.Thread(target=worker)
    th.start()

    bottle.run(host="192.168.178.49", port=8088, debug=True, reloader=True)
    
