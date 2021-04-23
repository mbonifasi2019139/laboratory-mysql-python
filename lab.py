# Realizar un programa en Python que permita poder realizar conexiones a base de datos en MySql utilizar
# MYSQL Connector (python -m pip install mysql-connector-python) e importar el conector (import
# mysql.connector)
# 1. Crear conexión para la base de datos ( utilizar host , user , password , nombre base de datos)
# 2. Crear base de datos
# 3. Crear un cursor para poder manejar las conexiones
# 4. Crear una tabla que permita la inserción de los datos contenidos en este documento
# 5. Insertar los datos
# 6. Mostrar todos los datos insertados desde Python

# Estudiante:
#     Marcos Daniel Bonifasi de Leon
# Curso:
#     Python Intermedio J - SaeSap

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    #database="dbpython"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database dbpython")

# mycursor.execute("create table user( user_id varchar(255), username varchar(255), name varchar(255), letter char(1), num char(1), email varchar(255), phone varchar(255), phoneBrand varchar(255), company varchar(255), price varchar(255), amount char(1))")

# sql = "insert into user values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# val = [
#     ("1", "BRE2271","BRENDA" ,"M", "2", "brenda@live.com", "655-143-5736", "SAMSUNG", "UISACELL", "100", "1"),
#     ("2","OSC4677","OSCAR","H","3","oscar@gmail.com","655-143-4181","LG","TELCEL","0","1"),
#     ("3","JOS7086","JOSE","H","3","francisco@gmail.com","655-143-3922","NOKIA","MOVISTAR","150","1"),
#     ("4","LUI6115","LUIS","H","0","enrique@outlook.com","655-137-1279","SAMSUNG","TELCEL","50","1"),
#     ("5","LUI7072","LUIS","H","1","luis@hotmail.com","655-100-8260","NOKIA","IUSACELL","50","0"),
#     ("6","DAN2832","DANIEL","H","0","daniel@outlook.com","655-145-2586","SONY","UNEFON","100","1"),
#     ("7","JAQ5351","JAQUELINE","M","0","jaqueline@outlook.com","655-330-5514","BLACKBERRY","AXEL","0","1"),
#     ("8","ROM6520","ROMAN","H","2","roman@gmail.com","655-330-3263","LG","IUSACELL","50","1"),
#     ("9","BLA9739","BLAS","H","0","blas@hotmail.com","655-330-3871","LG","UNEFON","100","1"),
#     ("10","JES4752","JESSICA","M","1","jessica@hotmail.com","655-143-6861","SAMSUNG","TELCEL","500","1"),
#     ("11","DIA6570","DIANA","M","1","diana@live.com","655-143-3952","SONY","UNEFON","100","0"),
#     ("12","RIC8283","RICARDO","H","2","ricardo@hotmail.com","655-145-6049","MOTOROLA","IUSACELL","150","1"),
#     ("13","VAL6882","VALENTINA","M","0","valentina@live.com","655-137-4253","BLACKBERRY","AT&T","50","0"),
#     ("14","BRE8106","BRENDA","M","3","brenda2@gmail.com","655-100-1351","MOTOROLA","NEXTEL","150","1"),
#     ("15","LUC4982","LUCIA","M","3","lucia@gmail.com","655-145-4992","BLACKBERRY","IUSACELL","0","1"),
#     ("16","JUA2337","JUAN","H","0","juan@outlook.com","655-100-6517","SAMSUNG","AXEL","0","0"),
#     ("17","ELP2984","ELPIDIO","H","1","elpidio@outlook.com","655-145-9938","MOTOROLA","MOVISTAR","500","1"),
#     ("18","JES9640","JESSICA","M","3","jessica2@live.com","655-330-5143","SONY","IUSACELL","200","1"),
#     ("19","LET4015","LETICIA","M","2","leticia@yahoo.com","655-143-4019","BLACKBERRY","UNEFON","100","1"),
#     ("20","LUI1076","LUIS","H","3","luis2@live.com","655-100-5085","SONY","UNEFON","150","1")
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "Usuarios insertados")

# mycursor.execute("select * from user")
# myquery = mycursor.fetchall()

# for user in myquery:
#     print(user)
