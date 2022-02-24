from mysite import app,socketio
import os
if __name__ == '__main__':
   
    app.run(host="0.0.0.0",debug=True,port=os.environ['PORT'])