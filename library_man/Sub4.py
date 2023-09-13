def issue():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
        Student_Name = input("Enter Student Name")
        Date_Of_Issuing = input("Enter Date Of Issuing(yyyy/mm/dd)")
        Id= input("Enter Book Id")
        Date_Of_Returning = input("Enter Date  of Returb(yyyy/mm/dd)")
        sql = "insert into Book_Issuing (Student_Name,Date_Of_Issuing,Id,Date_Of_Returning)values(%s,%s,%s,%s)"
        val = (Student_Name,Date_Of_Issuing,Id,Date_Of_Issuing)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        print("Issue Successfully")
'''
crate table Book_Issuing
(Student_Name Varchar(100),
Date_Of_Issuing Date,
Id Int(10)
Date_Of_Returning Date);
'''
