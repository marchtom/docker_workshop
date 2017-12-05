from flask import Flask, jsonify

app = Flask(__name__)

# app can't use default 127.0.0.1 host
# must be changed

@app.route('/')
def result():
  res = {'a': 1, 'b': 'b'}
  return jsonify(res)
  
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
  
