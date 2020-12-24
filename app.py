from flask import Flask
from flask_restful import Api

from main.services.get_topten import Get_TopTen

app = Flask(__name__)
api = Api(app)

api.add_resource(Get_TopTen,  	  "/Get_TopTen")

@app.route('/')
def index():
  return "This is Monthly Top Ten diagnosis API by Data Engineer Team"

if __name__=="__main__":
  app.run(host='0.0.0.0', port=int("445"), debug=True)
