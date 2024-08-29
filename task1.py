import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    # Validate email format (optional)
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return

    # Save data to a file or database (customize this part)

    # Display a success message
    messagebox.showinfo("Registration Form", "Registration successful!")

def validate_email(email):
    # Implement your email validation logic here
    # For example, use regular expressions to check the format
    # Return True if valid, False otherwise
    return True  # Placeholder; replace with actual validation

# Create the main window
root = tk.Tk()
root.title("Advanced Registration Form")

# Labels and entry fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Add some spacing between entry fields
tk.Label(root, text="").pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the application
root.mainloop()



import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    # Validate email format (optional)
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return

    # Save data to a file or database (customize this part)

    # Display a success message
    messagebox.showinfo("Registration Form", "Registration successful!")

def validate_email(email):
    # Implement your email validation logic here
    # For example, use regular expressions to check the format
    # Return True if valid, False otherwise
    return True  # Placeholder; replace with actual validation

# Create the main window
root = tk.Tk()
root.title("Advanced Registration Form")

# Labels and entry fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Add some spacing between entry fields
tk.Label(root, text="").pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the application
root.mainloop()
