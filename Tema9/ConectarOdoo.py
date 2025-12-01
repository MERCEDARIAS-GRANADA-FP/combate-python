import xmlrpc.client

url = "http://localhost:8069"
db = "BaseDeDatos"
username = "e.ruiz@fp.mercedarias.es"
password = "alumnoalumno"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
print("UID autenticado:", uid)
