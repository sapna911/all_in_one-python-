from tkinter import*
from tkinter import ttk
import random
import time
from datetime import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        self.Nametablet=StringVar()
        self.ref = StringVar()
        self.Lot  = StringVar()
        self.NoOftablets= StringVar()
        self.Dose = StringVar()
        self.issuedate = StringVar()
        self.expdate = StringVar()
        self.Dailydose= StringVar()
        self.SideEffect= StringVar()
        self.Furtherinfo= StringVar()
        self.Bloodpressure = StringVar()
        self.Storage = StringVar()
        self.Medicine = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber= StringVar()
        self.Patientname = StringVar()
        self.PatientAddress = StringVar()
        self.DateOfBirth = StringVar()





        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        # ====================================DATAFRAME==========================================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1360,height=399)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                                 font=("arial",12,"bold"),text="patient Information")
        DataFrameLeft.place(x=4,y=3,width=990,height=355)

        DataFrameRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                   font=("arial", 12, "bold"), text="prescription")
        DataFrameRight.place(x=1000, y=3, width=310, height=355)

        #========================buttons frame================================================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=525,width=1360,height=60)

        # ========================Details frame================================================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=585, width=1360, height=120)

        #=======================================DataframeLeft=================================

        lblNameTablet=Label(DataFrameLeft,text="NAMES OF TABLET",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nametablet,state="readonly",font=("arial",12,"bold"),
                                                                                  width=33)
        comNametablet["values"]=("NICE","CORONA VACACINE","ACETAMIOPHEN","ADDERALL","AMLODIPINE","ATIVAN")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="REFFRENCE NO:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LOT:", padx=2,pady=4)
        lblLot.grid(row=2, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=2, column=1)


        lblNoOftablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NO OF TABLETS:", padx=2,pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.NoOftablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="DOSE:", padx=2, pady=6)
        lblDose.grid(row=4, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Dose, width=35)
        txtDose.grid(row=4, column=1)

        lblissuedate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ISSUE DATE:", padx=2, pady=6)
        lblissuedate.grid(row=5, column=0, sticky=W)
        txtissuedate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.issuedate, width=35)
        txtissuedate.grid(row=5, column=1)

        lblexpdate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="EXP DATE:", padx=2, pady=6)
        lblexpdate.grid(row=6, column=0, sticky=W)
        txtexpdate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.expdate, width=35)
        txtexpdate.grid(row=6, column=1)

        lblDailydose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="DAILY DOSE:", padx=2, pady=4)
        lblDailydose.grid(row=7, column=0, sticky=W)
        txtDailydose = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Dailydose, width=35)
        txtDailydose.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="SIDE EFFECT:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.SideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FURTHER INFORMATION:", padx=2,)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Furtherinfo, width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="BLOOD PRESSURE:", padx=2,pady=6 )
        lblBloodpressure.grid(row=1, column=2, sticky=W)
        txtBloodpressure = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Bloodpressure, width=35)
        txtBloodpressure.grid(row=1, column=3)



        lblStorage=  Label(DataFrameLeft, font=("arial", 12, "bold"), text="STORAGE ADVICE:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Storage, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="MEDICATION:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Medicine, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PATIENT ID:", padx=2, pady=6)
        lblPatientId .grid(row=4, column=2, sticky=W)
        txtPatientId  = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.PatientId, width=35)
        txtPatientId .grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS NUMBER:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.NhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PATIENT NAME:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname= Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.Patientname, width=35)
        txtPatientname.grid(row=6, column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PATIENT ADDRESS:", padx=2, pady=6)
        lblPatientAddress.grid(row=7, column=2, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=7, column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="DATE OF BIRTH:", padx=2, pady=6)
        lblDateOfBirth .grid(row=8, column=2, sticky=W)
        txtDateOfBirth  = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth .grid(row=8, column=3)


        #===========================DATAFRAMERIGHT=======================
        self.txtPrescription=Text(DataFrameRight, font=("arial", 12, "bold"),width=28,height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #==================================buttons===================================
        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white", font=("arial", 12, "bold"),width=20, padx=2, pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="UPDATE", bg="green", fg="white",
                                     font=("arial", 12, "bold"),
                                     width=20,  padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="DELETE", bg="green", fg="white",
                                     font=("arial", 12, "bold"),
                                     width=20, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="CLEAR", bg="green", fg="white",
                                     font=("arial", 12, "bold"),
                                     width=20, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="EXIT", bg="green", fg="white",
                          font=("arial", 12, "bold"),
                          width=20,  padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        #====================table==============================================================================================
        #==========================================scrollbar=============================================================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("NameTablet","NoOftablets","Dose","issuedate","expdate","Dailydose","SideEffect","Furtherinfo","Bloodpressure"
                                                             ,"ref" ,"Storage","Medicine","PatientId","NhsNumber","Patientname","PatientAddress","DateOfBirth")
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack  (side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameTablet", text="NAMES OF TABLET")
        self.hospital_table.heading("NoOftablets",text="NO OF TABLETS")
        self.hospital_table.heading("Dose", text="DOSE")
        self.hospital_table.heading("issuedate", text="ISSUE DATE")
        self.hospital_table.heading("expdate", text="EXP DATE")
        self.hospital_table.heading("Dailydose", text="DAILY DOSE")
        self.hospital_table.heading("SideEffect", text="SIDE EFFECT")
        self.hospital_table.heading("Furtherinfo", text="FURTHER INFORMATION")
        self.hospital_table.heading("Bloodpressure", text="BLOOD PRESSURE")
        self.hospital_table.heading("ref", text="REFERENCE NO.")
        self.hospital_table.heading("Storage", text="STORAGE")
        self.hospital_table.heading("Medicine", text="MEDICATION")
        self.hospital_table.heading("PatientId", text="PATIENT ID")
        self.hospital_table.heading("NhsNumber", text="NHS NUMBER")
        self.hospital_table.heading("Patientname", text="PATIENT NAME")
        self.hospital_table.heading("PatientAddress", text="PATIENT ADDRESS")
        self.hospital_table.heading("DateOfBirth", text="DATE OF BIRTH")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("NameTablet",width=99)
        self.hospital_table.column("NoOftablets", width=93)
        self.hospital_table.column("Dose", width=40)
        self.hospital_table.column("issuedate", width=68)
        self.hospital_table.column("expdate", width=68)
        self.hospital_table.column("Dailydose", width=70)
        self.hospital_table.column("SideEffect", width=75)
        self.hospital_table.column("Furtherinfo",width=139)
        self.hospital_table.column("Bloodpressure", width=105)
        self.hospital_table.column("ref",width=95)
        self.hospital_table.column("Storage", width=60)
        self.hospital_table.column("Medicine",width=79)
        self.hospital_table.column("PatientId", width=65)
        self.hospital_table.column("NhsNumber", width=79)
        self.hospital_table.column("Patientname",width=90)
        self.hospital_table.column("PatientAddress",width=100)
        self.hospital_table.column("DateOfBirth", width=90)

        self.hospital_table.pack(fill=BOTH, expand=1)


 #========================================FINCTINALITY DECLRATION============================================
def  iprescriptionData(self):
         if self.Nametablet.get()=="" or self.ref.get()=="":
             messagebox.showerror("Error", "All field are required")
         else:
             conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", databse="Mydata")
             my_cursor = conn.cursor()
             my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",
                               (

                                   self.Nametablet.get(),
                                   self.ref.get(),
                                   self.Lot.get(),
                                   self.NoOftablets.get(),
                                   self.Dose.get(),
                                   self.issuedate.get(),
                                   self.expdate.get(),
                                   self.Dailydose.get(),
                                   self.SideEffect.get(),
                                   self.Furtherinfo.get(),
                                   self.Bloodpressure.get(),
                                   self.Storage.get(),
                                   self.Medicine.get(),
                                   self.PatientId.get(),
                                   self.NhsNumber.get(),
                                   self.Patientname.get(),
                                   self.PatientAddress.get(),
                                   self.DateOfBirth.get()

                               ))
             conn.commit()
             conn.close()
        













root=Tk()
ob=Hospital(root)
root.mainloop()

