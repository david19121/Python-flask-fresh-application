from flask import Flask,render_template
import socket
app = Flask(__name__)


def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)


@app.route("/")
def index():
    return "welcome to my python flask fresh application"





if __name__=='__main__':
    app.run(host="127.0.0.1",port=5004)