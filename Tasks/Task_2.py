import tkinter as tk

colors = [
    ("Красный", "#ff0000"),
    ("Оранжевый", "#ff7d00"),
    ("Желтый", "#ffff00"),
    ("Зеленый", "#00ff00"),
    ("Голубой", "#007dff"),
    ("Синий", "#0000ff"),
    ("Фиолетовый", "#7d00ff")
]

root = tk.Tk()
root.title("Цвета радуги")

# Метка названия цвета
label = tk.Label(root, text="Выберите цвет", font=("Arial", 14))
label.pack(pady=10)

# Текстовое поле для отображения кода цвета
color_code_entry = tk.Entry(root, font=("Arial", 12), width=15, justify="center")
color_code_entry.pack(pady=10)

def show_color(name, code):
    label.config(text=name) 
    color_code_entry.delete(0, tk.END) 
    color_code_entry.insert(0, code)  

# Кнопки для каждого цвета
for name, code in colors:
    button = tk.Button(
        root, text=name, bg=code, width=10, height=2,
        command=lambda n=name, c=code: show_color(n, c)
    )
    button.pack(pady=5)

# Запуск цикла
root.mainloop()
