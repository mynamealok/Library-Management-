def search():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
        Id = int(input("Enter Book Id"))
        flg=False
        mycursor = mydb.cursor()
        sql="select*from Books where Id=%s"
        val=(Id,)
        mycursor.execute(sql,val)
        result=mycursor.fetchall()
        for i in result: 
               print(i,end=" ")
               flg=True
        print()
        if flg==False:
                print("Record Not Found")
