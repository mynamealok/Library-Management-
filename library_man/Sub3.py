def show():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
        mycursor = mydb.cursor()
        mycursor.execute("select * from Books")
        for i in mycursor:
            print(i)
