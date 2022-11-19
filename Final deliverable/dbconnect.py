import ibm_db
hostname="2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="pyd03172"
password="yVoUxh8d5GJAup2S"
driver="(IBM DB2 ODBC DRIVER)"
db="bludb"
port="32328"
protocol="TCPIP"
cert="DigiCertGlobalRootCA"
dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};").format(db,hostname,port,uid,cert,password)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("conneccted to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())
    