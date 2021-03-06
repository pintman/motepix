"""Ein server für motepix clients."""

import bottle
import threading
import time
import json


class PixelServer:
    """A server to serve single pixels to a bunch of smartphones or similar 
    devices."""

    def __init__(self, width=3, height=2):
        self.on_off = [[False for w in range(height)] for h in range(width)]
        # A demo that is running
        self.demo_programm = "pixel_row"

    def start(self):
        th = threading.Thread(target=self.worker)
        th.start()
        
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

    def all_pixels(self, on_off):
        for y in range(self.height()):
            for x in range(self.width()):
                self.on_off[x][y] = on_off

    def width(self):
        return len(self.on_off)

    def height(self):
        return len(self.on_off[0])

    def route_dimensions(self):
        return str(self.width()) + "x" + str(self.height())
    
    def route_run_demo(self, demo_name):
        self.demo_programm = demo_name
        bottle.redirect("/")

    def route_index(self):
        return bottle.template("index", title="Konfig", width=self.width(),
                               height=self.height())
 
    def route_show(self, x, y):
        return bottle.template("show", status=self.color_at(x, y),
                               title=str(x)+"|"+str(y))

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
            if self.demo_programm == "pixel_row":
                for y in range(self.height()):
                    for x in range(self.width()):
                        self.on_off[x][y] = True
                        time.sleep(0.5)
                        self.on_off[x][y] = False

            elif self.demo_programm == "blink":
                self.swap_all_colors()
                time.sleep(1)
            
            elif self.demo_programm == "blink_fast":
                self.swap_all_colors()
                time.sleep(0.2)

            elif self.demo_programm == "all_on":
                self.all_pixels(True)
                
            elif self.demo_programm == "all_off":
                self.all_pixels(False)


def main():

    ps = PixelServer()
    ps.start()
    
    bottle.route("/show/<x:int>/<y:int>")(ps.route_show)
    bottle.route("/data/px/<x:int>/<y:int>")(ps.route_px)
    bottle.route("/data/pixels")(ps.route_pixels)
    bottle.route("/data/dimensions")(ps.route_dimensions)
    bottle.route("/run_demo/<demo_name>")(ps.route_run_demo)
    bottle.route("/static/<filename>")(ps.route_serve_static)
    bottle.route("/preview")(ps.route_preview)
    bottle.route("/")(ps.route_index)

    bottle.run(host="0.0.0.0", port=8088, debug=True, reloader=True)
    # bottle.run(host="0.0.0.0", port=8088)

if __name__ == "__main__":
    main()
