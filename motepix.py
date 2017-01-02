"""Ein server für motepix clients."""

import bottle

@bottle.route("/register")
def register():
    """Register a new client."""
    # import pdb; pdb.set_trace()
    print(bottle.request)

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)
    
