# customException class
# logging class

from visa.exception import CustomException
from visa.logger import logging
from flask import Flask
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception('testing the custom exception so that i am writing here')
    
        
    
    except Exception as e:
        visa=CustomException(e,sys)
        logging.info(visa.error_message)
        logging.info("we are testing logging  file let see it is correct or no.....")
  

if __name__=="__main__":
    app.run(debug = True)


