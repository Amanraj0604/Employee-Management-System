from tkinter import*
import mysql.connector
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('employee Mannagement System')
        StringVar
        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproffcomb=StringVar()
        self.var_idproff=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        lbl_title=Label(self.root,text='EMPLOYEE MANNAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='black',bg='skyblue')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #logo
        img_logo=Image.open(r'F:\1st Sem\python obb\wether1\Employee Mannagment System\aserts\5.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=5,width=35,height=40)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='lightgreen')
        img_frame.place(x=0,y=50,width=1530,height=160)



        # #2nd img
        img2=Image.open(r'F:\1st Sem\python obb\wether1\Employee Mannagment System\aserts\2.jpg')
        img2=img2.resize((520,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=520,y=0,width=520,height=160)
        
        #main frame

        main_frame=Frame(self.root,bd=6,relief=RIDGE,bg='skyblue')
        main_frame.place(x=10,y=230,width=1500,height=565)

        #upper frame
        upper_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Employee Infromation',font=('time new roman',11,'bold'),fg='darkblue')
        upper_frame.place(x=10,y=10,width=1470,height=270)

        # Labels and entry fields

        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('select Department','HR','Software Engineer','Mannager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10, sticky=W)

        #Name
        lbl_Name=Label(upper_frame,font=('arial',11,'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',12,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)


        #lbl_Designition
        lbl_Designition=Label(upper_frame,font=('arial',11,'bold'),text='designition:',bg='white')
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=('arial',12,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Email
        lbl_email=Label(upper_frame,font=('arial',11,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',12,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,font=('arial',11,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',12,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        #Married
        lbl_merried_status=Label(upper_frame,font=('arial',11,'bold'),text='Married Status:',bg='white')
        lbl_merried_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_married['value']=('Married','unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #dob
        lbl_dob=Label(upper_frame,font=('arial',11,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',12,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #Date of join
        lbl_doj=Label(upper_frame,font=('arial',11,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',12,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)


        #ID Proff
        # lbl_id_proff=Label(upper_frame,font=('arial',11,'bold'),text='ID:',bg='white')
        # lbl_id_proff.grid(row=4,column=4,sticky=W,padx=2,pady=7)

        com_txt_proff=ttk.Combobox(upper_frame,textvariable=self.var_idproffcomb,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_proff['value']=('Select ID ','PAN CARD','ADDHAR','DRIVING LICENCE','VOTER ID')
        com_txt_proff.current(0)
        com_txt_proff.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproff,width=22,font=('arial',12,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        lbl_gender=Label(upper_frame,font=('arial',11,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_gender['value']=('Male','Female','Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone

        lbl_phone=Label(upper_frame,font=('arial',11,'bold'),text='Phone No:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',12,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #country

        lbl_country=Label(upper_frame,font=('arial',11,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',12,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #Sallary(CTC)
        lbl_ctc=Label(upper_frame,font=('arial',11,'bold'),text='Salary(CTC):',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',12,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #mask image
        img_mask=Image.open(r'F:\1st Sem\python obb\wether1\Employee Mannagment System\aserts\6.png')
        img_mask=img_mask.resize((220,220),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_mask)
        
        self.img_mask=Label(upper_frame,image=self.photo3)
        self.img_mask.place(x=1050,y=0,width=220,height=220)

        #Button Frame
        
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1280,y=10,width=170,height=210)

        btn_add=Button(button_frame,command=self.add_data,text='Save',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,command=self.reset_data,text='Clear',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        
        
        #Down frame
        down_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Employee Details',font=('time new roman',11,'bold'),fg='darkblue',bg='lightyellow')
        down_frame.place(x=10,y=280,width=1470,height=270)
        
        #search frame
        search_frame=LabelFrame(down_frame,bd=5,relief=RIDGE,text='Employee Table Details',font=('time new roman',11,'bold'),fg='darkblue',)
        search_frame.place(x=0,y=0,width=1453,height=60)

        search_by=Label(search_frame,font=('arial',11,'bold'),text='Search By:',fg='white',bg='black')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_search['value']=('Select Option','Name','ID_NUM','DOJ')
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,sticky=W,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,command=self.fetch_data,text='Show ALL',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        styahome=Label(search_frame,text='wear a mask',font=('Times new roman',30,'bold'),fg="red",bg='white')
        styahome.place(x=780,y=0,width=600,height=30)


        img_logo_mask=Image.open(r'F:\1st Sem\python obb\wether1\Employee Mannagment System\aserts\mask.jpg')
        img_logo_mask=img_logo_mask.resize((45,45),Image.ANTIALIAS)
        self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask)

        self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=30)

        ######################################################  EMPLOYEE TABLE  ##########################################################   
        
        #tABLE FRAME
        Table_frame=LabelFrame(down_frame,bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=60,width=1450,height=165)

        #Scroll bar

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(Table_frame,columns=('dep','name','Degi','E-mail','address','married','DOB','DOJ','idproffcomb','idproff','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('Degi',text='Degignation')
        self.employee_table.heading('E-mail',text='Email')
        self.employee_table.heading('address',text='address')
        self.employee_table.heading('married',text='Married')
        self.employee_table.heading('DOB',text='DOB')
        self.employee_table.heading('DOJ',text='DOJ')
        self.employee_table.heading('idproffcomb',text='ID type')
        self.employee_table.heading('idproff',text='ID proff')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('Degi',width=100)
        self.employee_table.column('E-mail',width=120)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('DOB',width=100)
        self.employee_table.column('DOJ',width=100)
        self.employee_table.column('idproffcomb',width=100)
        self.employee_table.column('idproff',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ##################  Function ##################

    def add_data(self):
        if self.var_dep.get()==""or self.var_email.get()=="": 
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sindi',database='employee')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                
                            self.var_dep.get(),
                            self.var_name.get(),
                            self.var_designation.get(),
                            self.var_email.get(),
                            self.var_address.get(),
                            self.var_married.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_idproffcomb.get(),
                            self.var_idproff.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_country.get(),
                            self.var_salary.get()
                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been Added',parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #fatch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Sindi',database='employee')
        my_cursor=conn.cursor()
        my_cursor.execute('select *from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)

            conn.commit()
        conn.close()


    # Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproffcomb.set(data[8])
        self.var_idproff.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    #update 

    def update_data(self):
        if self.var_dep.get()==""or self.var_email.get()=="": 
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('update','Are you sure update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Sindi',database='employee')
                    my_cursor=conn.cursor() 
                    my_cursor.execute('update employee set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,ID_TYPE=%s,Gender=%s,Phone_no=%s,Country=%s,Salary=%s where ID_NUM=%s',(

                            self.var_dep.get(),
                            self.var_name.get(),
                            self.var_designation.get(),
                            self.var_email.get(),
                            self.var_address.get(),
                            self.var_married.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_idproffcomb.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_country.get(),
                            self.var_salary.get(),
                            self.var_idproff.get(),
                                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('suceess','Employee Successfully update',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #Delete

    def delete_data(self):
        if self.var_dep.get()==""or self.var_email.get()=="": 
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Sindi',database='employee')
                    my_cursor=conn.cursor()
                    sql='delete from employee where ID_NUM=%s'
                    value=(self.var_idproff.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



    #Reset

    def reset_data(self):
        
        self.var_dep.set("select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproffcomb.set("select ID")
        self.var_idproff.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()==''or self.var_search.get()=="":
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Sindi',database='employee')
                my_cursor=conn.cursor()
                my_cursor.execute('select *from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                 messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

