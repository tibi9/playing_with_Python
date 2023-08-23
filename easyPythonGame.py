import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.number_to_guess:
            result = "Too low! Try again."
        elif guess > self.number_to_guess:
            result = "Too high! Try again."
        else:
            result = f"Congratulations! You guessed the number {self.number_to_guess} in {self.attempts} attempts."
            self.submit_button.config(state=tk.DISABLED)

        if self.attempts == self.max_attempts:
            result = f"Sorry, you've run out of attempts. The number was {self.number_to_guess}."
            self.submit_button.config(state=tk.DISABLED)

        messagebox.showinfo("Result", result)


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
