import tkinter as tk

def on_radio_button_select():
    if r_var.get() == 1:
        info_label.config(text="1 Января")
    elif r_var.get() == 2:
        info_label.config(text="4 Ноября")
    elif r_var.get() == 3:
        info_label.config(text="9 Мая")

# главное окно
root = tk.Tk()
root.title("Радиокнопки")

radio_frame = tk.Frame(root)
radio_frame.pack(side=tk.LEFT, padx=20, pady=20)

info_label = tk.Label(root, text="Выберите вариант", font=("Arial", 14), width=30, anchor="w")
info_label.pack(side=tk.LEFT, padx=20, pady=20)

r_var = tk.IntVar()

r1 = tk.Radiobutton(radio_frame, text='Новый Год', variable=r_var, value=1, command=on_radio_button_select, indicatoron=0, width=20, height=2, anchor="w", padx=10, pady=5)
r1.pack(pady=5)

r2 = tk.Radiobutton(radio_frame, text='День Народного Единства', variable=r_var, value=2, command=on_radio_button_select, indicatoron=0, width=20, height=2, anchor="w", padx=10, pady=5)
r2.pack(pady=5)

r3 = tk.Radiobutton(radio_frame, text='День Победы', variable=r_var, value=3, command=on_radio_button_select, indicatoron=0, width=20, height=2, anchor="w", padx=10, pady=5)
r3.pack(pady=5)

root.mainloop()
