# URL SHORTENER ReadMe FILE
URL Shortener is a simple program written in Python to shorten long URLs. 
It features a user-friendly interface built using Tkinter library. 
URLs are shortened using the pyshorteners library with the tinyurl service. New URL's are valid lifetime and do not expire.

![Static Badge](https://img.shields.io/badge/python-tkinter-blue)
![Static Badge](https://img.shields.io/badge/Version-2.0-green)

## CONTENTS
1. [How to Use](#how-to-use)
2. [Error Handling](#error-handling)
3. [Versions and Changes](#versions-and-changes)
4. [Known Issues](#known-issues)

## How to Use and Set up

### Installing
Download main.py, constants, gui_utils and url_shortener.
You need Python >3.6 presintalled.
Install pyshorteners module:
```
 pip install pyshorteners 
```
Run main.py.
### Shorten any URL
Copy the URL you want to shorten and paste it into the first field.
Click on the "Shorten URL" button. The shortened URL will appear in the second field below.
You can copy your new URL to the clipboard using the "Copy" button.
The generated URL is permanent and will always be valid.

## Error Handling
The URL field cannot be left blank. If left empty, you will receive a warning and the program will not execute.
## Versions and Changes
🔻Version 2.0 - 26.03.2024
- Code broken into smaller functions and classes.
- More Modular: easier to handle.
- All versions of 1.0 removed.
- ReadMe file updated.

🔻Version 1.02 - 25.03.2024
- Top menu added. File, Edit, Tools, Help created.
- File, Help contents created.
- Documentation, Licence, About sections added.

🔻Version 1.01: - 24.03.2024
- Added a Clear Clipboard button and function.
- ReadMe file created.
- MIT licence added.

🔻Version 1.0: - 21.03.2024
- Added Shorten URL and Copy buttons.
- Created a user interface using Tkinter.

## Known Issues
- Undo & Redo in Edit menu not working.

![urlshort](https://github.com/storlak/URL-shortener/assets/101433369/f446dd74-5c02-4790-b029-2bcd2458e8ba)

