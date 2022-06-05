from tkinter import *
import tkinter.messagebox
from datetime import *
import mysql.connector
root=Tk
root1=Tk
s='2468110'
dat=date.today()
dat=str(datetime.strftime(dat,"%d-%m-%Y"))
try:
    con=mysql.connector.connect(host="localhost",user="root",passwd="yash@1122",database="vimaltara")
    mycur=con.cursor()

except Exception as e:
    print(e)
def close():
    global root
    root.destroy()
def paydb(c):
    global re
    pa=ip.get()
    if pa>re:
        tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="BALANCE FEES IS LESS THEN AMOUN RECEIVED")
    else:
        if c==1:
            re-=pa
            r=str(re)
            try:
                sql="UPDATE Student SET First_Installment=%s WHERE Name=%s and STD=%s"
                op=pa,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Remaining=%s WHERE Name=%s and STD=%s"
                op=re,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Date_Of_First_Installment=%s WHERE Name=%s and STD=%s"
                op=dat,name,std
                mycur.execute(sql,op)
                con.commit()
                tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY",message="FEES UPDATED")
                wel()
            except Exception as e:
                print(e)
        if c==2:
            re-=pa
            r=str(re)
            try:
                sql="UPDATE Student SET Second_Installment=%s WHERE Name=%s and STD=%s"
                op=pa,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Remaining=%s WHERE Name=%s and STD=%s"
                op=re,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Date_Of_Second_Installment=%s WHERE Name=%s and STD=%s"
                op=dat,name,std
                mycur.execute(sql,op)
                con.commit()
                tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY",message="FEES UPDATED")
                wel()
            except Exception as e:
                print(e)
        if c==3:
            re-=pa
            r=str(re)
            try:
                sql="UPDATE Student SET Third_Installment=%s WHERE Name=%s and STD=%s"
                op=pa,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Remaining=%s WHERE Name=%s and STD=%s"
                op=re,name,std
                mycur.execute(sql,op)
                con.commit()
                sql="UPDATE Student SET Date_Of_Third_Installment=%s WHERE Name=%s and STD=%s"
                op=dat,name,std
                mycur.execute(sql,op)
                con.commit()
                tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY",message="FEES UPDATED")
                wel()
            except Exception as e:
                print(e)
def full():
    global root
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    tf=str(tfees)
    n1=str(in1)
    d1=str(date1)
    n2=str(in2)
    d2=str(date2)
    n3=str(in3)
    d3=str(date3)
    Label(root,text="NAME: "+name.upper(),font="none 13 bold").grid(row=0,sticky='w')
    Label(root,text="STD: "+std,font="none 13 bold").grid(row=1, sticky='w')
    Label(root,text="JOINING DATE: "+datea,font="none 13 bold").grid(row=3,sticky='w')
    Label(root,text="TOTAL FEES: Rs."+tf,font="none 13 bold").grid(row=2,sticky='w')
    Label(root,text="FULL FEES RECEIVED",font="none 14 bold",fg="green").grid(row=4,sticky='w')
    if in1!=None and in2==None and in3==None:
        Label(root,text="TOTAL FEES RECEIVED FOR Rs."+n1+" on "+d1,font="none 13 bold").grid(row=5,sticky='w')
        Button(root,text="HOME",font="none 13 bold",borderwidth=2,relief=SOLID,command=wel).grid(row=6)
    elif in1!=None and in2!=None and in3==None:
        Label(root,text="FIRST INSTALLMENT RECEIVED FOR Rs."+n1+" on "+d1,font="none 13 bold").grid(row=5,sticky='w')
        Label(root,text="BALANCE FEES RECEIVED FOR Rs."+n2+" on "+d2,font="none 13 bold").grid(row=6,sticky='w')
        Button(root,text="HOME",font="none 13 bold",borderwidth=2,relief=SOLID,command=wel).grid(row=7)
    else:
        Label(root,text="FIRST INSTALLMENT RECEIVED FOR Rs."+n1+" on "+d1,font="none 13 bold").grid(row=5,sticky='w')
        Label(root,text="SECOND INSTALLMENT RECEIVED FOR Rs."+n2+" on "+d2,font="none 13 bold").grid(row=6,sticky='w')
        Label(root,text="BALANCE FEES RECEIVED FOR Rs."+n3+" on "+d3,font="none 13 bold").grid(row=7,sticky='w')
        Button(root,text="HOME",font="none 13 bold",borderwidth=2,relief=SOLID,command=wel).grid(row=8)
