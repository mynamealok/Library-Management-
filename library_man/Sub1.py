def book():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="alok", database="alok")
    Id = input("Enter Book Id:")
    Name = input("Enter Name Of Author:")
    Sub = input("Enter Subject:")
    Class = input("Enter Class:")
    sql = "insert into Books (Id,Name,Sub,Class)values(%s,%s,%s,%s)"
    val = (Id,Name,Sub,Class)
    mycursor = mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()
    print("Update Successfully")
'''
create database wps;
create table Books
(Id int(10),
Name Varchar(100),
Sub Varchar(25),
Class Varchar(5));
'''
