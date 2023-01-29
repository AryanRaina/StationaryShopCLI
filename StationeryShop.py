import mysql.connector
import datetime
from tabulate import tabulate

db=input("Enter name of your database:")

mydb=mysql.connector.connect(host='localhost',user='root',password='password')
mycursor = mydb.cursor()

sql="CREATE DATABASE if not exists %s"%(db,)
mycursor.execute(sql)
print("Database created Successfully....")
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
TableName=input("Name of Table to be created:")
query="Create table if not exists "+TableName+" \
(SNo int primary key,\
ItemName varchar(20) not null,\
NameOfDealer varchar(20) not null,\
CostPrice float,\
SellingPrice float,\
Profit float,\
Loss float,\
GST float,\
StockBought int,\
StockSold int,\
StockRemaining int,\
DateOfPurchase date)"
print("Table"+TableName+"Created Successfully....")
mycursor.execute(query)

while True:
    print('\n\n\n')
    print("*"*95)
    print('\t\t\t\t\tMAIN MENU')
    print("*"*95)
    print('\t\t\t\t1. Adding Item records')
    print('\t\t\t\t2. For Displaying Record of ALL the Items')
    print('\t\t\t\t3. For Displaying Record of a particular Item')
    print('\t\t\t\t4. For Deleting Records of ALL the Items')
    print('\t\t\t\t5. For Deleting Record of a particular Item')
    print('\t\t\t\t6. For Modification in a Record')
    print('\t\t\t\t7. For Displaying Stationary Bill')
    print('\t\t\t\t8. For Displaying Stationary Bill for a particular Item')
    print('\t\t\t\t9. For Exit')
    print('Enter Choice...',end='')
    choice=int(input())
    if choice==1:
        try:
            print('Enter Item Information....')
            msno=int(input('Enter SNo:'))
            mitemname=input('Enter Item Name:')
            mnameofdealer=input('Enter Name of Dealer:')
            mcostprice=float(input('Enter Cost Price:'))
            msellingprice=float(input('Enter Selling Price:'))
            if msellingprice > mcostprice:
                mprofit=msellingprice-mcostprice
            elif msellingprice < mcostprice:
                mloss=mcostprice-msellingprice
            elif msellingprice == mcostprice:
                mprofit=0
                mloss=0
            mloss=float()
            mgst=msellingprice*0.18
            mstockbought=int(input('Enter Stock Bought:'))
            mstocksold=int(input('Enter Stock Sold:'))
            mstockremaining=int(input('Enter Stock Remaining:'))
            mdateofpurchase=input('Enter Date of Purchase in YYYYMMDD:')
            rec =(msno,mitemname,mnameofdealer,mcostprice,msellingprice,mprofit,mloss,mgst,mstockbought,mstocksold,mstockremaining,mdateofpurchase)
            query="insert into "+TableName+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,rec)


            mydb.commit()
            print('Record Added Successfully....')
        except Exception as e:
            print('Something went wrong',e)



    elif choice==2:
        try:
            query='select * from '+TableName
            mycursor.execute(query)
            print(tabulate(mycursor, headers=['SNo','ItemName','NameOfDealer','CostPrice','SellingPrice','Profit','Loss','GST','StockBought','StockSold','StockRemaining','DateOfPurchase'], tablefmt='fancy_grid'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)'''
        except:
            print('Something went wrong')

    elif choice==3:
        try:
            en=input('Enter SNo of the record to be displayed...')
            query="select * from "+TableName+" where SNo="+en
            mycursor.execute(query)
            print("\n\nRecord of SNo.:"+en)
            print(tabulate(mycursor, headers=['SNo','ItemName','NameOfDealer','CostPrice','SellingPrice','Profit','Loss','GST','StockBought','StockSold','StockRemaining','DateOfPurchase'], tablefmt='fancy_grid'))
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Nothing to Display')
        except:
            print('Something went wrong')


    elif choice==4:
        try:
            ch=input('Do you want to delete all the records(y/n)')
            if ch.upper()=='Y':
                mycursor.execute('delete from '+TableName)
                mydb.commit()
                print('All the records are deleted...')
        except:
            print('Something went wrong')
    elif choice==5:
        try:
            en=input('Enter SNo of the record to be deleted....')
            query='delete from '+TableName+' where SNo='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print('Deletion Done')
            else:
                print('SNo ',en,'not found')
        except:
            print('Something went wrong')


    elif choice==6:
        try:
            en=input('Enter SNo of the record to be modified....')
            query='select * from '+TableName+' where SNo='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('SNo '+en+' does not exist')
            else:
                mitemname=myrecord[1]
                mnameofdealer=myrecord[2]
                mcostprice=myrecord[3]
                print('SNo :',myrecord[0])
                print('ItemName :',myrecord[1])
                print('NameOfDealer :',myrecord[2])
                print('CostPrice :',myrecord[3])
                print('SellingPrice :',myrecord[4])
                print('Profit :',myrecord[5])
                print('Loss :',myrecord[6])
                print('GST :',myrecord[7])
                print('StockBought :',myrecord[8])
                print('StockSold :',myrecord[9])
                print('StockRemaining :',myrecord[10])
                print('DateOfPurchase :',myrecord[11])
                print('--------------------------------')
                print('Type Value to modify below or just press Enter for no change')
                x=input('Enter ItemName ')
                if len(x)>0:
                    mitemname=x
                x=input('Enter NameOfDealer ')
                if len(x)>0:
                    mnameofdealer = x
                x=input('Enter CostPrice ')
                if len(x)>0:
                    mcostprice=float(x)
                x=input('Enter SellingPrice ')
                if len(x)>0:
                    msellingprice=float(x)
                if msellingprice > mcostprice:
                    mprofit=msellingprice-mcostprice
                elif msellingprice < mcostprice:
                    mloss=mcostprice-msellingprice
                elif msellingprice == mcostprice:
                    mprofit=0
                    mloss=0
                mloss=float()
                mgst=msellingprice*0.18
                mstockbought=int(input('Enter Stock Bought:'))
                mstocksold=int(input('Enter Stock Sold:'))
                mstockremaining=int(input('Enter Stock Remaining:'))
                mdateofpurchase=input('Enter Date of Purchase in YYYYMMDD:')
                query='update '+TableName+' set ItemName='+"'"+mitemname+"'"+','+'NameOfDealer='+"'"+mnameofdealer+"'"+','+'CostPrice='+str(mcostprice)+','+'SellingPrice='+str(msellingprice)+','+'Profit='+str(mprofit)+','+'Loss='+str(mloss)+','+'GST='+str(mgst)+','+'StockBought='+str(mstockbought)+','+'StockSold='+str(mstocksold)+','+'StockRemaining='+str(mstockremaining)+','+'DateOfPurchase='+str(mdateofpurchase)+' where SNo='+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print('Record Modified')
        except:
            print('Something went wrong')
    elif choice==7:
        try:
            query=='select * from '+TableName
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print(95*'*')
            print('Stationary Bill'.center(90))
            print(95*'*')
            now = datetime.datetime.now()
            print("Current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            print(95*'-')
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s %-8s %-8s %-8s'%('SNo','ItemName','NameOfDealer','CostPrice','SellingPrice','Profit','Loss','GST','StockBought','StockSold','StockRemaining','DateOfPurchase'))
            print(95*'-')
            for rec in myrecords:
                print('%-4d %-15s %-10s %-8.2f %-8.2f %-8.2f %-9.2f %-8.2f %-9s %-8s %-8s %-8s'%rec)
            print(95*'-')
        except Exception as e:
            print('Something went wrong',e)

    elif choice==8:
        try:
            en=input("Enter SNo. whose bill you want to retreive: ")
            query='select * from '+TableName+' where SNo='+en
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n")
            print('-'*95)
            print("Stationary Bill ".center(90))
            print('-'*95)
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(tabulate(mycursor, headers=['SNo','ItemName','NameOfDealer','CostPrice','SellingPrice','Profit','Loss','GST','StockBought','StockSold','StockRemaining','DateOfPurchase'], tablefmt='fancy_grid'))

        except Exception as e:
            print('Something went wrong',e)

    elif choice==9:
        break
    else:
        print('Wrong Choice....')

    
                
            
            
    
