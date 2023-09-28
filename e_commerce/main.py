import sys
sys.path.append('F:/e_commerce')
from e_commerce.app import app
from e_commerce.db import db

if __name__ == '__main__':  
    app.run(debug=True)