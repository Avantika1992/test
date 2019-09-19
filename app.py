from flask import Flask,url_for,redirect,render_template,request
app = Flask(__name__)

@app.route('/health')
def health():
    return "<h1>Connection successful</h1>"


if __name__ == '__main__':
  app.run(host='0.0.0.0')
