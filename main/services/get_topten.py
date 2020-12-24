from flask_restful import Resource
from flask import jsonify, request 
import psycopg2

from ..config.credentials import DB_CONN
from ..main_fun.func import connect

class Get_TopTen(Resource):
  def get(self):
    connection   = DB_CONN["conn"] [0]
    command      = f"""select v1."rank", v1.diagnosis_name from vw_topten_dx v1 where v1.processed_date = (select max(v2.processed_date) from vw_topten_dx v2)"""
    try:
      conn = connect(connection)
      cur = conn.cursor()
      cur.execute( command )
      result = cur.fetchall()
      cur.close()
      conn.close()        
      retJson = \
        {
          "data": 
            {
              "status":200,
              "message": result
            }
        }
      return jsonify(retJson)   
    except (Exception, psycopg2.DatabaseError) as error:
      retJson = \
        {
          "data": 
            {
              "status":501,
              "message": f"{error}"
            }
        }
      return jsonify(retJson)