import tkinter as tk
# ввожу блок кода, в котором могут возникнуть исключения
def calculate():
    try:
        # поля ввода
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        # cоздаём исключения
        if operation not in ['+', '-', '*', '/']:
            result_var.set("Неверная операция. Можно использовать '+', '-', '*' или '/'")
            return

        # деление на ноль
        if operation == '/' and num2 == 0:
            result_var.set("Error")
            return

        result = perform_calculation(num1, num2, operation)
        result_text = f"Результат: {result}"
        result_var.set(result_text)

        # ошибка на случай если пользователь вводит не целые числа, или вообще не числа
    except ValueError:
        result_var.set("Ошибка ввода. Введите цельные числа.")

        # задаю операции
def perform_calculation(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b

# Создание графического интерфейса
root = tk.Tk()
root.title("Калькулятор без цветов")

# Ввод чисел и операции
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

# Кнопка для выполнения расчета
calculate_button = tk.Button(root, text="Выполнить подсчёт", command=calculate)
calculate_button.pack()

# Отображение результата
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

# Запуск главного цикла программы
root.mainloop()
