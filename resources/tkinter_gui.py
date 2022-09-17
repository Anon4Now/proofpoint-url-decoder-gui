"""Module containing tkinter GUI geometry and input"""

# Standard Library imports
import tkinter as tk
from tkinter import Tk, Text, END
from typing import Optional


class DecoderGUIInput:
    """Action-oriented class containing the Geometry and input fields for Tkinter GUI"""

    # Set the GUI Geometry during object instantiation
    def __init__(self):
        #  This is all related to setting the Geometry of the GUI
        self.root = tk.Tk()
        self.root.geometry("400x50")
        self.root.title("ProofPoint Decoder")
        self.root.configure(bg='#16325c')
        self.entry = tk.Entry(self.root, bd=1)
        self.entry.config(fg='grey')
        self.entry.pack(side="left")
        self.entry.pack()
        self.entry.grid(row=1,
                        column=0,
                        padx=7,
                        pady=10,
                        ipadx=130,
                        ipady=3)

        self.result: str = ""  # this is the actual text that is being provided by the user

    # Event listeners for user text entry
    def _on_entry_click(self, event: Optional[tk.Event]) -> None:
        """
        Method that handles the greyed out text once a user clicks into the input field.
        :param event: (required) This event listener param is needed due to the Tkinter program logic
        :return: None
        """
        if self.entry.get() == 'Paste encoded URL and press <ENTER>...':
            self.entry.delete(0, "end")  # delete all the text in the entry
        self.entry.insert(0, '')  # Insert blank for user input
        self.entry.config(fg='black')

    # Event listeners for user text entry
    def _on_focusout(self, event: Optional[tk.Event]) -> None:
        """
        Method that handles the greyed out text once a user clicks out of the input field.
        :param event: (required) This event listener param is needed due to the Tkinter program logic
        :return: None
        """
        if self.entry.get() == '':
            self.entry.insert(0, 'Paste encoded URL and press <ENTER>...')
            self.entry.config(fg='grey')

    # Event listeners for user text entry
    def _callback(self, event: Optional[tk.Event]) -> None:
        """
        Method that takes the inputted text from user and destroys the running GUI process.
        :param event: (required) This event listener param is needed due to the Tkinter program logic
        :return: None
        """
        self.result = self.entry.get()
        self.root.destroy()

    def binding(self) -> str:
        """
        Method that binds the individual methods to the event listeners and makes GUI actions
        :return: String containing the input field entry from user
        """
        self.entry.insert(0, 'Paste encoded URL and press <ENTER>...')
        self.entry.bind('<FocusIn>', self._on_entry_click)
        self.entry.bind('<FocusOut>', self._on_focusout)
        self.entry.bind("<Return>", self._callback)
        self.root.mainloop()
        return self.result


def display_result(result_input) -> None:
    """
    Function that takes in a 'decoded' string value (e.g., URL)
    and displays it on a newly created GUI.
    :param result_input: String value containing the 'decoded' data from the user
    :return: None
    """
    root_out = Tk()  # instantiate the TK object
    root_out.geometry("400x50")  # set the output GUI geometry size
    root_out.title("ProofPoint Decoder Output")  # give it a title
    text = Text(root_out)  # display the inputted text to the GUI screen
    text.pack()
    text.insert(END, result_input)  # pass the string to the GUI
    root_out.mainloop()  # run the loop