def feeans(c,ans):
    global root1
    root1.destroy()
    if ans==1:
        paydb(c)
    else:
        wel()
def feeco(c):
    global root1
    py=ip.get()
    if py > re:
        paydb(c)
    else:
        root1=Tk()
        root1.title("VIMALTARA ACADEMY")
        root1.iconbitmap("images.ico")
        Label(root1,text="CONFIRM PAYMENT RECEIPT OF Rs."+str(py),font="none 13 bold").grid(row=0,columnspan=2)
        py=str(re-py)
        Label(root1,text="BALANCE FEES Rs."+py,font="none 13 bold").grid(row=1,columnspan=2)
        Button(root1,text="CONFIRM",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeans(c,1)).grid(row=2)
        Button(root1,text="CANCEL",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeans(c,0)).grid(row=2,column=1)
def pay(c):
    global root
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    global ip
    tf=str(tfees)
    ip=IntVar()
    Label(root,text="NAME: "+name.upper(),font="none 13 bold").grid(row=0,sticky='w',columnspan=3)
    Label(root,text="STD: "+std,font="none 13 bold").grid(row=1,sticky='w',columnspan=3)
    Label(root,text="JOINING DATE: "+datea,font="none 13 bold").grid(row=3,sticky='w',columnspan=3)
    Label(root,text="TOTAL FEES: Rs."+tf,font="none 13 bold").grid(row=2,sticky='w',columnspan=3)
    if c==1:
        Label(root,text="FIRST INSTALLMENT: Rs.",font="none 13 bold").grid(row=4)
        Entry(root,font="none 13 bold",textvariable=ip).grid(row=4,column=1)
        Button(root,text="UPDATE",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeco(1)).grid(row=4,column=2)
    if c==2:
        n1=str(in1)
        d1=str(date1)
        r=str(re)
        Label(root,text="FIRST INSTALLMENT RECEIVED FOR Rs."+n1+" on "+d1,font="none 13 bold").grid(row=4,sticky='w',columnspan=3)
        Label(root,text="BALANCE FEES: Rs."+r,font="none 13 bold").grid(row=5,sticky='w',columnspan=3)
        Label(root,text="SECOND INSTALLMENT: Rs.",font="none 13 bold").grid(row=6)
        Entry(root,font="none 13 bold",textvariable=ip).grid(row=6,column=1)
        Button(root,text="UPDATE",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeco(2)).grid(row=6,column=2)
    if c==3:
        n1=str(in1)
        d1=str(date1)
        n2=str(in2)
        d2=str(date2)
        r=str(re)
        Label(root,text="FIRST INSTALLMENT RECEIVED FOR Rs."+n1+" on "+d1,font="none 13 bold").grid(row=4,sticky='w',columnspan=3)
        Label(root,text="SECOND INSTALLMENT RECEIVED FOR Rs."+n2+" on "+d2,font="none 13 bold").grid(row=5,sticky='w',columnspan=3)
        Label(root,text="BALANCE FEES RECEIVABLE: Rs."+r,font="none 13 bold",fg="red").grid(row=7,sticky='w',columnspan=3)
        Label(root,text="THIRD INSTALLMENT: Rs.",font="none 13 bold").grid(row=8)
        Entry(root,font="none 13 bold",textvariable=ip).grid(row=8,column=1)
        Button(root,text="UPDATE",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeco(3)).grid(row=8,column=2)
def uppay():
    close()
    if in1==None:
        pay(1)
    if in1!=None and in2==None and re!=0:
        pay(2)
    if in1!=None and in2!=None and in3==None and re!=0:
        pay(3)
    if re==0:
        full()
def delete():
    n=na.get()
    s=st.get()
    try:
        mycur.execute("DELETE FROM student WHERE Name='"+n+"' and STD='"+s+"'")
        con.commit()
        tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY",message="RECORD DELETED")
        wel()
    except Exception as e:
        print(e)
def feeeditdb():
    try:
        sql="UPDATE Student SET Remaining=%s WHERE Name=%s and STD=%s"
        op=re,name,std
        mycur.execute(sql,op)
        con.commit()
        sql="UPDATE Student SET Total_Fees=%s WHERE Name=%s and STD=%s"
        op=tfees,name,std
        mycur.execute(sql,op)
        con.commit()
        tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY",message="RECORD UPDATED")
        wel()
    except Exception as e:
        print(e)
