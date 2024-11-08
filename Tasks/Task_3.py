import tkinter as tk

colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff"
}

def on_color_button_click(color_name, color_code):
    color_label.config(text=color_name)  
    color_code_entry.delete(0, tk.END)   
    color_code_entry.insert(0, color_code)  

root = tk.Tk()
root.title("Цвета радуги")

color_label = tk.Label(root, text="Название цвета", font=("Arial", 14))
color_label.pack(pady=10)

color_code_entry = tk.Entry(root, font=("Arial", 12), justify="center")
color_code_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for color_name, color_code in colors.items():
    button = tk.Button(
        button_frame, 
        bg=color_code, 
        width=6, 
        height=3,
        command=lambda name=color_name, code=color_code: on_color_button_click(name, code)
    )
    button.pack(side=tk.LEFT, padx=5)

root.mainloop()
