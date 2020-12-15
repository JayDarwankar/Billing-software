from tkinter import *
import math, random,os
from tkinter import messagebox
import time


class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1360x720+0+0")
        self.root.title("LAXMI GENERAL STORES BILLING SOFTWARE".center(395))
        bg_color= "maroon4"
        title = Label(self.root,text="Laxmi Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        Label(self.root, text="Jay darwankar",font="arial 18 bold",fg="white").pack()
        #=============variables===========

        #===========cosmetics==============
        self.hair = IntVar()
        self.wash = IntVar()
        self.cream = IntVar()
        self.spray = IntVar()
        self.lipstick = IntVar()
        self.nail = IntVar()

        #=============stationary============
        self.book = IntVar()
        self.pen = IntVar()
        self.box = IntVar()
        self.basket = IntVar()
        self.bag = IntVar()
        self.cover = IntVar()

        #=============child items=============

        self.doll = IntVar()
        self.train = IntVar()
        self.puzzle = IntVar()
        self.sticker = IntVar()
        self.toy = IntVar()
        self.colour = IntVar()

        #=======Total price and tax=========

        self.cosmetics_price = StringVar()
        self.stationary_price = StringVar()
        self.child_price = StringVar()

        self.cosmetics_tax = StringVar()
        self.stationary_tax = StringVar()
        self.child_tax = StringVar()

        #==========customers-===============

        self.name = StringVar()
        self.phone = StringVar()
        self.bill = StringVar()
        x = random.randint(10000, 99999)
        self.bill.set(str(x))
        self.search = StringVar()


  ##customers frames

        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="arial 15", textvariable=self.name, bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, font="arial 15", bd=7,textvariable=self.phone, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, font="arial 15", bd=7,textvariable=self.search, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,font="arial 12 bold",bd=7).grid(row=0,column=6,pady=10,padx=10)
        print_btn=Button(F1,text="Print",command=self.iprint, width=10,font="arial 12 bold",bd=7).grid(row=0,column=7,pady=10,padx=10)


        ######cosmetics section

        F2 = LabelFrame(self.root, text="Cosmetics section", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=0, y=180, width=325,height=380)

        bath_lbl=Label(F2,text="Hair oil",font=("times new roman", 16, "bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font=("times new roman", 16, "bold"),bd=5,textvariable=self.hair,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        face_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.wash, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        Facial_lbl = Label(F2, text="Facial cream", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Facial_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.cream, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        body_lbl = Label(F2, text="Body Spray", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.spray, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)
        lip_lbl = Label(F2, text="Lipstick", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        lip_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.lipstick,relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)
        nail_lbl = Label(F2, text="Nail paint", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        nail_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.nail, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)
  ########Stationary items
        F3 = LabelFrame(self.root, text="Stationary Items", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=330, y=180, width=325, height=380)

        books = Label(F3, text="Drawing Books", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        books = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.book,relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        gel = Label(F3, text="Gel Pen", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        gel = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.pen, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        compass = Label(F3, text="Compass Box", font=("times new roman", 16, "bold"), fg="lightgreen",
                           bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        compass = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.box, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        basket = Label(F3, text="Tiffin basket", font=("times new roman", 16, "bold"), fg="lightgreen",
                         bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        basket = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.basket, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)
        school = Label(F3, text="School bags", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        school = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.bag, relief=SUNKEN).grid(row=4, column=1,
                                                                                                      padx=10, pady=10)
        cover = Label(F3, text="Books cover", font=("times new roman", 16, "bold"), fg="lightgreen",
                         bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        cover = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.cover, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        ###Child items

        F4 = LabelFrame(self.root, text="Child Items", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=660, y=180, width=325, height=380)

        doll = Label(F4, text="Baby Doll", font=("times new roman", 16, "bold"), fg="lightgreen",
                      bg=bg_color).grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        doll = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.doll, relief=SUNKEN).grid(row=0, column=1,
                                                                                                    padx=10, pady=10)

        train = Label(F4, text="Train", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        train = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.train, relief=SUNKEN).grid(row=1, column=1,
                                                                                                  padx=10, pady=10)

        puzzle = Label(F4, text="Puzzles", font=("times new roman", 16, "bold"), fg="lightgreen",
                        bg=bg_color).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        puzzle = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.puzzle, relief=SUNKEN).grid(row=2,
                                                                                                      column=1,
                                                                                                      padx=10,
                                                                                                      pady=10)

        sticker = Label(F4, text="Cartoon stickers", font=("times new roman", 16, "bold"), fg="lightgreen",
                       bg=bg_color).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        sticker = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.sticker, relief=SUNKEN).grid(row=3, column=1,
                                                                                                     padx=10, pady=10)
        cartoon  = Label(F4, text="Cartoon toys", font=("times new roman", 16, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        cartoon = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.toy, relief=SUNKEN).grid(row=4, column=1,
                                                                                                     padx=10, pady=10)
        paint = Label(F4, text="Painting colours", font=("times new roman", 16, "bold"), fg="lightgreen",
                      bg=bg_color).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        paint = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.colour, relief=SUNKEN).grid(row=5, column=1,
                                                                                                    padx=10, pady=10)
        ##Bill area

        F5 =Frame(self.root, bd=10, relief=GROOVE,)
        F5.place(x=990, y=180, width=350, height=380)

        bill_title=Label(F5,text="Bill Area",font=("arial", 15, "bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #####Bill menu

        F6=LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                   fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=160)


        ## over all total


        m1_lbl=Label(F6,text="Total Cosmetics Price",font=("times new roman", 15, "bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,bd=7,textvariable=self.cosmetics_price,font="arial 10 bold",relief=SUNKEN,width=18).grid(row=0,column=1,padx=10,pady=2)

        m2_lbl = Label(F6, text="Total Stationary Price", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, bd=7,textvariable=self.stationary_price, font="arial 10 bold", relief=SUNKEN, width=18).grid(row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text="Total Child Items", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, bd=7,textvariable=self.child_price, font="arial 10 bold", relief=SUNKEN, width=18).grid(row=2, column=1, padx=10, pady=2)

        ####Total tax

        t1_lbl = Label(F6, text="Cosmetics Tax", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(F6, bd=7,textvariable=self.cosmetics_tax, font="arial 10 bold", relief=SUNKEN, width=18).grid(row=0, column=3, padx=10, pady=2)

        t2_lbl = Label(F6, text="Stationary Tax", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(F6, bd=7,textvariable=self.stationary_tax, font="arial 10 bold", relief=SUNKEN, width=18).grid(row=1, column=3, padx=10, pady=2)

        t3_lbl = Label(F6, text="Child Tax", font=("times new roman", 15, "bold"), bg=bg_color,
                       fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(F6, bd=7,textvariable=self.child_tax, font="arial 10 bold", relief=SUNKEN, width=18).grid(row=2, column=3, padx=10, pady=2)


        ###button frame

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",font="arial 13 bold",bg="cadetblue",fg="white",bd=5,pady=15,width=11).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_f,command=self.Bill_area, text="Generate Bill", font="arial 13 bold", bg="cadetblue", fg="white", bd=5, pady=15,
                       width=11).grid(row=0, column=1, padx=5,pady=5)
        clear_btn = Button(btn_f,command=self.clear_data, text="Clear Data", font="arial 13 bold", bg="cadetblue", fg="white", bd=5, pady=15,
                       width=11).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f, text="Exit",command=self.exit_app, font="arial 13 bold", bg="cadetblue", fg="white", bd=5, pady=15,
                       width=11).grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()
    def total(self):
        self.hair_price =(self.hair.get() * 50)
        self.wash_price=(self.wash.get() * 75)
        self.cream_price=(self.cream.get() * 30)
        self.spray_price=(self.spray.get() * 150)
        self.lipstick_price=(self.lipstick.get() * 150)
        self.nail_price=(self.nail.get() * 100)

        self.total_cosmetics_price = float(
                 self.hair_price +
                 self.wash_price +
                 self.cream_price +
                 self.spray_price +
                 self.lipstick_price +
                 self.nail_price
        )
        self.cosmetics_price.set("Rs. "+ str(self.total_cosmetics_price))
        self.cos_tax=round((self.total_cosmetics_price*0.05), 2)
        self.cosmetics_tax.set("Rs. "+str(self.cos_tax))


        self.book_price=(self.book.get() * 30)
        self.pen_price=(self.pen.get() * 20)
        self.box_price=(self.box.get() * 50)
        self.basket_price=(self.basket.get() * 60)
        self.bag_price=(self.bag.get() * 350)
        self.cover_price=(self.cover.get() * 45)

        self.total_stationary_price = float(
                self.book_price +
                self.pen_price +
                self.box_price +
                self.basket_price +
                self.bag_price +
                self.cover_price
        )
        self.stationary_price.set("Rs. "+ str(self.total_stationary_price))
        self.s_tax=round((self.total_stationary_price * 0.05), 2)
        self.stationary_tax.set("Rs. " + str(self.s_tax))


        self.doll_price=(self.doll.get() * 250)
        self.train_price=(self.train.get() * 1155)
        self.puzzle_price=(self.puzzle.get() * 150)
        self.sticker_price=(self.sticker.get() * 50)
        self.toy_price=(self.toy.get() * 200)
        self.colour_price=(self.colour.get() * 100)


        self.total_child_price = float(
                self.doll_price +
                self.train_price +
                self.puzzle_price +
                self.sticker_price +
                self.toy_price +
                self.colour_price
        )
        self.child_price.set("Rs. "+ str(self.total_child_price))
        self.c_tax=round((self.total_child_price * 0.05), 2)
        self.child_tax.set("Rs. " + str(self.c_tax))

        self.over_all_total=float(self.total_cosmetics_price +
                                  self.total_stationary_price +
                                  self.total_child_price +
                                  self.cos_tax +
                                  self.s_tax +
                                  self.c_tax
                                  )
    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END,"    Welcome to Laxmi General Stores\n")
        self.textarea.insert(END, f"\n Shop Owner Name: Vilas Darwankar")
        self.textarea.insert(END, f"\n Bill Number: {self.bill.get()} ")
        self.textarea.insert(END, f"\n Customer Name: {self.name.get()}")
        self.textarea.insert(END, f"\n Phone Number: {self.phone.get()}")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Products\t\tQuantity\t\tPrice")
        self.textarea.insert(END, f"\n======================================")
    def Bill_area(self):
        if self.name.get() == "" or self.phone.get() == "":
            messagebox.showerror("Error","Customer details are mandatory")

        elif self.cosmetics_price.get()=="Rs. 0.0" and self.stationary_price.get()=="Rs. 0.0" and self.child_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product has been selected")

        else:
            self.welcome_bill()
            # =====cosmetics========
            if self.hair.get() != 0:
                self.textarea.insert(END, f"\n Hair oil\t\t{self.hair.get()}\t\t{self.hair_price}")
            if self.wash.get() != 0:
                self.textarea.insert(END, f"\n Face wash\t\t{self.wash.get()}\t\t{self.wash_price}")
            if self.cream.get() != 0:
                self.textarea.insert(END, f"\n Facial cream\t\t{self.cream.get()}\t\t{self.cream_price}")
            if self.spray.get() != 0:
                self.textarea.insert(END, f"\n Body Spray\t\t{self.spray.get()}\t\t{self.spray_price}")
            if self.lipstick.get() != 0:
                self.textarea.insert(END, f"\n Lipstick\t\t{self.lipstick.get()}\t\t{self.lipstick_price}")
            if self.nail.get() != 0:
                self.textarea.insert(END, f"\n Nail paint\t\t{self.nail.get()}\t\t{self.nail_price}")

            # ==============stationary=========

            if self.book.get() != 0:
                self.textarea.insert(END, f"\n Drawing Books\t\t{self.book.get()}\t\t{self.book_price}")
            if self.pen.get() != 0:
                self.textarea.insert(END, f"\n Gel Pen\t\t{self.pen.get()}\t\t{self.pen_price}")
            if self.box.get() != 0:
                self.textarea.insert(END, f"\n Compass Box\t\t{self.box.get()}\t\t{self.box_price}")
            if self.basket.get() != 0:
                self.textarea.insert(END, f"\n Tiffin Basket\t\t{self.basket.get()}\t\t{self.basket_price}")
            if self.bag.get() != 0:
                self.textarea.insert(END, f"\n School bag\t\t{self.bag.get()}\t\t{self.bag_price}")
            if self.cover.get() != 0:
                self.textarea.insert(END, f"\n Books cover\t\t{self.cover.get()}\t\t{self.cover_price}")

            # ===================child item=======

            if self.doll.get() != 0:
                self.textarea.insert(END, f"\n Baby Doll\t\t{self.doll.get()}\t\t{self.doll_price}")
            if self.train.get() != 0:
                self.textarea.insert(END, f"\n Train\t\t{self.train.get()}\t\t{self.train_price}")
            if self.puzzle.get() != 0:
                self.textarea.insert(END, f"\n Puzzles\t\t{self.puzzle.get()}\t\t{self.puzzle_price}")
            if self.sticker.get() != 0:
                self.textarea.insert(END, f"\n Cartoon Stickers\t\t{self.sticker.get()}\t\t{self.sticker_price}")
            if self.toy.get() != 0:
                self.textarea.insert(END, f"\n Cartoon Toy\t\t{self.toy.get()}\t\t{self.toy_price}")
            if self.colour.get() != 0:
                self.textarea.insert(END, f"\n Painting colours\t\t{self.colour.get()}\t\t{self.colour_price}")

            self.textarea.insert(END, f"\n--------------------------------------")
            if self.cosmetics_tax.get() != "Rs.0.0":
                self.textarea.insert(END, f"\nCosmetics Tax:\t\t\t {self.cosmetics_tax.get()}")
            if self.stationary_tax.get() != "Rs.0.0":
                self.textarea.insert(END, f"\nStationary Tax:\t\t\t {self.stationary_tax.get()}")
            if self.child_tax.get() != "Rs.0.0":
                self.textarea.insert(END, f"\nChild tax:\t\t\t {self.child_tax.get()}")
            self.textarea.insert(END, f"\n--------------------------------------")

            self.textarea.insert(END, f"\nTotal Amount:\t\t\tRs.{self.over_all_total}")
            self.save_bill()

    def save_bill(self):
        s=messagebox.askyesno("Save Bill", "Would u like to save the current bill")
        if s>0:
            self.bill_data=self.textarea.get("1.0", END)
            f1=open("bills/"+str(self.bill.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"{self.name.get()} bill has saved successfully")
        else:
            return

    def find_bill(self):
        present="yes"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="no"
        if present=="yes":
            messagebox.showerror("Error","Invalid bill number please check your Bill number")

    def clear_data(self):
        c=messagebox.askyesno("Clear","Do u really want to clear the data?")
        if c>0:
            self.hair.set(0)
            self.wash.set(0)
            self.cream.set(0)
            self.spray.set(0)
            self.lipstick.set(0)
            self.nail.set(0)

            # =============stationary============
            self.book.set(0)
            self.pen.set(0)
            self.box.set(0)
            self.basket.set(0)
            self.bag.set(0)
            self.cover.set(0)

            # =============child items=============

            self.doll.set(0)
            self.train.set(0)
            self.puzzle.set(0)
            self.sticker.set(0)
            self.toy.set(0)
            self.colour.set(0)

            # =======Total price and tax=========

            self.cosmetics_price.set("")
            self.stationary_price.set("")
            self.child_price.set("")

            self.cosmetics_tax.set("")
            self.stationary_tax.set("")
            self.child_tax.set("")

            # ==========customers-===============

            self.name.set("")
            self.phone.set("")
            self.bill.set("")
            x = random.randint(10000, 99999)
            self.bill.set(str(x))
            self.search.set("")
            self.welcome_bill()
        else:
            return

    def exit_app(self):
        m=messagebox.askyesno("Exit", "Do you really want to exit?")
        if m>0:
            self.root.destroy()

    def iprint(self):
        q=self.textarea.get('1.0',END)
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")

root=Tk()
obj= Bill_App(root)
root.mainloop()