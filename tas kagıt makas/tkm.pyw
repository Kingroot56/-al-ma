# -*- coding: utf-8 -*
#import os
from tkinter import *

from time import sleep
import random
from PIL.ImageTk import PhotoImage

son_makine=0
son_siz=0
makine_isaret="                          "
oyuncu_isaret="                          "
liste=["TAŞ","KAGIT","MAKAS"]
pencere = Tk()
pencere.title("TAS KAGIT MAKAS")
pencere.geometry("600x500")
#pencere.resizable(width=FALSE, height=FALSE)
img1=PhotoImage(file="tas.gif")
img2=PhotoImage(file="kagit.gif")
img3=PhotoImage(file="makas.gif")
img4=PhotoImage(file="bos.gif")
def tas_button():
    global makine_isaret,oyuncu_isaret,img1,img2,img3,img4
    makine_isaret="                          "
    oyuncu_isaret="                          "
    makine_hareket=Label(text=makine_isaret,image=img4).place(relx="0.685",rely="0.4")
    oyuncu_hareket=Label(text=oyuncu_isaret,image=img4).place(relx="0.240",rely="0.4")
    v=random.choice(liste)
    makine_isaret=v
    secim="TAŞ"
    oyuncu_isaret=secim
    if secim==v:
        makine_hareket=Label(image=img1).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img1).place(relx="0.240",rely="0.4")
    elif v=="MAKAS":
        sonuc_sizi()
        makine_hareket=Label(image=img3).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img1).place(relx="0.240",rely="0.4")
        winner()
    elif v == "KAGIT":
        sonuc_makinee()
        makine_hareket=Label(image=img2).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img1).place(relx="0.240",rely="0.4")
        winner()
def kagit_button():
    global makine_isaret,oyuncu_isaret,img1,img2,img3,img4
    makine_isaret="                          "
    oyuncu_isaret="                          "
    makine_hareket=Label(text=makine_isaret,fg="red").place(relx="0.685",rely="0.4")
    oyuncu_hareket=Label(text=oyuncu_isaret,fg="red").place(relx="0.240",rely="0.4")
    v=random.choice(liste)
    makine_isaret=v
    secim="KAGIT"
    oyuncu_isaret=secim
    if secim==v:
        makine_hareket=Label(image=img2).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img2).place(relx="0.240",rely="0.4")
    elif v=="MAKAS":
        sonuc_makinee()
        makine_hareket=Label(image=img3).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img2).place(relx="0.240",rely="0.4")
        winner()
    elif v == "TAŞ":
        sonuc_sizi()
        makine_hareket=Label(image=img1).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img2).place(relx="0.240",rely="0.4")
        winner()
def makas_button():
    global makine_isaret,oyuncu_isaret,img1,img2,img3,img4
    makine_isaret="                          "
    oyuncu_isaret="                          "
    makine_hareket=Label(image=img4).place(relx="0.685",rely="0.4")
    oyuncu_hareket=Label(image=img4).place(relx="0.240",rely="0.4")
    v=random.choice(liste)
    makine_isaret=v
    secim="MAKAS"
    oyuncu_isaret=secim
    if secim==v:
        makine_hareket=Label(image=img3).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img3).place(relx="0.240",rely="0.4") 
    elif v=="TAŞ":
        sonuc_makinee()
        makine_hareket=Label(image=img1).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img3).place(relx="0.240",rely="0.4")
        winner()
    elif v == "KAGIT":
        sonuc_sizi()
        makine_hareket=Label(image=img2).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img3).place(relx="0.240",rely="0.4")
        winner()
def sonuc_sizi():
    global son_siz
    son_siz = son_siz + 1
    score=Label(pencere,text=son_siz).place(relx="0.0889",rely="0.1")
def sonuc_makinee():
    global son_makine
    son_makine+=1
    score2=Label(pencere,text=son_makine).place(relx="0.889",rely="0.1")
def mak():
    pass
def winner():
    global son_siz,son_makine,makine_isaret,oyuncu_isaret
    if son_makine==5:
        makine_isaret="                          "
        oyuncu_isaret="                          "
        msb.showinfo(title="KAZANAN",message="MAKİNE")
        son_siz=0
        son_makine=0
        score=Label(pencere,text=son_siz).place(relx="0.0889",rely="0.1")
        score2=Label(pencere,text=son_makine).place(relx="0.889",rely="0.1")
        makine_hareket=Label(image=img4).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img4).place(relx="0.240",rely="0.4")
    elif son_siz==5:
        makine_isaret="                          "
        oyuncu_isaret="                          "
        msb.showinfo(title="KAZANAN",message="OYUNCU ")
        son_siz=0
        son_makine=0
        score=Label(pencere,text=son_siz).place(relx="0.0889",rely="0.1")
        score2=Label(pencere,text=son_makine).place(relx="0.889",rely="0.1")
        makine_hareket=Label(image=img4).place(relx="0.685",rely="0.4")
        oyuncu_hareket=Label(image=img4).place(relx="0.240",rely="0.4")
puan=Label(text="SİZ=").place(relx="0.05",rely="0.1")
puan2=Label(text="MAKİNE=").place(relx="0.8",rely="0.1")
score=Label(pencere,text=son_siz,fg="green").place(relx="0.0889",rely="0.1")
score2=Label(pencere,text=son_makine,fg="red").place(relx="0.889",rely="0.1")
makine=Label(text="MAKİNENİN İŞARETİ:",fg="red").place(relx="0.485",rely="0.4")
makine_hareket=Label(image=img4).place(relx="0.685",rely="0.4")
oyuncu=Label(text="SİZİN İŞARETİNİZ:",fg="green").place(relx="0.055",rely="0.4")
oyuncu_hareket=Label(image=img4).place(relx="0.240",rely="0.4")
tas_butt=Button(pencere,text="TAŞ",command=tas_button).place(relx="0.1",rely="0.8")
kagit_butt=Button(pencere,text="KAĞIT",command=kagit_button).place(relx="0.4",rely="0.8")
makas_butt=Button(pencere,text="MAKAS",command=makas_button).place(relx="0.7",rely="0.8")
pencere.mainloop()