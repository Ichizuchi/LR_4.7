import tkinter as tk
from tkinter import messagebox

# Функция для открытия файла и загрузки содержимого в Text
def open_file():
    file_name = entry.get()
    if not file_name:
        messagebox.showwarning("Ошибка", "Введите имя файла")
        return
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text.delete(1.0, tk.END) 
            text.insert(tk.END, file.read())  
    except FileNotFoundError:
        messagebox.showerror("Ошибка", f"Файл '{file_name}' не найден")

# Cохранениt содержимого Text в файл
def save_file():
    file_name = entry.get()
    if not file_name:
        messagebox.showwarning("Ошибка", "Введите имя файла")
        return
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text.get(1.0, tk.END)) 
    messagebox.showinfo("Успех", f"Файл '{file_name}' успешно сохранен")

root = tk.Tk()
root.title("Редактор файлов")

entry_label = tk.Label(root, text="Имя файла:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

text = tk.Text(root, wrap='word', width=60, height=20)
text.pack(padx=10, pady=5)

open_button = tk.Button(root, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=10, pady=5)

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Запуск основного цикла 
root.mainloop()
