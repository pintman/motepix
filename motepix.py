"""Ein server für motepix clients."""

import bottle


@bottle.route("/register")
def register():
    """Register a new client."""
    # import pdb; pdb.set_trace()
    print(bottle.request)


@bottle.route("/show")
def show():
    return bottle.template("index")


if __name__ == "__main__":
    bottle.run(host="localhost", port=8088, debug=True, reloader=True)
    
