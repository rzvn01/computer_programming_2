import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FunctionPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Plotter")
        error_label = tk.Label()
        error_label.grid(row=4, column=0, sticky="w")
        self.selected_function = tk.StringVar(value="sin")
        self.min_limit_var = tk.StringVar()
        self.max_limit_var = tk.StringVar()

        # Function Label and Dropdown
        function_label = tk.Label(root, text="Select Function:")
        function_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        function_entry = ttk.Entry(root, textvariable=self.selected_function)
        function_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Limits Label and Entry for Min
        min_limit_label = tk.Label(root, text="Enter Min Limit:")
        min_limit_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.min_limit_entry = tk.Entry(root, textvariable=self.min_limit_var)
        self.min_limit_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Limits Label and Entry for Max
        max_limit_label = tk.Label(root, text="Enter Max Limit:")
        max_limit_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.max_limit_entry = tk.Entry(root, textvariable=self.max_limit_var)
        self.max_limit_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Plot Button
        plot_button = tk.Button(root, text="Plot", command=lambda: self.plot_function(error_label))
        plot_button.grid(row=3, column=0, columnspan=2, pady=10)

    def plot_function(self, error_label):
        # Get selected function and limits
        selected_function = self.selected_function.get()
        min_limit_str = self.min_limit_var.get()
        max_limit_str = self.max_limit_var.get()

        # Validate and convert limits to floats
        try:
            min_limit = float(min_limit_str)
            max_limit = float(max_limit_str)
            if max_limit <= min_limit:
                raise ValueError

        except ValueError:
            error_label.config(text="Invalid limit values.", fg='#FF0000')
            return

        # Plot the function based on the selected function and limits
        try:
            self.plot(selected_function, min_limit, max_limit)
        except Exception as e:
            error_label.config(text=f"An error occurred: {str(e)}", fg='#FF0000')

    def plot(self, selected_function, min_limit, max_limit):

        # Define the function to plot
        def f(x):
            if selected_function == "sin":
                return sin(x)
            elif selected_function == "cos":
                return cos(x)
            elif selected_function == "tan":
                return tan(x)
            elif selected_function == "xcos":
                return cos(x) / x
            else:
                raise ValueError("Invalid function")

        # Generate x values
        x_values = np.arange(min_limit, max_limit, 0.1)

        # Generate y values using the selected function
        y_values = [f(x) for x in x_values]

        fig = plt.figure(figsize=(4, 5))
        plt.plot(x_values, y_values)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=1)


root = tk.Tk()
app = FunctionPlotterApp(root)

root.mainloop()