def coans(c,ans):
    global root1
    root1.destroy()
    if ans==1:
        if c==2.1 or c==2.2:
            feeeditdb()
        if c==3:
            delete()
    else:
        wel()
def feeedco(c):
    global re
    global tfees
    ed=ip.get()
    if c==2.2 and ed>tfees:
        tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="DECREASE AMOUNT EXCEEDS TOTAL FEES")
    else:
        global root1
        root1=Tk()
        root1.title("VIMALTARA ACADEMY")
        root1.iconbitmap("images.ico")
        if c==2.1:
            tfees+=ed
            re+=ed
            t=str(tfees)
            r=str(re)
            ed=str(ed)
            Label(root1,text="CONFIRM FEES INCREASE FOR Rs."+ed,font="none 13 bold").grid(row=0,columnspan=2)
            Label(root1,text="UPDATED FEES AMOUNT IS Rs."+t+" AND BALANCE IS Rs."+r,font="none 13 bold").grid(row=1,columnspan=2)
            Button(root1,text="CONFIRM",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,1)).grid(row=2)
            Button(root1,text="CANCEL",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,0)).grid(row=2,column=1)
        if c==2.2:
            tfees-=ed
            re-=ed
            t=str(tfees)
            r=str(re)
            ed=str(ed)
            Label(root1,text="CONFIRM FEES DECREASE FOR Rs."+ed,font="none 13 bold").grid(row=0,columnspan=2)
            Label(root1,text="UPDATED FEES AMOUNT IS Rs."+t+" AND BALANCE IS Rs."+r,font="none 13 bold").grid(row=1,columnspan=2)
            Button(root1,text="CONFIRM",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,1)).grid(row=2)
            Button(root1,text="CANCEL",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,0)).grid(row=2,column=1)
def editfee():
    close()
    global root
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    global ip
    ip=IntVar()
    tf=str(tfees)
    r=str(re)
    Label(root,text="NAME: "+name.upper(),font="none 13 bold").grid(row=0,sticky='w',columnspan=2)
    Label(root,text="STD: "+std,font="none 13 bold").grid(row=1,sticky='w',columnspan=2)
    Label(root,text="JOINING DATE: "+datea,font="none 13 bold").grid(row=3,sticky='w',columnspan=2)
    Label(root,text="TOTAL FEES: Rs."+tf,font="none 13 bold").grid(row=2,sticky='w',columnspan=2)
    Label(root,text="BALANCE FEES RECEIVABLE: Rs."+r,font="none 13 bold").grid(row=4,sticky='w',columnspan=2)
    Label(root,text="ENTER INCREASE / DECREASE FEES AMOUNT: Rs.",font="none 13 bold").grid(row=5)
    Entry(root,textvariable=ip,font="none 13 bold").grid(row=5,column=1)
    Button(root,text="INCREASE",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeedco(2.1)).grid(row=6)
    Button(root,text="DECREASE",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:feeedco(2.2)).grid(row=6,column=1)
def delco(c):
    global root1
    root1=Tk()
    root1.title("VIMALTARA ACADEMY")
    root1.iconbitmap("images.ico")
    Label(root1,text="CONFIRM DELETE RECORD",font="none 13 bold").grid(row=0,columnspan=2)
    Button(root1,text="CONFIRM",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,1)).grid(row=1)
    Button(root1,text="CANCEL",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:coans(c,0)).grid(row=1,column=1)
def search(c):
    global name
    global std
    global datea
    global tfees
    global in1
    global date1
    global in2
    global date2
    global in3
    global date3
    global re
    n=na.get()
    s=st.get()
    try:
        mycur.execute("select * from student where Name='"+n+"' and STD='"+s+"';")
        r=mycur.fetchall()
        if r==[]:
            tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="NO RECORD FOUND")
        else:
            for i in r:
                name=i[0]
                std=i[1]
                datea=i[2]
                tfees=i[3]
                in1=i[4]
                date1=i[5]
                in2=i[6]
                date2=i[7]
                in3=i[8]
                date3=i[9]
                re=i[10]
                if c==1:
                    uppay()
                if c==2:
                    editfee()
                if c==3:
                    delco(c)
    except Exception as e:
        print(e)
