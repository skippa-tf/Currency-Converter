from tkinter import *
from tkinter import ttk



class CurrencyConverter():
    """Overall class to manage GUI and button behavior"""

    def __init__(self):
        """Initialize needed attributes and creates the window."""
        self.currencies = ('CAD', 'USD', 'EUR', 'YEN')
        self.currency_exchange_rates = {'CAD': 1.24, 'USD': 1, 'EUR': 0.83, 'YEN': 108.13}
        self.root = Tk()
        self.root.title('Currency Converter')

        #Create the gui boxes
        self.entrybox = ttk.Entry(self.root, width=12)
        self.entrybox.grid(column=0, row=0, sticky='news')

        self.entrybox_two = self.create_entrybox(column=3)

        self.combobox_one = ttk.Combobox(self.root, values=self.currencies, state='readonly', width='4')
        self.combobox_one.set('USD')
        self.combobox_one.grid(column=1, row=0, sticky='news')

        self.combobox_two = ttk.Combobox(self.root, values=self.currencies, state='readonly', width='4')
        self.combobox_two.set('USD')
        self.combobox_two.grid(column=4, row=0, sticky='news')

        self.calculate_btn = self.create_calculate_btn(column=2)

        self.root.mainloop()


    def create_entrybox(self, column=0, row=0):
        """Creates an entry box"""
        self.entry_text = StringVar()
        entrybox = ttk.Entry(self.root, width=12, state=DISABLED, textvariable=self.entry_text)
        entrybox.grid(column=column, row=row, sticky='news')
    

    def create_calculate_btn(self, default_direction='->', column=0, row=0):
        """Creates the button to convert currencies"""
        button = ttk.Button(self.root, text=default_direction, command=self.calculate)
        button.grid(column=column, row=row, sticky='news')


    def calculate(self):
        """Converts the currencies when button is pushed"""
        exrate_one = self.currency_exchange_rates[self.combobox_one.get()]
        exrate_two = self.currency_exchange_rates[self.combobox_two.get()]
        self.total_two = (int(self.entrybox.get()) / exrate_one) * exrate_two
        self.entry_text.set(round(self.total_two, 2))
        



converter = CurrencyConverter()
