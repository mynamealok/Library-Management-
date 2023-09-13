def retun():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
        Student_Name = input("Enter Student Name")
        Id= int(input("Enter Book Id"))
        sql = "delete from Book_Issuing where Student_Name=%s and ID=%s "
        val = (Student_Name,Id)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        print("Return Sucessfull")
