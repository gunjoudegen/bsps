import tkinter as tk
from tkinter import messagebox

def show_modal_dialog():
    modal_dialog = tk.Toplevel(root)
    modal_dialog.title("Modal Dialog")
    modal_dialog.geometry("300x150")

    label = tk.Label(modal_dialog, text="This is a modal dialog!")
    label.pack(pady=10)

    ok_button = tk.Button(modal_dialog, text="OK", command=modal_dialog.destroy)
    ok_button.pack()

    # Set modal dialog as transient for root window (prevents it from appearing in taskbar)
    modal_dialog.transient(root)

    # Grab focus and disable user interaction with other windows
    modal_dialog.grab_set()

    # Create a tkinter variable to track the state of the modal dialog
    modal_dialog_closed = tk.BooleanVar(value=False)

    def on_modal_dialog_close():
        modal_dialog_closed.set(True)

    modal_dialog.protocol("WM_DELETE_WINDOW", on_modal_dialog_close)

    # Wait for the modal dialog to close before allowing user interaction with other windows
    modal_dialog.wait_variable(modal_dialog_closed)

    # Release grab and allow user interaction with other windows
    modal_dialog.grab_release()

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Add a button to the main window that opens the modal dialog
button = tk.Button(root, text="Open Modal Dialog", command=show_modal_dialog)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
