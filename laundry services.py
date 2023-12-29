'''Laundry Services Project'''

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="admin")
mycursor=mydb.cursor()
##mycursor.execute("CREATE DATABASE LAUNDRY")
mycursor.execute("USE LAUNDRY")
print("******************WELCOME TO LAUNDRY AND WARDROBE SERVICES******************************")
print('\n')

##string1="CREATE TABLE DRYCLEANING(SNO int(3) Primary key ,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3),ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##mycursor.execute(string1)
##
##string2="CREATE TABLE IRONING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##mycursor.execute(string2)
##
##string3="CREATE TABLE DYEING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3),ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##mycursor.execute(string3)
##
##string4="CREATE TABLE DARNING(SNO int(3) Primary key ,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3),ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##mycursor.execute(string4)
##
##string5="CREATE TABLE WARDROBESERVICES(SNO int(3) Primary key ,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3),ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##mycursor.execute(string5)
##
##def check1():
##    mycursor.execute("SHOW DATABASES")
##    found=0
##    for i in mycursor:
##        if i==('LAUNDRY',):
##            found=1
##    if found==0:
##        mycursor.execute("CREATE DATABASE LAUNDRY")
##    mycursor.execute("USE LAUNDRY")
##    mycursor.execute("SHOW TABLES")
##    found=0
##    for i in mycursor:
##        if i==('DRYCLEANING',):
##            found=1
##    if found==0:
##        string1="CREATE TABLE DRYCLEANING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##        mycursor.execute(string1)
##
##def check2():
##    mycursor.execute("SHOW DATABASES")
##    found=0
##    for i in mycursor:
##        if i==('LAUNDRY',):
##            found=1
##    if found==0:
##        mycursor.execute("CREATE DATABASE LAUNDRY")
##    mycursor.execute("USE LAUNDRY")
##    mycursor.execute("SHOW TABLES")
##    found=0
##    for i in mycursor:
##        if i==('IRONING',):
##            found=1
##    if found==0:
##        string2="CREATE TABLE IRONING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##        mycursor.execute(string2)
##
##def check3():
##    mycursor.execute("SHOW DATABASES")
##    found=0
##    for i in mycursor:
##        if i==('LAUNDRY',):
##            found=1
##    if found==0:
##         mycursor.execute("CREATE DATABASE LAUNDRY")
##    mycursor.execute("USE LAUNDRY")
##    mycursor.execute("SHOW TABLES")
##    found=0
##    for i in mycursor:
##        if i==('DYEING',):
##            found=1
##    if found==0:
##        string3="CREATE TABLE DYEING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##        mycursor.execute(string3)
##
##def check4():
##    mycursor.execute("SHOW DATABASES")
##    found=0
##    for i in mycursor:
##        if i==('LAUNDRY',):
##            found=1
##    if found==0:
##         mycursor.execute("CREATE DATABASE LAUNDRY")
##    mycursor.execute("USE LAUNDRY")
##    mycursor.execute("SHOW TABLES")
##    found=0
##    for i in mycursor:
##        if i==('DARNING',):
##            found=1
##    if found==0:
##        string4="CREATE TABLE DARNING(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENTS VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##        mycursor.execute(string4)
##
##def check5():
##    mycursor.execute("SHOW DATABASES")
##    found=0
##    for i in mycursor:
##        if i==('LAUNDRY',):
##            found=1
##    if found==0:
##         mycursor.execute("CREATE DATABASE LAUNDRY")
##    mycursor.execute("USE LAUNDRY")
##    mycursor.execute("SHOW TABLES")
##    found=0
##    for i in mycursor:
##        if i==('WARDROBESERVICES',):
##            found=1
##    if found==0:
##        string5="CREATE TABLE WARDROBE SERVICES(SNO int(3) Primary key,NAME VARCHAR(20),\
##DATE DATE, CONTENT VARCHAR(25), QUANTITY INT(3), ECODE INT(4),DATEOFRETURN DATE,PHONE NUMERIC(10))"
##        mycursor.execute(string5)

def insertion():
    print("Following are the different services:-")
    print("1. DRY CLEANING")
    print("2. IRONING")
    print("3. DYEING")
    print("4. DARNING")
    print("5. WARDROBE SERVICES")
    print("6. EXIT")
    table=''
    t=int(input("Enter the service you want to proceed with(1-6)="))
    if t==1:
        table='drycleaning'
    elif t==2:
        table='ironing'
    elif t==3:
        table='dyeing'
    elif t==4:
        table='darning'
    elif t==5:
        table='wardrobeservices'
    elif t==6:
        print("Proceeding to the main menu")
        return
    mycursor.execute("SELECT * FROM {}".format(table))
    items={'saree':250,'blazer':300,'shawl':150,'blanket':350,'quilt':400,
           'dress':400,'jeans':150,'suit':200,'curtain':100,'covers':400,
           'shirt':100,'jacket':150}
    for i in mycursor:
        print(i)

    print('\n')    
    sno=int(input("Enter Sno:-"))
    nm=input("Enter Name:-")
    dt=str(input("Enter Date(yyyy-mm-dd):-"))
    contents=''
    while True:
        ct=input("Enter Contents:-")
        contents+=(str(ct)+' ')
        print(contents)
        ans=input("Are there more items to give for service(y/n)=")
        if ans in 'yY':
            continue
        elif ans in 'nN':
            break
        
    for x in (contents.split()):
        qnt=int(input("Enter Quantity for {}:-".format(x)))
    for x in (contents.split()):
        if x.lower() in items:
            pc=items[x.lower()]
        else:
            pc=int(input("Enter Price of {}:-".format(x)))    
    ##ec=int(input("Enter Ecode:-"))
    global ecode
    ec=int(input("Enter the last ecode alotted="))
    ec+=1
    tt=qnt*pc
    dor=str(input("Enter Date of Return:-"))
    ph=int(input("Enter Phone no:-"))
    for x in (contents.split()):
        mycursor.execute("INSERT INTO {} VALUES({},'{}','{}','{}',{},{},'{}',{})".format(table,sno,nm,dt,x,qnt,ec,dor,ph))
        sno+=1
        mydb.commit()
    print("Record given by you is inserted....")
    fr=input("Is the phone number inserted for the insertion correct=")
    if fr in 'yY':
         print("Ok")
    else:
        update()
    mycursor.execute("SELECT * FROM {}".format(table))
    for i in mycursor:
        print(i)

    
    print('\n')
    print("-------SLIP GENERATION---------")
    print(tt)
    print("Your invoice no=",ec)
    print("Date of return:",dor)
    print("Collect your belongings on",dor,".Have a nice day ahead.")
    print('\n')
    
    ans=input("Is there anything to be given for other services(y/n):")
    if ans in 'yY':
        insertion()
    elif ans in 'nN':
        print("-------------------------------------Thanks.Have a nice day ahead.-----------------------------------------------")



