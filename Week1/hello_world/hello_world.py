import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','banana','peach']
    return bottle.template('hello_world', username='Todd',things=mythings)

bottle.debug(True)
bottle.run(host='localhost', port=8082)
