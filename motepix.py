"""Ein server für motepix clients."""

import bottle
import threading
import time
import json


class MotepixServer:
    """A server to serve single pixels to a bunch of smartphones or similar devices."""

    # TODO add support to let others control the pixel array.

    def __init__(self, width=3, height=2):
        self.on_off = [[False for w in range(height)] for h in range(width)]
        # A demo that is running
        self.demo_programm = 0

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

    def width(self):
        return len(self.on_off)

    def height(self):
        return len(self.on_off[0])

    def route_run_demo(self, num):
        self.demo_programm = num
        bottle.redirect("/")

    def route_index(self):
        return bottle.template("index", title="Konfig", width=self.width(), height=self.height())
 
    def route_show(self, x, y):
        return bottle.template("show", status=self.color_at(x, y), title=str(x)+"|"+str(y))

    def route_px(self, x, y):
        return self.color_at(x, y)

    def route_pixels(self):
        return json.dumps(self.on_off)

    def route_preview(self):
        return bottle.template("preview")

    def route_serve_static(self, filename):
        """Serving static filed like js, css or images."""
        return bottle.static_file(filename, root="./static")

    def worker(self):
        """Worker Thread that is changing the display data."""

        while True:
            if self.demo_programm == 0:
                for y in range(self.height()):
                    for x in range(self.width()):
                        self.on_off[x][y] = True
                        time.sleep(0.5)
                        self.on_off[x][y] = False

            elif self.demo_programm == 1:
                self.swap_all_colors()
                time.sleep(1)
           

def main():

    ms = MotepixServer()
    
    bottle.route("/show/<x:int>/<y:int>")(ms.route_show)
    bottle.route("/px/<x:int>/<y:int>")(ms.route_px)
    bottle.route("/run_demo/<num:int>")(ms.route_run_demo)
    bottle.route("/static/<filename>")(ms.route_serve_static)
    bottle.route("/preview")(ms.route_preview)
    bottle.route("/pixels")(ms.route_pixels)
    bottle.route("/")(ms.route_index)

    th = threading.Thread(target=ms.worker)
    th.start()
    
    bottle.run(host="0.0.0.0", port=8088, debug=True, reloader=True)
    #bottle.run(host="0.0.0.0", port=8088)

if __name__ == "__main__":
    main()
