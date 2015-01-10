import bottle

@bottle.route('/')
def home_page():
    return "<html><title></title><body>Hello World\n</body></html>\n"

@bottle.route('/testpage')
def test_page():
    return "<html><title></title><body>This is a test page\n</body></html>\n"

bottle.debug(True)
bottle.run(host='localhost', port=8082)