def updel(c):
    global root
    global st
    global na
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    na=StringVar()
    st=StringVar()
    Label(root,text="NAME",font="none 13 bold").grid(row=0,sticky='w')
    Entry(root,textvariable=na,font="none 13 bold").grid(row=0,column=1)
    Label(root,text="STD",font="none 13 bold").grid(row=1,sticky='w')
    Entry(root,textvariable=st,font="none 13 bold").grid(row=1,column=1)
    if c==1:
        Button(root,text="PAY FEES",borderwidth=2,relief=SOLID,font="none 13 bold",command=lambda:search(1)).grid(row=2)
        Button(root,text="EDIT FEES",borderwidth=2,relief=SOLID,font="none 13 bold",command=lambda:search(2)).grid(row=2,column=1)
        Button(root,text="HOME",borderwidth=2,relief=SOLID,font="bold 13 bold",command=wel).grid(row=3,columnspan=2)
    else:
        Button(root,text="DELETE",borderwidth=2,relief=SOLID,font="none 13 bold",command=lambda:search(3)).grid(row=2,column=1)
        Button(root,text="HOME",borderwidth=2,relief=SOLID,font="bold 13 bold",command=wel).grid(row=2)
def ans(c):
    if c==0:
        wel()
    if c==1:
        search(1)
def qpay():
    global root
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    Label(root,text="DO YOU WANT TO PAY FEE NOW?",font="none 13 bold").grid(row=0,columnspan=2)
    Button(root,text="YES",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:ans(1)).grid(row=1)
    Button(root, text="NO",font="none 13 bold",borderwidth=2,relief=SOLID,command=lambda:ans(0)).grid(row=1,column=1)
def create(c):
    global mycur
    global con
    if c==2:
        n=namea.get()
        un=user_name.get()
        p1=pass1.get()
        p2=pass2.get()
        if n=="" or un=="" or p1=="" or p2=="":
            tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="You need to fill all details")
        elif p1!=p2:
            tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="PASSWORD DOES NOT MATCH")
        else:
            try:
                mycur.execute("INSERT INTO admin(Name,user_name,Password) VALUES('"+n+"','"+un+"','"+p1+"');")
                con.commit()
                tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY", message="CREATED")
                close()
                first()
            except mysql.connector.errors.IntegrityError:
                tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="USER NAME ALREADY EXISTS PLEASE USE ANOTHER USER NAME")
            except Exception as e:
                print(e)
    else:
        n=na.get()
        s=st.get()
        d=dat
        t=tf.get()
        if n=="" or s=="" or t==0:
            tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="You need to fill all details")
        else:
            try:
                sql="INSERT INTO student(Name,STD,Date_Of_Admission,Total_Fees,Remaining) VALUES(%s,%s,%s,%s,%s);"
                op=(n,s,d,t,t)
                mycur.execute(sql,op)
                con.commit()
                tkinter.messagebox.showinfo(title="VIMALTARA ACADEMY", message="CREATED")
                close()
                qpay()
            except Exception as e:
                print(e)
def new():
    global root
    global na
    global st
    global tf
    root=Tk()
    na=StringVar()
    st=StringVar()
    tf=IntVar()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    Label(root,text="NAME",font="bold 13 bold").grid(row=0,stick='e')
    Entry(root,textvariable=na,font="bold 13 bold").grid(row=0,column=1)
    Label(root,text="STANDARD",font="bold 13 bold").grid(row=1,stick='e')
    Entry(root,textvariable=st,font="bold 13 bold").grid(row=1,column=1)
    Label(root,text="JOINING DATE",font="bold 13 bold").grid(row=3,stick='e')
    Label(root,text=dat,font="bold 13 bold").grid(row=3,column=1)
    Label(root,text="TOTAL FEES",font="bold 13 bold").grid(row=2,stick='e')
    Entry(root,textvariable=tf,font="bold 13 bold").grid(row=2,column=1)
    Button(root,text="CREATE RECORD",borderwidth=2,relief=SOLID,font="bold 13 bold",command=lambda:create(1)).grid(row=4,column=1)
    Button(root,text="HOME",borderwidth=2,relief=SOLID,font="bold 13 bold",command=wel).grid(row=4)
def rootend(c):
    close()
    if c==1:
        updel(1)
    elif c==2:
        new()
    else:
        updel(2)
