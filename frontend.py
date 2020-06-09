from tkinter import *
from backend import *


def find_page():
    address = e1.get()
    data = request_html_https(address)

    cframe = Frame(master)
    cframe.grid(row=1, column=0)
    page = Canvas(cframe, width=w - 10, height=h - 200)
    page.grid(row=0, column=0)
    hscroll = Scrollbar(cframe, orient=HORIZONTAL, command=page.xview)
    hscroll.grid(row=1, column=0, sticky='ew')
    vscroll = Scrollbar(cframe, orient=VERTICAL, command=page.yview)
    vscroll.grid(row=0, column=1, sticky='ns')


    if data.status_code == 200 :
        page.create_text(0, 0, text=data.text, anchor='nw')
    else:
        page.create_text(0, 0, text=f'Error happened couldn\'t download the page\n status code: {data.status_code}', anchor='nw')


    page.configure(xscrollcommand=hscroll.set)
    page.configure(yscrollcommand=vscroll.set)
    page.config(scrollregion=page.bbox("all"))


master = Tk()
master.title("Browser")
w, h = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (w, h))

search_frame = Frame(master)
search_frame.grid(row=0, column=0, sticky='nw')

Label(search_frame, text="URL").grid(row=0)
e1 = Entry(search_frame)
e1.grid(row=0, column=1, columnspan=4)

b1 = Button(search_frame, text="Go To Page", command=lambda: find_page())
b1.grid(row=0, column=6)




master.mainloop()
