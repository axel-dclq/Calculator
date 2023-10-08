import tkinter as tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__() # recall constructor from Tk
        self.title('Calculator')
        self.geometry('400x500')
        self.config(bg="#d2e5f7") # set the background color of the calculator 

        self.entry = tk.Entry(self, font=("Helvetica", 24), justify="right") 
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.add_button()
        # self.add_result_button()
        # self.add_C_button()

    def add_button(self):
        bouton_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2)
        ]

        for (text, row, column) in bouton_texts:
            bouton = tk.Button(self, text=text, font=("Helvetica", 20), command=lambda t=text: self.click_button(t))
            bouton.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10)
    
    # def add_result_button():

    # def add_C_button():

    

    def click_button(self, button):
        """
        button is the value (string) contained by the clicked button
        """
        current_value = self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(tk.END, current_value + button)



if __name__ == '__main__':
    app = Calculator()
    app.mainloop()