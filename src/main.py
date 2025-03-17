import tkinter as tk
import math
from tkinter import Canvas, PhotoImage



if __name__ == "__main__":


    WIDTH, HEIGHT = 600, 600
    window = tk.Tk() 
    window.title("Mandelbrodt Visualisation")
    window.resizable(False, False)

    window.columnconfigure(0, minsize=600)
    window.columnconfigure(1, minsize=200)
    window.rowconfigure(0, minsize=600)
    window.rowconfigure(1, minsize=200)

    #configure functions
    def zoom_in():
        print("Zoom in")
        return
    
    def zoom_out():
        print("Zoom out")
        return
    
    def run_calculation():
        print("Run calculation")

    def go_up():
        print("Go up")
        return
    
    def go_down():
        print("Go down")
        return
    
    def go_left():
        print("Go left")
        return
    
    def go_right():
        print("Go right")
        return



    #configure and display first frame containing the canvas
    fr_upper = tk.Frame(window, borderwidth=5, relief=tk.GROOVE) #todo: make frame bigger than canvas
    canvas = Canvas(fr_upper, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    fr_upper.pack(fill=tk.BOTH)


    fr_lower = tk.Frame(window, borderwidth=5, relief=tk.GROOVE)
    fr_lower.pack(fill=tk.BOTH)
    fr_lower.columnconfigure(0, minsize=220)
    fr_lower.columnconfigure([1,2], minsize=150)

    #configure and display second frame containing the iterations and coordinates
    #todo: create labels and entries via loop as in address_form.py
    #todo: preset slider with value

    fr10 = tk.Frame(fr_lower)
    lbl0 = tk.Label(fr10, text="max. Iteration per Pixel")
    lbl1 = tk.Label(fr10, text="x_min")
    lbl2 = tk.Label(fr10, text="x_max")
    lbl3 = tk.Label(fr10, text="y_min")
    lbl4 = tk.Label(fr10, text="y_max")
    sld0 = tk.Scale(fr10, from_=0, to=10000, orient="horizontal")
    ent1 = tk.Entry(fr10)
    ent2 = tk.Entry(fr10)
    ent3 = tk.Entry(fr10)
    ent4 = tk.Entry(fr10)

    lbl0.grid(row=0, column=0)
    sld0.grid(row=0, column=1)
    lbl1.grid(row=1, column=0)
    ent1.grid(row=1, column=1)
    lbl2.grid(row=2, column=0)
    ent2.grid(row=2, column=1)
    lbl3.grid(row=3, column=0)
    ent3.grid(row=3, column=1)
    lbl4.grid(row=4, column=0)
    ent4.grid(row=4, column=1)

    fr10.grid(row=0, column=0, sticky="nsew")

    #configure and display the third frame containing the zoom controls
    fr01 = tk.Frame(fr_lower)

    #todo: replace with arrow symbols
    #add button commands
    btn0 = tk.Button(fr01, text="Zoom in", command=zoom_in)
    btn5 = tk.Button(fr01, text="Zoom out", command=zoom_out)

    fr01_in = tk.Frame(fr01)

    btn1 = tk.Button(fr01_in, text="^", command=go_up)
    btn2 = tk.Button(fr01_in, text="<", command=go_left)
    btn3 = tk.Button(fr01_in, text=">", command=go_right)
    btn4 = tk.Button(fr01_in, text="v", command=go_down)
    btn1.grid(row = 0, column=1, sticky="n")
    btn2.grid(row=1, column=0, sticky="w")
    btn3.grid(row=1, column=2, sticky="e")
    btn4.grid(row=2, column=1, sticky="s")

    btn0.pack(fill=tk.BOTH)
    fr01_in.pack()
    btn5.pack(fill=tk.BOTH)

    fr01.grid(row=0, column=1, sticky="nsew")

    #configure and display the fourth frame containing the start button and feedback
    fr11 = tk.Frame(fr_lower)
    btn_start = tk.Button(fr11, text="Run!", command=run_calculation)
    lbl_space= tk.Label(fr11, text=" ")
    lbl_runtime = tk.Label(fr11, text="Runtime:")
    lbl_runtime_val = tk.Label(fr11, text="0 s")
    lbl_iterations = tk.Label(fr11, text="Total iterations:")
    lbl_iterations_val = tk.Label(fr11, text="0")
    btn_start.pack()
    lbl_space.pack()
    lbl_runtime.pack()
    lbl_runtime_val.pack()
    lbl_iterations.pack()
    lbl_iterations_val.pack()

    fr11.grid(row=0, column=2, sticky="nsew")


    #prepopulate entry elements and slider with values

    def set_text(entry_widget, text):
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, text)
        return
    
    set_text(ent1, "-2.0")
    set_text(ent2, "1.0")
    set_text(ent3, "-1.0")
    set_text(ent4, "1.0")

    sld0.set(1000)

    # todo: access pixels on the canvas via their mathematical Im, Re coordinates
    # does the windows refresh every time a pixel is drawn autmatically?

    '''canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if x%2 == 0 and y%2 == 1:
                img.put("#ffffff", (x,y))'
    '''
    window.mainloop()