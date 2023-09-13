def bookdelete():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
        Id = input("Enter Book Id")
        Name = input("Enter Name Of Author")
        sql= "delete from Books where Id=%s and Name=%s";
        val = (Id,Name)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        print("Delete Successfully")    
