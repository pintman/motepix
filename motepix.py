"""Ein server für motepix clients."""

import bottle
import threading
import time


class MotepixServer:
    """A server to serve single pixels to a bunch of smartphones or similar devices."""

    def __init__(self, width=4, height=3):
        self.on_off = [[False for w in range(width)] for h in range(height)]

    def color_at(self, x, y):
        """Return the color at the given position."""

        if self.on_off[x][y]:
            return "grey"
        else:
            return "black"

    def swap_all_colors(self):
        for x in range(len(self.on_off)):
            for y in range(len(self.on_off[0])):
                self.on_off[x][y] = not self.on_off[x][y]

    def route_index(self):
        return bottle.template("index", title="Index")
 
    def route_show(self, x, y):
        return bottle.template("show", status=self.color_at(x, y), title=str(x)+"|"+str(y))

    def route_px_color(self, x, y):
        return self.color_at(x, y)

    def route_serve_static(self, filename):
        """Serving static filed like js, css or images."""
        return bottle.static_file(filename, root="./static")

    def worker(self):
        """Worker Thread that is changing the display data."""

        while True:
            # self.swap_all_colors()
            for x in range(len(self.on_off)):
                for y in range(len(self.on_off[0])):
                    self.on_off[x][y] = True
                    time.sleep(0.5)
                    self.on_off[x][y] = False


def main():

    ms = MotepixServer()
    
    bottle.route("/show/<x:int>/<y:int>")(ms.route_show)
    bottle.route("/px/<x:int>/<y:int>")(ms.route_px_color)
    bottle.route("/static/<filename>")(ms.route_serve_static)
    bottle.route("/")(ms.route_index)

    th = threading.Thread(target=ms.worker)
    th.start()
    
    bottle.run(host="0.0.0.0", port=8088, debug=True, reloader=True)
    

if __name__ == "__main__":
    main()