def name():
    print("*********************************")
    print("Following are the different services:-")
    print("1. DRY CLEANING")
    print("2. IRONING")
    print("3. DYEING")
    print("4. DARNING")
    print("5. WARDROBE SERVICES")
    ch=int(input("Enter the service chosen(1-5)?"))
    if ch==1:
        print("DRY CLEANING")
        
    elif ch==2:
        print("IRONING")
        
    elif ch==3:
        print("DYEING")
       
    elif ch==4:
        print("DARNING")
        
    elif ch==5:
        print("WARDROBE SERVICES")
        
    c=input("Did you choose other services also(Y/N)=")
    if c.upper()=='Y':
        name()
    elif c.upper()=="N":
        print("Thanks...........")            



def pricing():
    items={'saree':250,'blazer':300,'shawl':150,'blanket':350,'quilt':400,
           'dress':400,'jeans':150,'suit':200,'curtain':100,'covers':50,
           'shirt':100,'jacket':150}
    custname=input("Enter your name=")
    print("Welcome to our store",custname)
    cost=[]
    while True:        
        things=input("Enter the things given for service=")
        cost.append(things.lower())
        print(cost)
        ans=input("Are there more things(y/n)=")
        if ans in 'yY':
            continue
                
        elif ans in 'nN':
            break
    a=0
    for x in cost:
        if x in items:
            qt=int(input("no. of {} :-".format(x)))
            a+=(items[x]*qt)
            print(x,items[x])
        else:
            qt=int(input("no. of {} :-".format(x)))
            pc=int(input("Enter price for {}:".format(x)))
            print(x,pc)
            a+=(qt*pc)
    print(a)


def delete():
    print("Following are the different services:-")
    print("1. DRY CLEANING")
    print("2. IRONING")
    print("3. DYEING")
    print("4. DARNING")
    print("5. WARDROBE SERVICES")
    print("6. EXIT")
    table=''
    t=int(input("Enter the service you want to proceed with(1-6)="))
    if t==1:
        table='drycleaning'
    elif t==2:
        table='ironing'
    elif t==3:
        table='dyeing'
    elif t==4:
        table='darning'
    elif t==5:
        table='wardrobeservices'
    elif t==6:
        print("Proceeding to the main menu")
        return
    while True:
        mycursor.execute("SELECT * FROM {}".format(table))
        myrecords=mycursor.fetchall()
        print('sno','name','date','contents','quantity','ecode','dateofreturn','phone',sep='     ')
        print("--------------------------------------------------------------------------------------------------------")
        for i in myrecords:
            print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],sep='      ')
        found=0
        e=int(input("Enter ecode whose service has been completed="))
        for i in myrecords:
            if i[5]==e:
                found=1
        if found==0:
            print(e,"does not exist in the service")
        else:
            mycursor.execute("DELETE FROM {} WHERE ECODE={}".format(table,e))
            mydb.commit()
            mycursor.execute("SELECT * FROM {}".format(table))
            myrecords=mycursor.fetchall()
            print('sno','name','date','contents','quantity','ecode','dateofreturn','phone',sep='     ')
            print("--------------------------------------------------------------------------------------------------------")
            for i in myrecords:
                print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],sep='      ') 
        ch=input("Did you choose any other service also(Y/N):-")
        if ch.upper()=='Y':
            continue
        elif ch.upper()=='N':
            break

def update_ph():
    table=input("Enter the table in which you want updation to be done=")
    mycursor.execute("SELECT * FROM {}".format(table))
    myrecords=mycursor.fetchall()
    for i in myrecords:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
    ec=int(input("Enter ecode whose phone you want to update="))
    found=0
    for x in myrecords:
        if x[5]==ec:
            found=1
    if found==1:
        ph=int(input("Enter new phone="))
        mycursor.execute("UPDATE {} SET PHONE={} WHERE ECODE={}".format(table,ph,ec))
        mydb.commit()
        mycursor.execute("SELECT * FROM {}".format(table))
        myrecords=mycursor.fetchall()
        for i in myrecords:
            print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
    mydb.commit()
    print("Record given by you is updated....")

        
#MENU-DRIVEN:-
while True:
    print("*****************************************MAIN MENU*************************************************")
    print("1. Give things for service")
    print("2. Return things given for service")
    print("3. Exit")
    op=int(input("Enter the option chosen(1-3)="))
    if op==1:
        insertion()
    elif op==2:
        delete()
        name()
        pricing()
    elif op==3:
        print("-----------------------THANKS FOR VISITING.HAVE A NICE DAY AHEAD.------------------------------")
        break
    else:
        print("Select option 1-3")
        continue
























































































































































































