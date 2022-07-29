import mysql.connector as a
con=a.connect(host='localhost',user='root',passwd="Govind2131",database='librarydb')
def AddBook():
    bn=input("Book Name:")
    bc=input("Book Code:")
    t=input("Total Books:")
    sub=input("Subject:")
    data=(bn,bc,t,sub)
    sql='insert into book values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("--------------------------------------------------------------------------------")
    print("data is succesfully entered")
    main()

    
def Issuebook():
    n=input("Name:")
    rno=input("Registration Number:")
    co=input("Book Code:")
    d=input("Date:")
    data=(bn,bc,t,sub)
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,rno,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("--------------------------------------------------------------------------------")
    print("books issued to:",n)
    bookup(co,-1)


    
def SubmitBook():
    n=input("Name:")
    rno=input("Registration Number:")
    co=input("Book Code:")
    d=input("Date:")
    data=(bn,bc,t,sub)
    a="insert into submit values(%s,%s,%s,%s)"
    data=(n,rno,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("--------------------------------------------------------------------------------")
    print("books submitted from:",n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL =%s where BCODE=%s"
    d=(t,co)
    co.execute(sql,d)
    con.commit()
    main()

def DeleteBook():
    ac=input("Enter Book Code :")
    a="delete from books where BCODE=%s"
    data=(ac,)
    co=con.cursor()
    co.execute(a,data)
    con.commit()
    main()

def DisplayBook():
    a="select * from books"
    co=con.cursor()
    co.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name :",i[0])
        print("Book Code :",i[1])
        print("Total:",i[2])
        print("--------------------------------------------------------------------------------")
        main()

        
    
    
def main():
    print("""
                                                    LIBRARY MANAGER
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOK
    """)
    choice =input("Choose the task no:")
    print("..............................................................................................................")
    if(choice=="1"):
        AddBook()
    elif(choice=="2"):
        Issuebook()
    elif(choice=="3"):
        SubmitBook()
    elif(choice=="4"):
        DeleteBook()
    elif(choice=="5"):
        DisplayBook()
    else:
        print("Wrong Choice")
        main()

def pword():
    ps=input("Enter Password:")
    if ps == "lm123":
        main()
    else:
        print("Wrong Password")
        pword()
pword()

    
