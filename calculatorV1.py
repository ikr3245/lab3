import tkinter as tk
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        if operation not in ['+', '-', '*', '/']:
            result_var.set("Неверная операция. Можно использовать '+', '-', '*' или '/'")
            return

        if operation == '/' and num2 == 0:
            result_var.set("Error")
            return

        result = perform_calculation(num1, num2, operation)
        result_text = f"Результат: {result}"
        result_var.set(result_text)

    except ValueError:
        result_var.set("Ошибка ввода. Введите цельные числа.")

def perform_calculation(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b

root = tk.Tk()
root.title("Калькулятор без цветов")

label_num1 = tk.Label(root, text="Введите первое число:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_operation = tk.Label(root, text="Введите операцию (+, -, *, /):")
label_operation.pack()
entry_operation = tk.Entry(root)
entry_operation.pack()

label_num2 = tk.Label(root, text="Введите второе число:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

calculate_button = tk.Button(root, text="Выполнить подсчёт", command=calculate)
calculate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
