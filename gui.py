import tkinter as tk
from tkinter import ttk, messagebox

# Create main window
root = tk.Tk()
root.title("Train Finder")
root.geometry("800x600")
root.configure(bg="#1e1e1e")  # Dark mode background

# Custom Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#1e1e1e", foreground="white")

# Header Frame
header_frame = tk.Frame(root, bg="#ffcc00", height=60)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Train Finder App", font=("Arial", 18, "bold"), bg="#ffcc00")
header_label.pack(pady=10)

# Search Frame
search_frame = tk.Frame(root, bg="#2e2e2e", pady=20)
search_frame.pack(fill="x")

# Labels and Inputs
source_label = ttk.Label(search_frame, text="Source:")
source_label.grid(row=0, column=0, padx=10, pady=5)

source_entry = ttk.Entry(search_frame, font=("Arial", 12))
source_entry.grid(row=0, column=1, padx=10, pady=5)

destination_label = ttk.Label(search_frame, text="Destination:")
destination_label.grid(row=0, column=2, padx=10, pady=5)

destination_entry = ttk.Entry(search_frame, font=("Arial", 12))
destination_entry.grid(row=0, column=3, padx=10, pady=5)

find_train_btn = ttk.Button(search_frame, text="Find Train", command=lambda: messagebox.showinfo("Search", "Feature Coming Soon!"))
find_train_btn.grid(row=0, column=4, padx=10, pady=5)

# Train List Frame
train_frame = tk.Frame(root, bg="#1e1e1e")
train_frame.pack(fill="both", expand=True)

# Developer Label
footer_label = tk.Label(root, text="This App is Developed by Thiru Jugal", font=("Arial", 14, "bold"), bg="#ffcc00", fg="black", pady=10)
footer_label.pack(side="bottom", fill="x")

# Run Application
root.mainloop()
