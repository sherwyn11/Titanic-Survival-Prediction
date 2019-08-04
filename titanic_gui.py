from tkinter import *
import tkinter.ttk as tk
import tkinter.messagebox
import Titanic_survival_ml as tml

master = Tk()
master.title("Titanic Survival Probability")

def main():

    w = Frame(master,pady=20,padx=20)
    title = Label(w, text = 'Let\'s see if you\'d survive the Titanic') 

    def popup(msg):
        popup = Tk()
        popup.title("Titanic Survival Probability")
        popup.geometry('400x100')
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B = Button(popup, text="Ok", command = quit)
        B.pack()

    def check():
        data = []
        data.append(int(age.get()))
        if(t_choose.current()+1 == 1):
            data.append(90)
        elif(t_choose.current()+1 == 2):
            data.append(40)
        else:
            data.append(10)
        data.append(g_choose.current()+1)
        data.append(int(nos.get()))
        data.append(int(nop.get()))
        data.append(t_choose.current()+1)
        data.append(e_choose.current()+1)
        print(data)
        pred_prob = tml.survival([data])
        print("Predicted",pred_prob)
        popup(f'Probability of survival would be {pred_prob}%')



    name = Label(w, text = 'First Name') 
    Age = Label(w,text = 'Age')
    Gender = Label(w,text = 'Gender')
    g_choose = tk.Combobox(w, state = 'readonly')
    g_choose['values']= ("Male", "Female")
    g_choose.current(0)
    tclass = Label(w,text = 'Class')  
    t_choose = tk.Combobox(w, state = 'readonly')
    t_choose['values']= ("1st Class", "2nd Class", "3rd Class")
    t_choose.current(0)
    noS = Label(w,text = 'No of siblings/spouses aboard')
    noP = Label(w,text = 'No of parents/children aboard')
    eclass = Label(w,text = 'Embarked')  
    e_choose = tk.Combobox(w, state = 'readonly')
    e_choose['values']= ("Cherbourg","Queenstown","Southampton")
    e_choose.current(0)
    button = Button(w,text = "Predict",pady = 10,padx = 10,command = check)

    e1 = Entry(w) 
    age = IntVar()
    e2 = Entry(w,textvariable = age)
    nos = IntVar()
    e4 = Entry(w,textvariable = nos)
    nop = IntVar()
    e5 = Entry(w,textvariable = nop)

    title.pack()
    name.pack()
    e1.pack()
    Age.pack()
    e2.pack()
    Gender.pack()
    g_choose.pack()
    tclass.pack()
    t_choose.pack() 
    noS.pack()
    e4.pack()
    noP.pack()
    e5.pack()
    eclass.pack()
    e_choose.pack()
    button.pack()
    w.pack()

    master.mainloop()

main()