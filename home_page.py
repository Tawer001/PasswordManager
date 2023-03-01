import tkinter
import customtkinter
from tkinter import ttk


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Safe`T Manager")
        self.geometry("720x520")
        # self.minsize(600, 400)
        # self.maxsize(600, 400)

        # configure grid
        # self.grid_columnconfigure(1, )

        # create tabview
        self.tabview = customtkinter.CTkTabview(
            self, width=700, height=500, corner_radius=30)
        self.tabview.grid(row=1, column=1, padx=(
            10, 10), pady=(10, 10), sticky='wsen')

        self.tabview.add("Password Generator")
        self.tabview.add("Password Manager")
        self.tabview.add("Autofills")

        ##########################################

        self.tabview.tab(
            'Password Generator').grid_columnconfigure((1, 2, 3), weight=1)
        self.tabview.tab('Password Generator').grid_rowconfigure(
            (1, 2, 3, 4, 5, 6), weight=1)

        # Password Generator tab layout
        self.auto_generate_button = customtkinter.CTkButton(self.tabview.tab(
            'Password Generator'), text="Auto Generate Strong Password", command=None)
        self.auto_generate_button.grid(
            row=1, column=2, columnspan=2, padx=20, pady=20, sticky='snew')

        self.generated_password_label = customtkinter.CTkLabel(self.tabview.tab(
            'Password Generator'), text="Generated Password is : ", corner_radius=10, bg_color='grey')
        self.generated_password_label.grid(
            row=2, column=1, columnspan=3, padx=20, pady=15, sticky='snew')

        self.copy_password = customtkinter.CTkButton(
            self.tabview.tab('Password Generator'), text="Copy", command=None)
        self.copy_password.grid(
            row=2, column=4, padx=20, pady=15, sticky='snew')

        # password options frame
        self.password_options_frame = customtkinter.CTkFrame(
            self.tabview.tab('Password Generator'))
        self.password_options_frame.grid(
            row=3, column=1, rowspan=4, columnspan=2, padx=40, pady=15, sticky='snew')

        # password length
        self.password_length_value = customtkinter.CTkLabel(
            self.password_options_frame, bg_color='grey', text=" 15 ")
        self.password_length_value.grid(
            row=1, column=1, padx=10, pady=10, sticky='w')

        self.password_length_slider = customtkinter.CTkSlider(
            self.password_options_frame, from_=6, to=20, number_of_steps=12, command=None)
        self.password_length_slider.grid(
            row=1, column=1, columnspan=2, padx=50, pady=10, sticky='w')

        self.password_length_label = customtkinter.CTkLabel(
            self.password_options_frame, text="Password Length")
        self.password_length_label.grid(
            row=1, column=2, padx=(100, 10), pady=10, sticky='e')

        self.special_character_switch = customtkinter.CTkSwitch(
            self.password_options_frame, text="Special Characters", command=None)
        self.special_character_switch.grid(
            row=2, column=1, padx=10, pady=10, sticky='snew')

        self.custom_generate_button = customtkinter.CTkButton(self.tabview.tab(
            'Password Generator'), text="Generate Password", command=None)
        self.custom_generate_button.grid(
            row=3, column=4, rowspan=2, padx=20, pady=15, sticky='snew')

        ##########################################

        # Password Manager tab layout

        # Table frame
        self.table_frame = customtkinter.CTkFrame(
            self.tabview.tab('Password Manager'))
        self.table_frame.grid(row=1, column=1, columnspan=2,
                              padx=110, pady=20, sticky='snew')

        # Create a vertical scrollbar
        y_scrollbar = customtkinter.CTkScrollbar(
            self.table_frame, orientation='vertical')

        # Create a table
        self.password_table = ttk.Treeview(self.table_frame, columns=(
            'username', 'password'), show='headings', height=5, yscrollcommand=y_scrollbar.set)
        self.password_table.column('#1', anchor='center')
        self.password_table.heading('#1', text='username')
        self.password_table.column('#2', anchor='center')
        self.password_table.heading('#2', text='password')

        # Configure the scrollbar
        y_scrollbar.configure(command=self.password_table.yview)

        # Insert the data in the table
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))
        self.password_table.insert(
            '', 'end', text="1", values=('Amit', '17701'))
        self.password_table.insert(
            '', 'end', text="1", values=('Ankush', '17702'))

        # Pack the table and scrollbar
        self.password_table.pack(fill='both', side='left', padx=0)
        y_scrollbar.pack(side='right', padx=0)


def run_app():
    app = App()
    app.mainloop()

# app = App()
# app.mainloop()
