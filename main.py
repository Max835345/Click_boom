import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Calculator:
    def __init__(self, root):

        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x270")

        self.first_number_entry = ttk.Entry(self.root)
        self.second_number_entry = ttk.Entry(self.root)
        self.tab_button = ttk.Button(self.root, text="<=>", command=self.next_number)

        self.button_1 = ttk.Button(self.root, text="1", command=lambda: self.button_click(1))
        self.button_2 = ttk.Button(self.root, text="2", command=lambda: self.button_click(2))
        self.button_3 = ttk.Button(self.root, text="3", command=lambda: self.button_click(3))
        self.button_4 = ttk.Button(self.root, text="4", command=lambda: self.button_click(4))
        self.button_5 = ttk.Button(self.root, text="5", command=lambda: self.button_click(5))
        self.button_6 = ttk.Button(self.root, text="6", command=lambda: self.button_click(6))
        self.button_7 = ttk.Button(self.root, text="7", command=lambda: self.button_click(7))
        self.button_8 = ttk.Button(self.root, text="8", command=lambda: self.button_click(8))
        self.button_9 = ttk.Button(self.root, text="9", command=lambda: self.button_click(9))
        self.button_0 = ttk.Button(self.root, text="0", command=lambda: self.button_click(0))

        self.button_clear = ttk.Button(self.root, text="C", command=self.button_clear)
        self.button_equal = ttk.Button(self.root, text="-", command=self.button_neg)
        self.button_floor_div = ttk.Button(self.root, text="DIV", command=self.button_floor_div)
        self.button_modulus = ttk.Button(self.root, text="MOD", command=self.button_modulus)

        self.first_number_entry.grid(row=0, column=1, columnspan=2, padx=1, ipadx=10, ipady=10, pady=2)
        self.second_number_entry.grid(row=0, column=3, columnspan=2, padx=1, ipadx=10, ipady=10, pady=2)

        self.button_modulus.grid(row=1, column=0, columnspan=2, ipadx=20, ipady=10)
        self.tab_button.grid(row=1, column=2, columnspan=2, ipadx=20, ipady=10)
        self.button_floor_div.grid(row=1, column=4, columnspan=2, ipadx=20, ipady=10)

        self.button_1.grid(row=2, column=0, columnspan=2, ipadx=20, ipady=10)
        self.button_2.grid(row=2, column=2, columnspan=2, ipadx=20, ipady=10)
        self.button_3.grid(row=2, column=4, columnspan=2, ipadx=20, ipady=10)

        self.button_4.grid(row=3, column=0, columnspan=2, ipadx=20, ipady=10)
        self.button_5.grid(row=3, column=2, columnspan=2, ipadx=20, ipady=10)
        self.button_6.grid(row=3, column=4, columnspan=2, ipadx=20, ipady=10)

        self.button_7.grid(row=4, column=0, columnspan=2, ipadx=20, ipady=10)
        self.button_8.grid(row=4, column=2, columnspan=2, ipadx=20, ipady=10)
        self.button_9.grid(row=4, column=4, columnspan=2, ipadx=20, ipady=10)

        self.button_clear.grid(row=5, column=0, columnspan=2, ipadx=20, ipady=10)
        self.button_0.grid(row=5, column=2, columnspan=2, ipadx=20, ipady=10)
        self.button_equal.grid(row=5, column=4, columnspan=2, ipadx=20, ipady=10)

        self.current_number_entry = self.first_number_entry

    def next_number(self):
        if self.current_number_entry == self.first_number_entry:
            self.current_number_entry = self.second_number_entry
        else:
            self.current_number_entry = self.first_number_entry

    def button_click(self, number):
        current = self.current_number_entry.get()
        self.current_number_entry.delete(0, tk.END)
        self.current_number_entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.current_number_entry.delete(0, tk.END)

    def button_floor_div(self):
        first_number = int(self.first_number_entry.get())
        second_number = int(self.second_number_entry.get())
        showinfo("Результат", "Результат целочисленного деления: " + str(first_number // second_number))

    def button_modulus(self):
        first_number = int(self.first_number_entry.get())
        second_number = int(self.second_number_entry.get())
        showinfo("Результат", "Остаток от деления: " + str(first_number % second_number))

    def button_neg(self):
        current = self.current_number_entry.get()
        if current.startswith("-"):
            current = current[1:]
        else:
            current = "-" + current
        self.current_number_entry.delete(0, tk.END)
        self.current_number_entry.insert(0, current)


root = tk.Tk()
Calculator(root)
root.mainloop()
