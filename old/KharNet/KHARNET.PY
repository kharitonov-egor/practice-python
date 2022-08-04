from tkinter import *
import pickle
from time import sleep
from tkinter import messagebox
from math import *
import webbrowser
from tkinter import ttk
import math
import sys

#Социальная сеть от Егора Харитонова)
# I tried to replicate VKontakte in spring of 2019. 

sleep(1)
print('KharNet')
sleep(0.5)
print('Загрузка...')
sleep(1)

root=Tk()
root.geometry("960x540+480+270")
root.title("KharNet")

log_b = Button(root, font="Tahoma 10", text = "Войти", width="17",cursor="hand2",command=lambda: log()).place(x=51,y=30)
reg_b = Button(root, font="Tahoma 10", text="Зарегистрироваться",cursor="hand2", command=lambda: reg()).place(x=50,y=60)
kn_b_root = Button(root, font="Tahoma 10", text="KharNet 2019",fg='blue' ,bd=0,cursor="hand2", command=lambda: kharnet()).place(x=50,y=510)
welc_root = Label(root,font="Tahoma 15",text="Добро пожаловать!").place(x=446,y=20)
nov_l_root = Label(root, font="Tahoma 15", text="Новость:").place(x=200,y=60)
beta_s_l = Label(root, font="Tahoma 15", text="Вышла версия 1.0.2!").place(x=290,y=60)
beta_s2_l = Label(root, font="Tahoma 10", text="Был добавлен калькулятор.").place(x=290,y=90)
version = Label(root, font="Tahoma 10", text="Версия 1.0.1").place(x=850,y=510)


def kharnet():
    kharnet=Tk()
    kharnet.title("KharNet")
    kharnet.geometry("960x540+480+270")

    def_kharnet = Label(kharnet,text="Что такое KharNet?",font="Tahoma 15 bold").place(x=20,y=20)
    def2_kharnet = Label(kharnet,text="KharNet - это социальная сеть,созданная на языке Python.",font="Tahoma 11").place(x=20,y=50)
    kom_kharnet = Label(kharnet,text="Немного о нас:",font="Tahoma 15 bold").place(x=20,y=80)
    def callback(event):
        webbrowser.open_new("https://vk.com/ega.khar")
    kom2_kharnet = Label(kharnet,text="Программист - Егор Харитонов",font="Tahoma 11",fg="blue", cursor="hand2")
    kom2_kharnet.place(x=20,y=110)
    kom2_kharnet.bind("<Button-1>", callback)

    def callback2(event):
        webbrowser.open_new("https://vk.com/id264232662")
    kom3_kharnet = Label(kharnet, text="Тестер - Алексей Черненко", font="Tahoma 11",fg="blue",cursor="hand2")
    kom3_kharnet.place(x=20,y=140)
    kom3_kharnet.bind("<Button>", callback2)

def reg():
    reg=Tk()
    reg.geometry("960x540+480+270")
    reg.title("Регистрация")

    text_log = Label(reg,font="Tahoma 10",text="Введите ваш логин:").place(x=20,y=20)
    registr_lodin = Entry(reg,font="Tahoma 10")
    text_password1 = Label(reg,font="Tahoma 10",text="Введите свой пароль:").place(x=20,y=60)
    registr_password1 = Entry(reg,font="Tahoma 10")
    text_password2 = Label(reg,font="Tahoma 10",text="Еще раз пароль:").place(x=20,y=100)
    registr_password2 = Entry(reg,font="Tahoma 10",show="*")
    button_registr = Button(reg,font="Tahoma 10",text="Зарегистрироваться!",cursor="hand2", command=lambda: save()).place(x=20,y=145)

    registr_lodin.place(x=20,y=40)
    registr_password1.place(x=20,y=80)
    registr_password2.place(x=20,y=120)

    welc_reg = Label(reg,font="Tahoma 15",text="Добро пожаловать!").place(x=446,y=20)
    nov_l_reg = Label(reg, font="Tahoma 15", text="Новость:").place(x=200,y=60)
    beta_s_reg = Label(reg, font="Tahoma 15", text="Вышла версия 1.0.2!").place(x=290,y=60)
    beta_s2_reg = Label(reg, font="Tahoma 10", text="Был добавлен калькулятор.").place(x=290,y=90)
    kn_b_reg = Button(reg, font="Tahoma 10", text="KharNet 2019",cursor="hand2",fg='blue' ,bd=0, command=lambda: kharnet()).place(x=50,y=510)
    version_reg = Label(reg, font="Tahoma 10", text="Версия 1.0.1").place(x=850,y=510)

    def save():
        login_pass_save = {}
        login_pass_save[registr_lodin.get()]=registr_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        log()

