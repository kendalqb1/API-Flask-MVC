from flask import Flask

app = Flask(__name__)
from views.taskView import *

def main():
    app.run(debug = True, port = 4000)

if __name__ == '__main__':
    main()

