from tkinter import*
import random
from tkinter import messagebox
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    'terrestrial',
    'mamals',
    'ambassador',
    'ambidextrous',
    'frugality',
    'frustration',
    'furthest',
    'gardening',
    'perpendicular',
    'valuables',
    'medicate',
    'permission',
    'rainbow',
    'seeming',
    'syringe',
    'valuation',
    'pronunciation',
    'incarnation',
    'incognito',
    'factorize',
    'youngester',
    'zoology',
    'zoologist',
    'yearning',
    'wretched',
    'winding',
    'vacation',
    'tombstone',
    'somatic',
    'vegetation',
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    'resltetriar',
    'asmalm',
    'assramadob',
    'idexmastroub',
    'garfylitu',
    'strnfratiou',
    'thuftesr',
    'deaggninr',
    'pendepricular',
    'uaavsblel',
    'icemeatd',
    'misnpesior',
    'nwraboi',
    'mgseine',
    'iesyngr',
    'uaavntiol',
    'nuncrpniatioo',
    'arnninatioc',
    'ognionitc',
    'toaferizc',
    'ngeryosteu',
    'lyzoogo',
    'looztgiso',
    'rneygina',
    'tcrwdhee',
    'dgwiinn',
    'atavnioc',
    'bsotetonm',
    'acsotim',
    'etanvetiog',
]
num=random.randrange(0,len(words),1)
def default():
    global words,answers,num
    l1.configure(text=words[num])
def res():
    global words,answers,num
    num=random.randrange(0,len(words),1)
    l1.config(text=words[num])
    e1.delete(0,END)
def checkans():
    global words,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo(title="Result",message="Success,this is right answer")
        res()
    else:
        messagebox.showerror(title="Result",message="Incorrect")
        e1.delete(0,END)
window=Tk()
window.geometry("350x400+400+300")
window.title("Jumbble Game")
window.configure(bg="#000000")
l1=Label(window,text="Your Text Here",
         font=("bold",18),
         bg="#000000",
         fg="white"
         )
l1.pack(pady=30,ipady=10,ipadx=10)
ans1=StringVar()
e1=Entry(window,
         font=("bold",16),
         textvariable=ans1,
         )
e1.pack(ipady=5,ipadx=5)
bt=Button(window,
          text="Check",
          font=("Comic sans ms",16),
          width=16,
          bg="green",
          fg="white",
          relief=GROOVE,
          command=checkans
          )
bt.pack(pady=40)
bt1=Button(window,
          text="Reset",
          font=("Comic sans ms",16),
          width=16,
          bg="red",
          fg="white",
          relief=GROOVE,
          command=res
          )
bt1.pack()
default()
window.mainloop()
