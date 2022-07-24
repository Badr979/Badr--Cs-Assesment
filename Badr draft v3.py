from tkinter import*
from tkinter import ttk

main_window=Tk()

customer_details = []
all_entries = 0



Title = ttk.Label(main_window, text="Julie's Tracker", font=("Helvetica 20 bold"))
Title.grid(row=0, column= 0, columnspan=2)


### entry boxes and labels

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
    Label(main_window, text="Row").grid(column=0, row=9)
    Label(main_window, text="Customer Name").grid(column=1, row=9)
    Label(main_window, text="Item hired").grid(column=2, row=9)
    Label(main_window, text="Item Quantity").grid(column=3, row=9)
    Label(main_window, text="Reciept number").grid(column=4, row=9)
    Label(main_window, text=name_count).grid(column=0, row=name_count+10)
    Label(main_window, text=(customer_details[name_count][0])).grid(column=1, row=name_count+10)
    Label(main_window, text=(customer_details[name_count][1])).grid(column=4, row=name_count+10)
    Label(main_window, text=(customer_details[name_count][2])).grid(column=2, row=name_count+10)
    Label(main_window, text=(customer_details[name_count][3])).grid(column=3, row=name_count+10)
    name_count += 1
    print(name_count)
   







def quit():
    main_window.destroy()
   

button_print = ttk.Button(main_window, text="Print details", command=print_details)
button_quit = ttk.Button(main_window, text="Quit", command=quit)
button_print.grid(row=7, column=1)
button_quit.grid(row=7, column=2)






#Running the Interface
def main():
    global main_window
    global name
    main_window.mainloop()
   

main()

main_window.geometry("500x450")
main_window.mainloop()