def wel():
    close()
    global root
    root=Tk()
    root.title("VIMALTARA ACADEMY")
    root.iconbitmap("images.ico")
    Label(root,text="WELCOME "+namea.upper(),font="bold 13 bold").grid(row=1,columnspan=7)
    Label(root,text=" ").grid(row=3)
    Button(root,text="UPDATE",borderwidth=2,relief=SOLID,font="bold 13 bold",command=lambda :rootend(1)).grid(row=3,column=1)
    Label(root,text=" ").grid(row=3,column=2)
    Button(root,text="ADD NEW",borderwidth=2,relief=SOLID,font="bold 13 bold",command=lambda :rootend(2)).grid(row=3,column=3)
    Label(root,text=" ").grid(row=3,column=4)
    Button(root,text="DELETE",borderwidth=2,relief=SOLID,font="bold 13 bold",command=lambda :rootend(3)).grid(row=3,column=5)
    Label(root,text=" ").grid(row=3,column=6)
def new2():
    close()
    global root
    root = Tk()
    root.iconbitmap("images.ico")
    root.title("VIMALTARA ACADEMY")
    global namea
    global user_name
    global pass1
    global pass2
    namea=StringVar()
    user_name=StringVar()
    pass1=StringVar()
    pass2=StringVar()
    Label(root, text="NAME",font="none 10 bold").grid(row=0,stick='e')
    Entry(root, font="none 10 bold",textvariable=namea).grid(row=0,column=1)
    Label(root, text="USER NAME",font="none 10 bold").grid(row=1,stick='e')
    Entry(root, font="none 10 bold",textvariable=user_name).grid(row=1,column=1)
    Label(root, text="PASSWORD",font="none 10 bold").grid(row=2,stick='e')
    Entry(root, font="none 10 bold",textvariable=pass1,show="*").grid(row=2,column=1)
    Label(root, text="CONFIRM PASSWORD",font="none 10 bold").grid(row=3)
    Entry(root, font="none 10 bold",textvariable=pass2,show="*").grid(row=3,column=1)
    Button(root, text="CREATE",font="none 15 bold",borderwidth=2,relief=SOLID,command=lambda:create(2)).grid(row=4,columnspan=2)
def check():
    p=pa.get()
    if p==s:
        new2()
    else:
        tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY",message="INCORRECT PASSWORD")
def new1():
    close()
    global root
    global pa
    root=Tk()
    root.iconbitmap("images.ico")
    root.title("VIMALTARA ACADEMY")
    pa=StringVar()
    Label(root,text="ENTER SECURITY CODE",font="none 13 bold").grid(row=0)
    Entry(root,font="none 13 bold",show="*",textvariable=pa).grid(row=0,column=1)
    Button(root,text="NEXT",font="none 13 bold",command=check,borderwidth=2,relief=SOLID).grid(row=1,columnspan=2)
def roottroot():
    global mycur
    global con
    global namea
    ip1=p1.get()
    ip2=p2.get()
    try:
        mycur.execute("select * from admin where User_Name='"+ip1+"' and Password='"+ip2+"';")
        r=mycur.fetchall()
        for i in r:
            namea=i[0]
            namel=i[1]
            passwordl=i[2]
        if ip1==namel and ip2==passwordl:
            wel()
    except Exception:
        tkinter.messagebox.showwarning(title="VIMALTARA ACADEMY", message="INCORRECT USERNAME OR PASSWORD")
def first():
    global root
    global p1
    global p2
    root=Tk()
    p1=StringVar()
    p2=StringVar()
    root.iconbitmap("images.ico")
    root.title("VIMALTARA ACADEMY")
    Label(root,text="USERNAME",font="none 13 bold").grid(row=0)
    Entry(root,font="none 13 bold",textvariable=p1).grid(row=0,column=1)
    Label(root,text="PASSWORD",font="none 13 bold").grid(row=1)
    Entry(root,font="none 13 bold",show="*",textvariable=p2).grid(row=1,column=1)
    Button(root,text="LOG IN",borderwidth=2,relief=SOLID,font="none 13 bold",command=roottroot).grid(row=2)
    Button(root,text="NEW USER",borderwidth=2,relief=SOLID,font="none 13 bold",command=new1).grid(row=2,column=1)
    root.mainloop()
first()