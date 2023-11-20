from flask import Flask, render_template, request
from interestin import *
from sale_repository import *
from sale_service import *

cast()

app = Flask(__name__, static_folder='web/static', template_folder='web/templates', static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/sale', methods=['POST'])
def create_sale():
    json = request.json
    addSale(json)



if __name__ == '__main__':
    app.run(threaded=True, port=5000)