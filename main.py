import tkinter
from tkinter import ttk
import webbrowser
import url_shortener
import gui_utils
import menu_utils
from constants import *


# Shorten URL function
def shorten():
    url = longurl_entry.get().strip()
    if not url:
        gui_utils.show_error_message("Error", "Please enter a URL.")
        return

    try:
        short_url = url_shortener.shorten_url(url)
        if short_url:
            shorturl_entry.delete(0, tkinter.END)
            shorturl_entry.insert(0, short_url)
    except Exception as e:
        gui_utils.show_error_message(
            "Error", f"An error occurred while shortening the URL: {str(e)}"
        )


# Copy shortened URL to clipboard
def copyurl():
    shortened_url = shorturl_entry.get()
    if shortened_url:
        root.clipboard_clear()
        root.clipboard_append(shortened_url)
        root.update()
        gui_utils.show_info_message("Success", "Shortened URL copied to clipboard.")
    else:
        gui_utils.show_warning_message("Warning", "Shortened URL not found.")


# Function to clear data in both entries
def clear_entries():
    longurl_entry.delete(0, tkinter.END)
    shorturl_entry.delete(0, tkinter.END)


# Function for About dialog
def about():
    current_date = "15.05.2024"
    gui_utils.show_info_message(
        "About",
        f"{APP_NAME}\nVersion: {APP_VERSION}\nAuthor: {AUTHOR}\nLast Update: {current_date}",
    )


# Opens the README in Github
def open_readme():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/URL-shortener/blob/main/README.md"
    )


def welcome():
    menu_utils.open_url_in_browser("https://github.com/storlak/URL-shortener")


# Opens the License file in Github
def open_license():
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/URL-shortener/blob/main/LICENSE"
    )


root = tkinter.Tk()
root.title(APP_NAME)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=BACKGROUND_COLOR)

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
edit_menu.add_command(label="Clear Clipboard", command=clear_entries)
edit_menu.add_separator()
edit_menu.add_command(label="Shorten URL", command=shorten)
edit_menu.add_command(label="CopyShort URL", command=copyurl)

# Tools menu
tools_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Quick Commands")

# Help menu
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome", command=welcome)
help_menu.add_command(label="Documentation", command=open_readme)
help_menu.add_separator()
help_menu.add_command(label="View Licence", command=open_license)
help_menu.add_separator()
help_menu.add_command(label="About", command=about)

# Labels, entries, widgets
longurl_label = tkinter.Label(
    root, text="Enter a long URL to Shorten", fg=TEXT_COLOR, bg=BACKGROUND_COLOR
)
longurl_entry = tkinter.Entry(root, width=35)
shorten_button = tkinter.Button(
    root, text="Shorten URL", fg="black", bg="Turquoise", command=shorten
)
separator = ttk.Separator(root, orient="horizontal")
shorturl_label = tkinter.Label(
    root, text="Shortened URL", fg=TEXT_COLOR, bg=BACKGROUND_COLOR
)
shorturl_entry = tkinter.Entry(root, width=35)
copyurl_button = tkinter.Button(
    root, text="Copy", fg="black", bg="Turquoise", command=copyurl
)
bot_label = tkinter.Label(
    root, text=f"Version: {APP_VERSION} - {AUTHOR}", fg="black", bg="Turquoise"
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
