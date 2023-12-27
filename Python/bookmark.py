import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3

# Create a database connection
conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()

# Create a table to store bookmarks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        link TEXT
    )
''')
conn.commit()

# Function to add a bookmark to the database and listbox
def add_bookmark():
    name = name_entry.get()
    link = link_entry.get()
    cursor.execute("INSERT INTO bookmarks (name, link) VALUES (?, ?)", (name, link))
    conn.commit()
    name_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)
    display_bookmarks()

# Function to display bookmarks in the listbox
def display_bookmarks():
    bookmarks_listbox.delete(0, tk.END)  # Clear the listbox
    cursor.execute("SELECT * FROM bookmarks")
    bookmarks = cursor.fetchall()
    for bookmark in bookmarks:
        id, name, link = bookmark[0], bookmark[1], bookmark[2]
        bookmarks_listbox.insert(tk.END, f"Name: {name}\nLink: {link}\n")
        bookmarks_listbox.itemconfig(tk.END, {'bg': 'lightblue'})

# Function to delete a bookmark
# Function to delete a bookmark
def delete_bookmark():
    selected_item = bookmarks_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        bookmarks_listbox.delete(index)
        bookmark_info = bookmarks_listbox.get(index)
        name, link = bookmark_info.split('\n')[0][6:], bookmark_info.split('\n')[1][5:]
        cursor.execute("DELETE FROM bookmarks WHERE name=? AND link=?", (name, link))
        conn.commit()


# Function to modify a bookmark
def modify_bookmark():
    selected_item = bookmarks_listbox.curselection()
    if selected_item:
        index = selected_item[0]
        bookmark_info = bookmarks_listbox.get(index)
        name, link = bookmark_info.split('\n')[0][6:], bookmark_info.split('\n')[1][5:]

        # Create a new window for modifying the bookmark
        modify_window = tk.Toplevel(root)
        modify_window.title("Modify Bookmark")

        # Entry fields for modification
        name_label = tk.Label(modify_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(modify_window)
        name_entry.pack()
        name_entry.insert(0, name)

        link_label = tk.Label(modify_window, text="Link:")
        link_label.pack()
        link_entry = tk.Entry(modify_window)
        link_entry.pack()
        link_entry.insert(0, link)

        # Save modification button
        save_button = ttk.Button(modify_window, text="Save", command=lambda: save_modification(name, link, name_entry.get(), link_entry.get()))
        save_button.pack()



# Function to save modifications
def save_modification(old_name, old_link, new_name, new_link):
    cursor.execute("UPDATE bookmarks SET name=?, link=? WHERE name=? AND link=?", (new_name, new_link, old_name, old_link))
    conn.commit()
    display_bookmarks()
    root.focus_set()  # Return focus to the main window

# Create a Tkinter GUI
root = tk.Tk()
root.title("Bookmark Manager")

# Create a frame for bookmarks with a vertical scrollbar
bookmarks_frame = ttk.Frame(root)
bookmarks_frame.pack(fill='both', expand=True)

scrollbar = ttk.Scrollbar(bookmarks_frame, orient='vertical')
scrollbar.pack(side='right', fill='y')

# Create a listbox for displaying bookmarks
bookmarks_listbox = tk.Listbox(bookmarks_frame, yscrollcommand=scrollbar.set)
bookmarks_listbox.pack(fill='both', expand=True)

scrollbar.config(command=bookmarks_listbox.yview)

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

link_label = tk.Label(root, text="Link:")
link_label.pack()
link_entry = tk.Entry(root)
link_entry.pack()

add_button = ttk.Button(root, text="Add Bookmark", command=add_bookmark)
add_button.pack()

delete_button = ttk.Button(root, text="Delete Bookmark", command=delete_bookmark)
delete_button.pack()

modify_button = ttk.Button(root, text="Modify Bookmark", command=modify_bookmark)
modify_button.pack()

display_bookmarks()

root.mainloop()

# Close the database connection when the GUI is closed
conn.close()
