print("Library Management System" )
print ("Enter Your Choice:")
print("Options: ")
x=1
while(0<x):
    print("1=Add Book Details"
          "\n2=Delete Book"
          "\n3=View Book List"
          "\n4=Issue Book To Student"
          "\n5=Return Book"
          "\n6=View All Issued Books"
          "\n7=Search Book")
    x=int(input("0=Exit\n"))
    if(x==1):
        import Sub1
        Sub1.book()
    elif(x==2):
        import Sub2
        Sub2.bookdelete()
    elif(x==3):
        import Sub3
        Sub3.show()
    elif(x==4):
        import Sub4
        Sub4.issue()
    elif(x==5):
        import Sub5
        Sub5.retun()
    elif(x==6):
        import Sub6
        Sub6.view()
    elif(x==7):
        import Sub7
        Sub7.search()
    elif(x==0):
        print()
    else:
        print("Invalid Input")
