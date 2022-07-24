from tkinter import*
from tkinter import ttk

root=Tk()


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

def print_details():
    name_count = 0
    # Create the column headings
    Label(root, text="Row").grid(column=0, row=9)
    Label(root, text="Customer Name").grid(column=1, row=9)
    Label(root, text="Item hired").grid(column=2, row=9)
    Label(root, text="Item Quantity").grid(column=3, row=9)
    Label(root, text="Reciept number").grid(column=4, row=9)
    Label(root, text=name_count).grid(column=0, row=name_count+10)
    Label(root, text=(customer_details[name_count][0])).grid(column=1, row=name_count+10)
    Label(root, text=(customer_details[name_count][1])).grid(column=4, row=name_count+10)
    Label(root, text=(customer_details[name_count][2])).grid(column=2, row=name_count+10)
    Label(root, text=(customer_details[name_count][3])).grid(column=3, row=name_count+10)
    name_count += 1
    print(name_count)
    print_details()
def quit():
    root.destroy()

buttonPRNT = ttk.Button(root, text="Print details", command=print_details)
buttonQUIT = ttk.Button(root, text="Quit", command=quit)
buttonPRNT.grid(row=7, column=1, sticky=W+E, pady=5)
buttonQUIT.grid(row=7, column=2, sticky=W+E, pady=5)





#Running the Interface
def main():
    global main_window
    global name
    main_window =Tk()
    GUI()  

    main_window.title("Julie's Tracker")

    main_window.mainloop()

main()

root.geometry("500x450")
root.mainloop()

