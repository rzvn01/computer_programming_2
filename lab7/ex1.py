import tkinter as tk


def count_statistics(event=None):
    user_input = input_entry.get()
    selected_option = counting_option.get()

    if selected_option == "Sentences":
        split_string = user_input.split('.')
        count = len(user_input.split('.'))
        # Do not count white spaces after the last line as a sentence
        if len(split_string[len(split_string) - 1].replace(" ", "")) == 0:
            count = count - 1
    elif selected_option == "Words":
        count = len(user_input.split())
    elif selected_option == "Letters":
        count = len(user_input.replace(" ", ""))

    result_text.set(f"{selected_option}: {count}")


root = tk.Tk()

input_label = tk.Label(root, text="Input String:")
input_label.grid(row=0, column=0, columnspan=2, sticky="w")

input_entry = tk.Entry(root, width=40)
input_entry.grid(row=1, column=0, columnspan=2, sticky="w")

counting_option = tk.StringVar()
counting_option.set("Sentences")

sentences_radio = tk.Radiobutton(root, text="Sentences", variable=counting_option,
                                 value="Sentences")
words_radio = tk.Radiobutton(root, text="Words", variable=counting_option,
                             value="Words")
letters_radio = tk.Radiobutton(root, text="Letters", variable=counting_option,
                               value="Letters")

sentences_radio.grid(row=0, column=3)
words_radio.grid(row=1, column=3)
letters_radio.grid(row=2, column=3)

# Bind the count_statistics function to the <KeyRelease> event of the input_entry
input_entry.bind("<KeyRelease>", count_statistics)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=3, column=0, columnspan=4, pady=10, sticky="w")

root.mainloop()  # Start the main event loop for the GUI
