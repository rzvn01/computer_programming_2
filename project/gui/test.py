# import tkinter as tk
# from tkinter import ttk
#
# class FuelConsumptionApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Fuel Consumption Calculator")
#
#         # Create a StringVar to store the selected value
#         self.fuel_consumption_var = tk.StringVar()
#
#         # Set a default value
#         self.fuel_consumption_var.set("4.0")
#
#         # Create a Label
#         label = tk.Label(self, text="Fuel Consumption:")
#         label.pack(pady=10)
#
#         # Create an Entry for numeric input
#         self.entry = tk.Entry(self, textvariable=self.fuel_consumption_var)
#         self.entry.pack(pady=5)
#
#         # Create a dropdown with values from 4 to 10 with a step of 0.5
#         values = [round(i, 1) for i in range(40, 101, 5)]  # Multiply by 10 to handle floating-point precision
#         self.dropdown = ttk.Combobox(self, values=values, textvariable=self.fuel_consumption_var)
#         self.dropdown.pack(pady=10)
#
#         # Bind the Entry to validate the input
#         self.entry.bind("<FocusOut>", self.validate_entry)
#
#         # Set the dropdown event to update the Entry
#         self.dropdown.bind("<<ComboboxSelected>>", self.update_entry)
#
#     def validate_entry(self, event):
#         try:
#             # Validate the numeric input in the Entry
#             value = float(self.fuel_consumption_var.get())
#             if 4.0 <= value <= 10.0:
#                 # If valid, update the dropdown selection
#                 self.fuel_consumption_var.set(round(value, 1))
#                 self.dropdown.set(round(value, 1))
#             else:
#                 # If not valid, reset to the default value
#                 self.fuel_consumption_var.set("4.0")
#                 self.dropdown.set("4.0")
#         except ValueError:
#             # If not a valid float, reset to the default value
#             self.fuel_consumption_var.set("4.0")
#             self.dropdown.set("4.0")
#
#     def update_entry(self, event):
#         # Update the Entry when a dropdown value is selected
#         self.fuel_consumption_var.set(self.dropdown.get())
#
# if __name__ == "__main__":
#     app = FuelConsumptionApp()
#     app.mainloop()


import tkinter as tk
from tkinter import ttk

class FuelConsumptionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fuel Consumption Calculator")

        # Create a StringVar to store the selected value
        self.fuel_consumption_var = tk.StringVar()

        # Set a default value
        self.fuel_consumption_var.set("4.0")

        # Create a Label
        label = tk.Label(self, text="Fuel Consumption:")
        label.pack(pady=10)

        # Create an Entry for numeric input
        self.entry = tk.Entry(self, textvariable=self.fuel_consumption_var)
        self.entry.pack(pady=5)

        # Create a Combobox with values from 4 to 10 with a step of 0.5
        values = [round(i, 1) for i in range(40, 101, 5)]  # Multiply by 10 to handle floating-point precision
        self.dropdown = ttk.Combobox(self, values=values, textvariable=self.fuel_consumption_var)
        self.dropdown.pack(pady=10)

        # Create a Checkbox for manual input
        self.manual_input_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self, text="Manual Input", variable=self.manual_input_var, command=self.toggle_input_mode)
        self.checkbox.pack(pady=5)

        # Bind the Entry to validate the input
        self.entry.bind("<FocusOut>", self.validate_entry)

        # Set the dropdown event to update the Entry
        self.dropdown.bind("<<ComboboxSelected>>", self.update_entry)

        # Initially disable the Entry when using predefined values
        self.toggle_input_mode()

    def toggle_input_mode(self):
        # Enable or disable the Entry based on the checkbox state
        if self.manual_input_var.get():
            self.entry.config(state=tk.NORMAL)
        else:
            self.entry.config(state=tk.DISABLED)

    def validate_entry(self, event):
        if self.manual_input_var.get():
            try:
                # Validate the numeric input in the Entry
                value = float(self.fuel_consumption_var.get())
                if 4.0 <= value <= 10.0:
                    # If valid, update the dropdown selection
                    self.fuel_consumption_var.set(round(value, 1))
                    self.dropdown.set(round(value, 1))
                else:
                    # If not valid, reset to the default value
                    self.fuel_consumption_var.set("4.0")
                    self.dropdown.set("4.0")
            except ValueError:
                # If not a valid float, reset to the default value
                self.fuel_consumption_var.set("4.0")
                self.dropdown.set("4.0")

    def update_entry(self, event):
        # Update the Entry when a dropdown value is selected
        if self.manual_input_var.get():
            self.fuel_consumption_var.set(self.dropdown.get())

if __name__ == "__main__":
    app = FuelConsumptionApp()
    app.mainloop()
