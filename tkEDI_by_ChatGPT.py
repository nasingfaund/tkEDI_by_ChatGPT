###333###########################################################333
# autor: nasingfaund aka Serg Kado by ChatGPT
# e-mail1: nasingfaund@gmail.com
# e-mail2: nasingfaund@ya.ru
###333###########################################################333

import tkinter as tk  
from tkinter import filedialog  
import subprocess  
import os  
import re  
  
# Настройки окна  
root = tk.Tk()  
root.title("Python Editor")  
  
# Настройки текстового поля для кода  
text = tk.Text(root, font=("Consolas", 12), undo=True)  
text.pack(expand=True, fill="both")  
  
# Настройки подсветки синтаксиса  
def highlight_syntax(event=None):  
    text.tag_remove("python", "1.0", "end")  
    code = text.get("1.0", "end-1c")  
    tokens = re.findall(r"[\w']+|[.,!?;]", code)  
    for token in tokens:  
        if token in ["True", "False", "None"]:  
            text.tag_add("python", f"1.0+{code.index(token)}", f"1.0+{code.index(token)}+{len(token)}")  
        elif token in ["if", "else", "elif", "while", "for", "in", "range", "def", "return", "import", "from", "as"]:  
            text.tag_add("python", f"1.0+{code.index(token)}", f"1.0+{code.index(token)}+{len(token)}")  
        elif token in ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "and", "or", "not"]:  
            text.tag_add("python", f"1.0+{code.index(token)}", f"1.0+{code.index(token)}+{len(token)}")  
    text.tag_config("python", foreground="white", background="black")  
  
text.bind("<KeyRelease>", highlight_syntax)  
  
# Настройки командной строки для вывода результатов  
console = tk.Text(root, bg="black", fg="white", font=("Consolas", 12))  
console.pack(expand=True, fill="both")  
  
# Функции для работы с файлами  
def new_file():  
    text.delete("1.0", "end")  
  
def open_file():  
    file_path = filedialog.askopenfilename()  
    if file_path:  
        with open(file_path, "r") as file:  
            text.delete("1.0", "end")  
            text.insert("1.0", file.read())  
  
def save_file():  
    file_path = filedialog.asksaveasfilename(defaultextension=".py")  
    if file_path:  
        with open(file_path, "w") as file:  
            file.write(text.get("1.0", "end-1c"))  
  
# Функция для запуска кода  
def run_code():  
    code = text.get("1.0", "end-1c")  
    with open("temp.py", "w") as file:  
        file.write(code)  
    process = subprocess.Popen(["python", "temp.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    stdout, stderr = process.communicate()  
    output = stdout.decode("utf-8") + stderr.decode("utf-8")  
    console.delete("1.0", "end")  
    console.insert("1.0", output)  
    os.remove("temp.py")  
  
# Настройки меню  
menu = tk.Menu(root)  
file_menu = tk.Menu(menu, tearoff=0)  
file_menu.add_command(label="New", command=new_file)  
file_menu.add_command(label="Open", command=open_file)  
file_menu.add_command(label="Save", command=save_file)  
file_menu.add_separator()  
file_menu.add_command(label="Exit", command=root.quit)  
menu.add_cascade(label="File", menu=file_menu)  
menu.add_command(label="Run", command=run_code)  
root.config(menu=menu)  
  
root.mainloop()
