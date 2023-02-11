from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passwordletters = [random.choice(letters) for _ in range(nr_letters)]
    passwordsymbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passwordnumbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = passwordletters + passwordsymbols + passwordnumbers
    random.shuffle(password_list)

    password = "".join(password_list)

    passwordentry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Generated!", message="Password has been copied to clipboard.")
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteentry.get()
    email = emailentry.get()
    password = passwordentry.get()

    if len(website) ==0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Welp.", message="Please make sure no fields are empty :)")
    else:
        isok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                     f"\nPassword: {password} \nIs it ok to save?")

        if isok:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{website} | {email} | {password}\n")
                websiteentry.delete(0, END)
                passwordentry.delete(0, END)
                emailentry.delete(0, END)
                
                

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("P@ssw0rd Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)


#Labels
websitelabel = Label(text="Website")
websitelabel.grid(row=1, column=0)
emaillabel = Label(text="Email/Username")
emaillabel.grid(row=2, column=0)
passwordlabel = Label(text="Password")
passwordlabel.grid(row=3, column=0)

#Entries
websiteentry = Entry(width=35)
websiteentry.grid(row=1, column=1, columnspan=2)
websiteentry.focus()
emailentry = Entry(width=35)
emailentry.grid(row=2, column=1, columnspan=2)
passwordentry = Entry(width=25)
passwordentry.grid(row=3, column=1)


#Buttons
genpassbutton = Button(text="Generate", command=genpass)
genpassbutton.grid(row=3, column=2)
addbutton = Button(text="Add", width=35, command=save)
addbutton.grid(row=4, column=1, columnspan=2)

window.mainloop()
