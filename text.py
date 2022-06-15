from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Heart Diagnosis Report")
root.geometry("400x400")
root.configure(background = "white")

Question_1_Radio_Button = StringVar(value = 0)

Question_1 = Label(root, text = "Do you experience shortness of breath during regular routine activities?", bg = "black", fg = "white")
Question_1.pack()
Question_1_r1 = Radiobutton(root, text = "Yes", variable = Question_1_Radio_Button, value = "Yes", bg = "black", fg = "white")
Question_1_r1.pack()
Question_1_r2 = Radiobutton(root, text = "No", variable = Question_1_Radio_Button, value = "No", bg = "black", fg = "white")
Question_1_r2.pack()

Question_2_Radio_Button = StringVar(value = 0)

Question_2 = Label(root, text = "Do you have swelling in the feet, ankles, legs (shoes feel tighter), or abdomen?", bg = "black", fg = "white")
Question_2.pack()
Question_2_r1 = Radiobutton(root, text = "Yes", variable = Question_2_Radio_Button, value = "Yes", bg = "black", fg = "white")
Question_2_r1.pack()
Question_2_r2 = Radiobutton(root, text = "No", variable = Question_2_Radio_Button, value = "No", bg = "black", fg = "white")
Question_2_r2.pack()

Question_3_Radio_Button = StringVar(value = 0)

Question_3 = Label(root, text = "Do you feel any of these symtoms - confusion, disorientation, or loss of memory?", bg = "black", fg = "white")
Question_3.pack()
Question_3_r1 = Radiobutton(root, text = "Yes", variable = Question_3_Radio_Button, value = "Yes", bg = "black", fg = "white")
Question_3_r1.pack()
Question_3_r2 = Radiobutton(root, text = "No", variable = Question_3_Radio_Button, value = "No", bg = "black", fg = "white")
Question_3_r2.pack()

Question_4_Radio_Button = StringVar(value = 0)

Question_4 = Label(root, text = "Do you experience shortness of breath while at rest (lying down)?", bg = "black", fg = "white")
Question_4.pack()
Question_4_r1 = Radiobutton(root, text = "Yes", variable = Question_4_Radio_Button, value = "Yes", bg = "black", fg = "white")
Question_4_r1.pack()
Question_4_r2 = Radiobutton(root, text = "No", variable = Question_4_Radio_Button, value = "No", bg = "black", fg = "white")
Question_4_r2.pack()

Question_5_Radio_Button = StringVar(value = 0)

Question_5 = Label(root, text = "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?", bg = "black", fg = "white")
Question_5.pack()
Question_5_r1 = Radiobutton(root, text = "Yes", variable = Question_5_Radio_Button, value = "Yes", bg = "black", fg = "white")
Question_5_r1.pack()
Question_5_r2 = Radiobutton(root, text = "No", variable = Question_5_Radio_Button, value = "No", bg = "black", fg = "white")
Question_5_r2.pack()

def Heart_score():
    score = 0
    if Question_1_Radio_Button.get() == "Yes":
        score = score + 20
        print(score)
        
    if Question_2_Radio_Button.get() == "Yes":
        score = score + 20
        print(score)
        
    if Question_3_Radio_Button.get() == "Yes":
        score = score + 20
        print(score)
        
    if Question_4_Radio_Button.get() == "Yes":
        score = score + 20
        print(score)
        
    if Question_5_Radio_Button.get() == "Yes":
        score = score + 20
        print(score)
        
        
    if score <= 20:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
        
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report", "You might need to visit a doctor.")
        
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")
        
btn1 = Button(root, text = "Click Me", command = Heart_score)
btn1.pack()

root.mainloop()
