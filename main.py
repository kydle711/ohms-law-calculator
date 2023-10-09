import tkinter
import customtkinter as ctk

# Functions for conversions
def calculate():
    if calc_selector.get() == "Volts":
        ohms_value = float(ohms_entry.get())
        amps_value = float(amps_entry.get())
        volts_value = ohms_value * amps_value
        print(volts_value)
        volts_var.set(str(round(volts_value, 2)))

    elif calc_selector.get() == "Amps":
        ohms_value = float(ohms_entry.get())
        volts_value = float(volts_entry.get())
        amps_value = volts_value/ohms_value
        print(amps_value)
        amps_var.set(str(round(amps_value, 2)))

    elif calc_selector.get() == "Ohms":
        volts_value = float(volts_entry.get())
        amps_value = float(amps_entry.get())
        ohms_value = volts_value/amps_value
        print(ohms_value)
        ohms_var.set(str(round(ohms_value, 2)))





def reconfigure(choice):
    if choice == "Amps":
        amps_entry.configure(state='disabled')
        amps_var.set("")
        volts_entry.configure(state='normal')
        ohms_entry.configure(state='normal')
    elif choice == "Volts":
        volts_entry.configure(state='disabled')
        volts_var.set("")
        amps_entry.configure(state='normal')
        ohms_entry.configure(state='normal')
    elif choice == "Ohms":
        ohms_entry.configure(state='disabled')
        ohms_var.set("")
        volts_entry.configure(state='normal')
        amps_entry.configure(state='normal')


#Build app GUI with permanent labels and buttons, configure
app = ctk.CTk()
app.geometry("600x600")
app.title("Ohm's Law Calculator")
app.configure(fg_color='gray')

#selection menu for conversion
selection = ctk.StringVar(value="")
calc_selector = ctk.CTkOptionMenu(app, width=120, height=80, dropdown_fg_color='white', font=('Helvetica bold', 24),
                                values=['Amps', 'Ohms', 'Volts'], fg_color='black', text_color='gray',
                                  dropdown_font=("Helvetica bold", 24), button_color='black',
                                  button_hover_color='purple', variable=selection, command=reconfigure)
calc_selector.place(relx=0.3, rely=0.8, anchor='center')


#calculate button
calculate_button = ctk.CTkButton(app, width=200, height=80, text_color='gray', hover_color='purple',
                                 text='CALCULATE', font=('Helvetica Bold', 24), fg_color='black', border_width=3,
                                 border_color='purple', command=calculate)
calculate_button.place(relx=0.7, rely=0.8, anchor='center')

#labels
amps_label = ctk.CTkLabel(app, width=150, height=60, text_color='black', text='AMPS', font=('Helvetica bold', 24))
amps_label.place(relx=0.3, rely=0.1, anchor='center')

ohms_label = ctk.CTkLabel(app, width=150, height=60, text_color='black', text='OHMS', font=('Helvetica bold', 24))
ohms_label.place(relx=0.3, rely=0.3, anchor='center')

volts_label = ctk.CTkLabel(app, width=150, height=60, text_color='black', text='VOLTS', font=('Helvetica bold', 24))
volts_label.place(relx=0.3, rely=0.5, anchor='center')

#entry variables and fields
volts_var = ctk.StringVar(value="")
amps_var = ctk.StringVar(value="")
ohms_var = ctk.StringVar(value="")

volts_entry = ctk.CTkEntry(app, textvariable=volts_var, width=150, height=60, text_color='gray', font=("Helvetica "
                                                                                                       "bold", 24),
                           fg_color='black')
volts_entry.place(relx=0.7, rely=0.5, anchor='center')


amps_entry = ctk.CTkEntry(app, textvariable=amps_var, width=150, height=60, text_color='gray', font=("Helvetica "
                                                                                                      "bold", 24),
                          fg_color='black')

amps_entry.place(relx=0.7, rely=0.1, anchor='center')


ohms_entry = ctk.CTkEntry(app, textvariable=ohms_var, width=150, height=60, text_color='gray', font=("Helvetica "
                                                                                                       "bold", 24),
                          fg_color='black')
ohms_entry.place(relx=0.7, rely=0.3, anchor='center')


#main

app.mainloop()



