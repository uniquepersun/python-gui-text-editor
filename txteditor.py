import tkinter as tk
from tkinter import filedialog

def open_file():
    root = tk.Tk()
    root.title("Text Editor")
    text_area = tk.Text(root)
    
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

def save_file():
    root = tk.Tk()
    root.title("Text Editor")
    text_area = tk.Text(root)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def create_temporary_status_bar(root, text):
    status_bar = tk.Label(root, text=text, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    def destroy_status_bar():
        status_bar.destroy()
    root.after(2400, destroy_status_bar)

def create_text_editor():
    root = tk.Tk()
    root.title("Text Editor")
    text_area = tk.Text(root)
    text_area.pack(expand=True, fill="both")
    status_bar = tk.Label(root, text="Ready", anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    toolbar = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
    toolbar.pack(side=tk.TOP, fill=tk.X)
    open_button = tk.Button(toolbar, text="Open", command=open_file)
    open_button.pack(side=tk.LEFT, padx=2, pady=2)
    save_button = tk.Button(toolbar, text="Save", command=save_file)
    save_button.pack(side=tk.LEFT, padx=2, pady=2)
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)
    create_temporary_status_bar(root, "Editor loaded successfully")
    root.mainloop()

create_text_editor()
