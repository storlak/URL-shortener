import pyshorteners
import tkinter.messagebox


def shorten_url(url):
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url
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
