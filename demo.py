from flask import Flask
from visa.logger import logging


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("We are just testing logging module let see.....")
    return "this is my first ML end to end project"

if __name__=="__main__":
    app.run(debug = True)