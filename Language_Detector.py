'''This is a Language Identifier program which identifies the text written in which language.
credit :- @scratch_py_coder '''
import tkinter as tk
from langdetect import detect
def show_output():
    input_text = input_entry.get()
    code=detect(input_text)
    result=codes[code]
    output_label.config(text=result)
    
def clear_input():
    input_entry.delete(0, 'end')
    output_label.config(text="")

# Creating the main window
root = tk.Tk()
root.title("Language Detector")

codes={
 'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
 'sq': 'Albanian','bn': 'Bangla', 'bh': 'Bhojpuri',
'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
 'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
 'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
 'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
 'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
 'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
'te': 'Telugu', 'ta': 'Tamil','cy':'Welsh'}

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

# Creating input box
input_entry = tk.Entry(root, width=30)
input_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

#@scratch_py_coder

# Create a sbumit button
submit_button = tk.Button(root, text="Submit", command=show_output , font=('Helvetica', 12))
submit_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create a button to clear input
clear_button = tk.Button(root, text="Clear", command=clear_input, font=('Helvetica', 12))
clear_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a label to show the output
output_label = tk.Label(root, text="")
output_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
#@scratch_py_coder
