import tkinter as tk
import random
#creates the main window.


# root = tk.Tk() -> creates a blank canvas on which we can add the different features.
root = tk.Tk()
root.title("Number Guessing Game") # gives the title to the window.
root.geometry("450x400") # Setting the size of the window.
root.configure(bg = "black")



# Welcome message for the players.

welcome_label = tk.Label(text = "Welcome to the Number Guessing Game!", font = ("Roboto", 17), fg="Blue")
welcome_label.configure(bg="Black")
welcome_label.pack(pady = "20")



# Adding a label for the players.

guess_label = tk.Label(root, text="Enter your Guess (1-100)", font=("Arial", 18), bg="Yellow")
guess_label.pack(pady = "10")


# Adding an Entry box for input.

guess_entry = tk.Entry(root, font = ("Arial", 14))
guess_entry.pack(pady = "10")


#Creating a feedback label for the user.
feedback_label = tk.Label(root, text="", font=("Arial", 12), bg = "Black")
feedback_label.pack(pady = "10")


#Generating a random number to be guessed.
target = random.randint(1,100)
print("Target value is: ", target)


# Writing the logic for getting the inputed guess and guessing the number. 
def submit_guess():
    attempts = 3
    try:
        guess = int(guess_entry.get())
        print("Number guessed is: ", guess)
        
        if guess < target:
            feedback_label.config(text="Too Low, Try Again!", fg="red")
        elif guess > target:
            feedback_label.config(text="Too High, Try Again!", fg = "red")
        else:
            feedback_label.config(text="Congratulations!! You have rightly guessed the number", fg = "green")
            
    except ValueError:
        feedback_label.config(text="Please enter a valid numerical value.", fg = "red")
        
  
#Creating the button to submit the guess.

submit_button = tk.Button(root, text="Submit your guess", font=("Arial", 14), command = submit_guess, bg="Blue", fg="White")
submit_button.pack(pady = "10")


#starting the main loop.
root.mainloop()