def log():
    log=Tk()
    log.geometry("960x540+480+270")
    log.title("Вход")

    text_enter_login = Label(log, font="Tahoma 10", text="Введите логин:").place(x=20,y=40)
    enter_login = Entry(log, font="Tahoma 10")
    text_enter_pass = Label(log, font="Tahoma 10", text="Введите ваш пароль:").place(x=20,y=80)
    enter_password = Entry(log, font="Tahoma 10", show="*")
    button_enter = Button(log, font="Tahoma 10", text="Войти",cursor="hand2",command=lambda: log_pass()).place(x=20,y=125)

    enter_login.place(x=20,y=60)
    enter_password.place(x=20,y=100)

    welc_log = Label(log,font="Tahoma 15",text="Здравствуйте,ещё раз!").place(x=446,y=20)
    nov_l_log = Label(log, font="Tahoma 15", text="Новость:").place(x=200,y=60)
    beta_s_log = Label(log, font="Tahoma 15", text="Вышла версия 1.0.2!").place(x=290,y=60)
    beta_s2_log = Label(log, font="Tahoma 10", text="Был добавлен калькулятор.").place(x=290,y=90)
    kn_b_log = Button(log, font="Tahoma 10", text="KharNet 2019",fg='blue' ,cursor="hand2",bd=0, command=lambda: kharnet()).place(x=50,y=510)
    version_log= Label(log, font="Tahoma 10", text="Версия 1.0.1").place(x=850,y=510)

    def log_pass():
        f = open("login.txt" , "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                programma()
            else:
                messagebox.showerror("Ошибка!", "Вы ввели неверный логин или пароль")
        else:
            messagebox.showerror("Ошибка!", "Вы ввели неверный логин.")

def programma():
    def kvadr():
        def onetime():
            onetime=Tk()
            onetime.title("Может ещё раз?")
            onetime.geometry("480x270+720+405")

            one_but = Button(onetime, text="Да", font="Tahoma 15 bold", command=lambda: kvadr()).place(x=220,y=100)

            onetime.mainloop()
        print('Программа для решений квадратных уравнений.')
        sleep(1)
        print('Введите коэф. a')
        a=input()
        print('Введите коэф. b')
        b=input()
        print('Введите коэф. c')
        c=input()

        a=float(a)
        b=float(b)
        c=float(c)

        D=(b**2)-(4*a*c)
        D=float(D)

        if D<0:
            print('Решений нет - D<0')
            sleep(1.5)
            onetime()
        if D==0:
            x=(-b)/(2*a)
            print('----------------------')
            print('Ваш корень:')
            print(x)
            sleep(4)
            onetime()
        if D>0:
            y=(-b+sqrt(D))/(2*a)
            z=(-b-sqrt(D))/(2*a)
            print('----------------------')
            print('Ваши корни:')
            print(y)
            print(z)
            sleep(5)
            onetime()
    def calc2():
        #Код с сайта https://habr.com/ru/

        root = Tk()
        root.title("Калькулятор")
        root.geometry("280x180+120+510")

        bttn_list = [
        "7", "8", "9", "+",
        "4", "5", "6","*",
        "1", "2", "3","-",
        "(","0",")","/","xⁿ",
        "±",".", "=",  "C"]


        r = 1
        c = 0
        for i in bttn_list:
            rel = ""
            cmd=lambda x=i: calc(x)
            ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
            c += 1
            if c >= 4:
                c = 0
                r += 1

        calc_entry = Entry(root, width = 33)
        calc_entry.grid(row=0, column=0, columnspan=5)

        #логика калькулятора
        def calc(key):
            global memory
            if key == "=":
        #исключение написания слов
                str1 = "-+0123456789.*/)("
                if calc_entry.get()[0] not in str1:
                    calc_entry.insert(END, "Первый символ - не цифра!")
                    messagebox.showerror("Ошибка!", "Вы не ввели номер!")
        #исчисления
                try:
                    result = eval(calc_entry.get())
                    calc_entry.insert(END, "=" + str(result))
                except:
                    calc_entry.insert(END, "Ошибка!")
                    messagebox.showerror("Ошибка!", "Проверьте правильность данных")

        #очищение поля ввода

            elif key == "C":
                calc_entry.delete(0, END)
            elif key == "±":
                if "=" in calc_entry.get():
                    calc_entry.delete(0, END)
                try:
                    if calc_entry.get()[0] == "-":
                        calc_entry.delete(0)
                    else:
                        calc_entry.insert(0, "-")
                except IndexError:
                    pass
            elif key == "Exit":
                root.after(1,root.destroy)
                sys.exit
            elif key == "xⁿ":
                calc_entry.insert(END, "**")
            elif key == "(":
                calc_entry.insert(END, "(")
            elif key == ")":
                calc_entry.insert(END, ")")
            else:
                if "=" in calc_entry.get():
                    calc_entry.delete(0, END)
                calc_entry.insert(END, key)
        root.mainloop()

    proga=Tk()
    proga.geometry("960x540+480+270")
    proga.title("KharNet")
    sinka=Button(proga, state="disable",bg="#4a76a8",bd=0).place(x=0,y=0,height=45,width=960)
    kharnet_logo = Label(proga, text="KharNet", font="Arial 25 bold", bg="#4a76a8",fg="white").place(x=430,y=1)


    bl1 = Button(proga,bg="black",state="disable").place(x=120,y=0,height=540,width=1)
    bl2 = Button(proga,bg="black",state="disable").place(x=840,y=0,height=540,width=1)


    fun1 = Button(proga,text="Решение квадратных уравнений", font="Tahoma 10", command=lambda: kvadr()).place(x=161,y=400)
    fun2 = Button(proga,text="Калькулятор", font="Tahoma 10", command=lambda: calc2()).place(x=161,y=410)

    

    proga.mainloop()



root.mainloop()
