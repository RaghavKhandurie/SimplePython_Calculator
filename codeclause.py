from tkinter import *;
from tkinter import messagebox;

def is_number(s):
    if(s != ''):
        if (s.replace('.', '', 1).isdigit()):
            return True
        if (s.isdigit()):
            return True;
        if s[0] in ['-', '+', '.', '0', ' ']:
            if (s[1] == '.'):
                if (s[2:].isdigit()):
                    return True
            if (s[1] == '0' and s[2] == '.'):
                if (s[3:].isdigit()):
                    return True
            if s[1:].isdigit():
                return True;
        return False;


#casting
def cast_num(number):
    if('.' in number):
        return float(number);
    else:
        return int(number)

#addition
def action_Plus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='red', bg='#9ed8ee')
    Showtemplabel.insert(0, 'Summation');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')
    ans = "0";
    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    number1 = first_number.get();
    number2 = second_number.get();

    if(is_number(number1) == True and is_number(number2) == True and number1 != ' ' and number2 != ' '):
        number1 = cast_num(number1);
        number2 = cast_num(number2);
        ans = str(number1 + number2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='red', bg='#9ed8ee')
        Showtemplabel.insert(0, 'Summation');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number")




#subtraction
def action_Minus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='green', bg='#ece7e2')
    Showtemplabel.insert(0, 'Subtraction');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0";

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    number1 = first_number.get();
    number2 = second_number.get();

    if(is_number(number1)==True and is_number(number2)==True):
        number1 = cast_num(number1);
        number2 = cast_num(number2);
        ans = str(number1 - number2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='green', bg='#ece7e2')
        Showtemplabel.insert(0, 'Subtraction');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number")




#multiplication
def action_Mul():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='blue', bg='#cacba9')
    Showtemplabel.insert(0, 'Multiplication');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    number1 = first_number.get();
    number2 = second_number.get();
    if(is_number(number1)==True and is_number(number2)==True):
        number1 = cast_num(number1);
        number2 = cast_num(number2);
        ans = str(number1 * number2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='blue', bg='#cacba9')
        Showtemplabel.insert(0, 'Multiplication');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number")




#division
def action_Div():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'Division');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    number1 = first_number.get();
    number2 = second_number.get();
    if(is_number(number1)==True and is_number(number2)==True):
        number1 = cast_num(number1);
        number2 = cast_num(number2);
        ans = str(number1 / number2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'Division');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number")
root = Tk();


#main

root.title('CodeClause Internship : Proj1 : Calculator');
root.geometry('380x300+200+250');
Title = Label(root, fg = 'white' ,text = 'CodeClause Project 1', compound = CENTER)
Title_2 = Label(root, fg = 'white' ,text = 'Raghav Khandurie', compound = CENTER)
Title.place(relx=0.5, rely=0.1, anchor='center')
Title_2.place(relx=0.5, rely=0.5, anchor='center')
Showlabel = Entry(root);
Showtemplabel = Entry(root);
first_number = Entry(root);
second_number = Entry(root);
first_number.place(relx=0.5, rely=0.3, anchor='center')
second_number.place(relx=0.5, rely=0.4, anchor='center')

plusb = Button(root, text="+", width = 5, command = action_Plus);
plusb.place(relx=0.1, rely=0.7)

minusb = Button(root, text="-", width = 5, command = action_Minus);
minusb.place(relx=0.3, rely=0.7)

mulb = Button(root, text="*", width = 5, command = action_Mul);
mulb.place(relx=0.5, rely=0.7)

divb = Button(root, text="/", width = 5, command = action_Div);
divb.place(relx=0.7, rely=0.7)


root.resizable(False, False);
root.mainloop();