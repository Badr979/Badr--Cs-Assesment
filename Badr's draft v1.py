from tkinter import*
from tkinter import ttk


def GUI(): #The Interface of the Program
    global full_name

    #Name
    Label(main_window, text="Customer Name :") .grid(row=1, column=1) #Making a Label for the Name Entry
    name = Entry(main_window)
    name.grid(row=1, column=2, padx=7, pady=7, columnspan=2) #pady and padx to put some space between the widgets 

    #Reciept
    Label(main_window, text="Reciept Number :") .grid(row=2, column=1) #Making a Label for the Reciept Number
    Reciept = Entry(main_window)
    Reciept.grid(row=2, column=2, padx=7, pady=7, columnspan=2)

    #What item was Hired
    Label(main_window, text="Item hired:") .grid(row=3, column=1) #Making a Label for the Item that was Hired
    item = Entry(main_window)
    item.grid(row=3, column=2, padx=7, pady=7, columnspan=2)

    #Quantity
    Label(main_window, text="Item Quantity :") .grid(row=4, column=1) #Making a Label for the Quantity of Items Hired
    quantity = Entry(main_window)
    quantity.grid(row=4, column=2, padx=7, pady=7, columnspan=2)





#Running the Interface
def main():
    global main_window
    global name
    main_window =Tk()
    GUI()  

    main_window.title("Julie's Tracker")

    main_window.mainloop()

main()
