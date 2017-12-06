from flask import Flask, jsonify
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

# click count stored in redis db
@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

# return txt as json
@app.route('/w/<txt>')
def write(txt):
    res = {'txt': txt}
    return (jsonify(res))

# add new key:val to redis db
@app.route('/post/<key>/<val>')
def post(key, val):
    redis.set(key, val)
    return ('key:{}, value:{} added to db'.format(key, val))

# redis db returns val for key
@app.route('/<key>')
def get(key):
    val = redis.get(key)
    res = {key: val}
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
