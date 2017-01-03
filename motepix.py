"""Ein server für motepix clients."""

import bottle

on_off = True


@bottle.route("/register")
def register():
    """Register a new client."""
    # import pdb; pdb.set_trace()
    print(bottle.request)

@bottle.route("/show")
def show():
    global on_off
    on_off = not on_off
    print("show")
    return bottle.template("index", status=on_off, title=on_off)

@bottle.route("/pixel_color")
def pixel_color():
    global on_off
    if on_off:
        on_off = not on_off
        return "grey"
    else:
        on_off = not on_off
        return "black"

@bottle.route("/static/<filename>")
def serve_static(filename):
    return bottle.static_file(filename, root="./static")


if __name__ == "__main__":
    bottle.run(host="localhost", port=8088, debug=True, reloader=True)
    
