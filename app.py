from flask import Flask, request, render_template
from utils.config import *
from utils.boot import *

app = Flask(__name__)

@app.before_first_request
def before_start():
    app.logger.info("booting application..")
    app.logger.info("boot completed..")

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/list')
def list():
    rows=Ip.select()
    return render_template('ip_list.html', ip_list=rows)

@app.route('/')
def none():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    record=Ip(ip_address=ip)
    record.save()
    return render_template('index.html', ip_address=ip)

@app.route('/add/<ip>')
def add(ip):
    record=Ip(ip_address=ip)
    record.save()
    return render_template('index.html', ip_address=ip)

if __name__ == '__main__':
   app.run(host=FLASK_HOST, port=FLASK_PORT, debug="on")
