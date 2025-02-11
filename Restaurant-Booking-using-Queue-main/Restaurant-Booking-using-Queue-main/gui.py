import tkinter as tk
from tkinter import messagebox
from data_structure import NODE, QUEUE  # Assuming this is your data structure file

class RestaurantBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Restaurant Reservation System')
        self.root.geometry('600x500')
        self.root.configure(bg="#f8f8f8")

        # --- Styling ---
        self.font_heading = ("Arial", 24, "bold")
        self.font_labels = ("Arial", 16)
        self.font_buttons = ("Arial", 14)
        self.color_primary = "#3498db"
        self.color_secondary = "#2ecc71"
        self.color_text = "#333333"

        # --- Frames ---
        self.frame_header = tk.Frame(root, bg=self.color_primary, pady=20)
        self.frame_header.pack(fill=tk.X)

        self.frame_input = tk.Frame(root, bg="#f8f8f8", padx=20, pady=20)
        self.frame_input.pack()

        self.frame_buttons = tk.Frame(root, bg="#f8f8f8", pady=10)
        self.frame_buttons.pack()

        self.frame_bookings = tk.Frame(root, bg="#f8f8f8", pady=10)
        self.frame_bookings.pack()

        # --- Header ---
        self.label_heading = tk.Label(self.frame_header, text="Restaurant Reservation System", font=self.font_heading, bg=self.color_primary, fg="white")
        self.label_heading.pack()

        # --- Input Fields ---
        self.label_name = tk.Label(self.frame_input, text="Name:", font=self.font_labels, bg="#f8f8f8", fg=self.color_text)
        self.label_name.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)

        self.entry_name = tk.Entry(self.frame_input, font=self.font_labels, bg="white", fg=self.color_text)
        self.entry_name.grid(row=0, column=1, padx=5, pady=10, sticky=tk.EW)

        self.label_people = tk.Label(self.frame_input, text="People:", font=self.font_labels, bg="#f8f8f8", fg=self.color_text)
        self.label_people.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)

        self.entry_people = tk.Entry(self.frame_input, font=self.font_labels, width=10, bg="white", fg=self.color_text)
        self.entry_people.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W)

        # --- Buttons ---
        self.button_add = tk.Button(self.frame_buttons, text="Add Booking", command=self.add_booking, font=self.font_buttons, bg=self.color_secondary, fg="white", padx=15, pady=8)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_process = tk.Button(self.frame_buttons, text="Process Booking", command=self.process_booking, font=self.font_buttons, bg=self.color_primary, fg="white", padx=15, pady=8)
        self.button_process.pack(side=tk.LEFT, padx=10)

        # --- Bookings Display ---
        self.bookings_text = tk.Text(self.frame_bookings, wrap=tk.WORD, height=10, width=50, bg="white", fg=self.color_text)
        self.bookings_text.pack()

        self.queue = QUEUE()  # Initialize the queue HERE!
        self.update_bookings_display()  # Call AFTER initializing the queue


    def add_booking(self):
        try:
            name = self.entry_name.get()
            people = int(self.entry_people.get())

            if not name or people <= 0:
                messagebox.showwarning("Input Error", "Please enter a valid name and number of people.")
                return

            self.queue.Enqueue(name, people)
            self.update_bookings_display()

            self.entry_name.delete(0, tk.END)
            self.entry_people.delete(0, tk.END)

        except ValueError:
            messagebox.showwarning("Input Error", "Number of people must be an integer.")
        except Exception as e:
            messagebox.showwarning("Error", f"An error occurred: {e}")

    def process_booking(self):
        if not self.queue.is_empty():
            self.queue.Dequeue()
            self.update_bookings_display()
        else:
            messagebox.showinfo("Queue Empty", "No bookings to process.")

    def update_bookings_display(self):
        self.bookings_text.delete("1.0", tk.END)
        if self.queue.is_empty():
            self.bookings_text.insert(tk.END, "No bookings in queue.")
        else:
            bookings_list = self.queue.Print_test()  # Assuming this returns a list of strings
            for booking in bookings_list:
                self.bookings_text.insert(tk.END, booking + "\n")


root = tk.Tk()
app = RestaurantBookingApp(root)
root.mainloop()