import tkinter as tk

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("400x600")
        self.config(bg="#f2f2f2")  # Couleur de fond de la fenêtre

        self.entry = tk.Entry(self, font=("Helvetica", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.ajouter_boutons()
        self.ajouter_bouton_resultat()
        self.ajouter_bouton_effacer()

    def ajouter_boutons(self):
        bouton_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2)
        ]

        for (text, row, column) in bouton_texts:
            bouton = tk.Button(self, text=text, font=("Helvetica", 20), command=lambda t=text: self.cliquer_bouton(t))
            bouton.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10)

    def ajouter_bouton_resultat(self):
        bouton = tk.Button(self, text="=", font=("Helvetica", 20), command=self.calculer_resultat)
        bouton.grid(row=4, column=3, padx=5, pady=5, ipadx=10, ipady=10)

    def ajouter_bouton_effacer(self):
        bouton = tk.Button(self, text="C", font=("Helvetica", 20), command=self.effacer)
        bouton.grid(row=4, column=0, padx=5, pady=5, ipadx=10, ipady=10)

    def cliquer_bouton(self, texte):
        valeur_actuelle = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, valeur_actuelle + texte)

    def calculer_resultat(self):
        expression = self.entry.get()
        try:
            resultat = str(eval(expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, resultat)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erreur")

    def effacer(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
