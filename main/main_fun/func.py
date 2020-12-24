import psycopg2
from cryptography.fernet import Fernet

'''
def checkPostedData(postedData, functionName):
  if (functionName == "Get_TopTen"):
    if postedData is None:
      return 'Null parameter', 500 
    elif "data" not in postedData or "id" not in postedData["data"]:
      return 'Missing parameter', 500
    elif postedData["data"]["id"] is None:
      return 'Null parameter', 500 
    else:
      return 'Success', 200  
'''

def connect(params_dick):
  """ Connect to the PostgreSQL database server """
  conn = None
  try:
    conn = psycopg2.connect(**params_dick)
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    # sys.exit(1)
  return conn

def fernie(text, key):
  f = Fernet(key)
  decrypted_password = f.decrypt(text)
  return decrypted_password.decode()
