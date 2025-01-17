from tkinter import Tk, Label, Button, PhotoImage, messagebox
from main import witCall

# Initialize the main Tkinter window
root = Tk()
root.title("Hear Everything")
root.geometry("400x300")  # Set the window size
root.resizable(False, False)  # Disable resizing

# Add a title label
Label(root, text='Hear Everything', font=('Verdana', 20, 'bold')).pack(pady=20)

# Add a subtitle label
Label(root, text='Your voice assistant for social media and searches', 
      font=('Verdana', 10)).pack(pady=5)

# Load and configure images for the button
try:
    mic_image = PhotoImage(file="mic.png").subsample(3, 3)
    listening_image = PhotoImage(file="mic2.png").subsample(3, 3)  # Replace with a listening state image
except Exception as e:
    messagebox.showerror("Error", f"Could not load images: {e}")
    mic_image = None
    listening_image = None

# Function to handle button click and change state
def start_voice_assistant():
    try:
        # Change the button to indicate listening state
        start_button.config(image=listening_image, text="Listening...", compound='top', state='disabled')
        root.update()  # Refresh the UI immediately
        
        witCall()  # Call the voice assistant function
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        # Revert the button back to the default state
        start_button.config(image=mic_image, text="Start", compound='top', state='normal')
        root.update()  # Refresh the UI

# Add the button with dynamic image switching
start_button = Button(
    root,
    image=mic_image,
    text="Start",
    command=start_voice_assistant,
    compound='top'
)
start_button.pack(pady=20)

# Add a footer
Label(root, text='Powered by Wit.ai and Hear Everything', font=('Verdana', 8, 'italic')).pack(side='bottom', pady=10)

# Start the Tkinter main loop
root.mainloop()