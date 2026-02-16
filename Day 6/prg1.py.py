import tkinter as tk

def find_definition():
    search_term = word_entry.get().lower()
    with open('wordDictionary.txt', 'r') as file:
            for line in file:
                if line.startswith(search_term + '|'):
                        meaning = line.split('|')[2]
                        break
    meaning = tk.Label(dict_window, text='')
    meaning.grid(row=0, column=4)
    meaning = tk.Label(dict_window, text=meaning)
    meaning.grid(row=0, column=4)

def find_number():
    chrs = chars_entry.get().lower()
    with open('wordDictionary.txt', 'r') as file:
        count = sum(1 for i in file if i.startswith(chrs))
        freq = tk.Label(dict_window, text=f"Count: {count}")
        freq.grid(row=1, column=4)

def find_word():
    num = int(length_entry.get())
    with open('wordDictionary.txt', 'r') as file:
            for line in file:
                    if line[num] == '|':
                            word = line.split('|')[0]
                            break

    result_lbl = tk.Label(dict_window, text=f"Found: {word}")
    result_lbl.grid(row=2, column=4)

def open_dictionary():
    global dict_window, word_entry, chars_entry, length_entry
    dict_window = tk.Toplevel()
    dict_window.title("Dictionary")
    dict_window.geometry("750x150")

    # Meaning Row
    tk.Label(dict_window, text="Find meaning of:").grid(row=0, column=0)
    word_entry = tk.Entry(dict_window)
    word_entry.grid(row=0, column=1)
    tk.Button(dict_window, text="Go", command=find_definition).grid(row=0, column=2)

    # Frequency Row
    tk.Label(dict_window, text="Find frequency of words starting with:").grid(row=1, column=0)
    chars_entry = tk.Entry(dict_window)
    chars_entry.grid(row=1, column=1)
    tk.Button(dict_window, text="Go", command=find_number).grid(row=1, column=2)
    
    # Length Row
    tk.Label(dict_window, text="Find first word with length:").grid(row=2, column=0)
    length_entry = tk.Entry(dict_window)
    length_entry.grid(row=2, column=1)
    tk.Button(dict_window, text="Go", command=find_word).grid(row=2, column=2)

def check_login():
    pswrd = password.get()
    user = username.get()
    Users = {"Tejassh": "password123", "Sanjay": "12345678"}
    if user in Users and pswrd == Users[user]:
        open_dictionary()

# Main Login Window
login = tk.Tk()
login.title("Dictionary Login")
login.geometry("300x150")

tk.Label(login, text="Username:").grid(row=1, column=0)
username = tk.Entry(login)
username.grid(row=1, column=1)

tk.Label(login, text="Password:").grid(row=2, column=0)
password = tk.Entry(login, show="*") 
password.grid(row=2, column=1)

tk.Button(login, text="Login", command=check_login).grid(row=3, column=1)

login.mainloop()
