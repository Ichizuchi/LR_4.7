import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root, width=10, font=("Arial", 14))
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10, font=("Arial", 14))
entry2.grid(row=1, column=0, padx=5, pady=5)

# Функция для калькулятора
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка")
    except ZeroDivisionError:
        result_label.config(text="Деление на ноль")

buttons = ["+", "-", "*", "/"]
for i, text in enumerate(buttons):
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: calculate(t))
    button.grid(row=2+i, column=0, padx=5, pady=5)

# Метка отображения результата
result_label = tk.Label(root, text="Результат", font=("Arial", 14))
result_label.grid(row=6, column=0, pady=10)

# Запуск цикла
root.mainloop()
