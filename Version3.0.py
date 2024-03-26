import tkinter
from tkinter import ttk
import pyshorteners
import tkinter.messagebox
import webbrowser


# Shorten URL function
def shorten():
    url = longurl_entry.get().strip()  # Check the URL line. It should not be empty!
    if not url:
        tkinter.messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        shorturl_entry.delete(
            0, tkinter.END
        )  # Clear previous content from the clipboard.
        shorturl_entry.insert(0, short_url)
    except pyshorteners.exceptions.ShorteningErrorException:
        tkinter.messagebox.showerror(
            "Error",
            "An error occurred while shortening the URL. Please enter a valid URL.",
        )
    except pyshorteners.exceptions.ServiceException:
        tkinter.messagebox.showerror(
            "Error",
            "URL shortening service is currently unavailable. Please try again later.",
        )
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Copy shortened URL to clipboard
def copyurl():
    shortened_url = shorturl_entry.get()
    if shortened_url:
        root.clipboard_clear()
        root.clipboard_append(shortened_url)
        root.update()
        tkinter.messagebox.showinfo("Success", "Shortened URL copied to clipboard.")
    else:
        tkinter.messagebox.showwarning("Warning", "Shortened URL not found.")


# Function to clear data in both entries
def clear_entries():
    longurl_entry.delete(0, tkinter.END)
    shorturl_entry.delete(0, tkinter.END)


# Function for Undo operation
def undo():
    pass


# Function for Redo operation
def redo():
    pass


# Shows an information message to user
def about():
    current_date = "26.03.2024"
    tkinter.messagebox.showinfo(
        "About",
        f"URL-Shortner \nVersion: 3.0 \nAuthor: Kazure\nLast Update: {current_date}",
    )


# Opens the README in Github
def open_readme():
    webbrowser.open_new("https://github.com/storlak/URL-shortener/blob/main/README.md")


# Opens the License file in Github
def open_license():
    webbrowser.open_new("https://github.com/storlak/URL-shortener/blob/main/LICENSE")


root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x275")
root.configure(bg="gray16")

# menu bar
menubar = tkinter.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_command(label="Clear", command=clear_entries)
edit_menu.add_separator()
edit_menu.add_command(label="Shorten URL", command=shorten)
edit_menu.add_command(label="CopyShort URL", command=copyurl)

# Tools menu
tools_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)

# Help menu
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome", command=about)
help_menu.add_command(label="Documentation", command=open_readme)
help_menu.add_separator()
help_menu.add_command(label="View Licence", command=open_license)
help_menu.add_separator()
help_menu.add_command(label="About", command=about)

# Labels, entries, widgets
longurl_label = tkinter.Label(
    root, text="Enter a long URL to Shorten", fg="#FFFFFF", bg="gray16"
)
longurl_entry = tkinter.Entry(root, width=35)
shorten_button = tkinter.Button(
    root, text="Shorten URL", fg="black", bg="Turquoise", command=shorten
)
separator = ttk.Separator(root, orient="horizontal")
shorturl_label = tkinter.Label(root, text="Shortened URL", fg="#FFFFFF", bg="gray16")
shorturl_entry = tkinter.Entry(root, width=35)
copyurl_button = tkinter.Button(
    root, text="Copy", fg="black", bg="Turquoise", command=copyurl
)
bot_label = tkinter.Label(
    root, text="Version: 3.0 - Kazure", fg="black", bg="Turquoise"
)

# Placing widgets, labels, entries
longurl_label.pack(pady=5)
longurl_entry.pack()
shorten_button.pack(pady=5)
separator.pack(fill="x", padx=5, pady=5)
shorturl_label.pack(pady=5)
shorturl_entry.pack()
copyurl_button.pack(pady=5)
bot_label.pack(side="bottom", fill="x")

# Clear button
clear_button = tkinter.Button(
    root, text="Clear Clipboard", fg="black", bg="Turquoise", command=clear_entries
)
clear_button.pack(pady=5)

root.mainloop()