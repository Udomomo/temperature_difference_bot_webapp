from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='192.168.33.11', port=2003, debug=True)
