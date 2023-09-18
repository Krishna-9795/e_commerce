import sys
sys.path.append('F:/e_commerce')
from e_comm.app import app,db



if __name__ == '__main__':
    app.run(debug=True)
    
