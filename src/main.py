import tkinter as tk
import time
from tkinter import Canvas, PhotoImage



if __name__ == "__main__":

    WIDTH, HEIGHT = 600, 400

    #create and configure the window
    window = tk.Tk() 
    window.title("Mandelbrodt Visualisation")
    window.resizable(False, False)
    window.columnconfigure(0, minsize=600)
    window.columnconfigure(1, minsize=200)
    window.rowconfigure(0, minsize=600)
    window.rowconfigure(1, minsize=200)

    def dec_to_hex_str(number):
        """turn a decimal number into a hex string and add a 0 if needed to make its length even"""
        key = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        result = ""
        while number>15:
            rest = number%16
            number = number // 16
            result = key[rest] + result
        result = key[number] + result
        if len(result)%2 == 1:
            result = "0" + result
        return result
    
    def create_colors():
        """create an array filled with rgb color values"""
        color_memory = []
        for a in range(1, 200, 5):
            color_memory.append(["#ffff" + dec_to_hex_str(a)])
        for a in range(1, 200, 5):
            color_memory.append(["#" + dec_to_hex_str(a) + "ff" + dec_to_hex_str(a)])
        for a in range(1, 200, 5):
            color_memory.append(["#" + dec_to_hex_str(a) + dec_to_hex_str(a) + "ff"])
        for a in range(1, 200, 5):
            color_memory.append(["#ff" + dec_to_hex_str(a) + dec_to_hex_str(a)])
        return color_memory

    class Fractal:
        def __init__(self, x_min, x_max, y_min, y_max, width, height, frame):

            self._x_min = x_min
            self._x_max = x_max
            self._y_min = y_min
            self._y_max = y_max
            self._width = width
            self._height = height
            self._frame = frame
            self._canvas = Canvas(frame, width=WIDTH, height=HEIGHT, bg="#ffffff")
            self._img = PhotoImage(width=WIDTH, height=HEIGHT)     
    
    def run_calculation():
        print("Run calculation")
        #get coordinates from entry elements
        fractal._x_min = float(ent1.get())
        fractal._x_max = float(ent2.get())
        fractal._y_min = float(ent3.get())
        fractal._y_max = float(ent4.get())
        max_iteration = sld0.get()
        amount_colors = len(colors)
        total_iterations = 0
        start_time = time.time()
        for x_canvas in range(WIDTH):
            for y_canvas in range(HEIGHT):
                fractal._img.put("#ffffff", (x_canvas, y_canvas)) #clear pixel
                xa = fractal._x_min + x_canvas * (fractal._x_max - fractal._x_min) / WIDTH
                ya = fractal._y_min + y_canvas * (fractal._y_max - fractal._y_min) / HEIGHT
                x = 0
                y = 0
                iteration = 0
                while (x+x + y*y <=4 and iteration < max_iteration):
                    xtemp = x*x - y*y + xa
                    y = 2*x*y + ya
                    x = xtemp
                    iteration += 1
                if iteration == max_iteration:
                    fractal._img.put("#000000", (x_canvas, y_canvas))
                else:
                    fractal._img.put(colors[iteration%amount_colors], (x_canvas, y_canvas))
                total_iterations += iteration
        lbl_iterations_val['text'] = str(total_iterations)
        lbl_runtime_val['text'] = "{0:.2f} s".format(time.time() - start_time)
        return

    
    def set_text(entry_widget, text):
        """push new content into an entry widget"""
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, text)
        return

    def coords_to_entry():
        """read the current fractal coordinates and push them to the corresponding entry widgets"""
        set_text(ent1, str(fractal._x_min))
        set_text(ent2, str(fractal._x_max))
        set_text(ent3, str(fractal._y_min))
        set_text(ent4, str(fractal._y_max))
        return

    #zoom and shift functions
    def zoom_in():
        print("Zoom in")
        x_min = fractal._x_min
        x_max = fractal._x_max
        y_min = fractal._y_min
        y_max = fractal._y_max
        fractal._x_min = x_min + ((x_max - x_min) * 0.25)
        fractal._x_max = x_max - ((x_max - x_min) * 0.25)
        fractal._y_min = y_min + ((y_max - y_min) * 0.25)
        fractal._y_max = y_max - ((y_max - y_min) * 0.25)
        coords_to_entry()
        return
        
    def zoom_out():
        print("Zoom out")
        x_min = fractal._x_min
        x_max = fractal._x_max
        y_min = fractal._y_min
        y_max = fractal._y_max
        fractal._x_min = x_min - ((x_max - x_min) * 0.5)
        fractal._x_max = x_max + ((x_max - x_min) * 0.5)
        fractal._y_min = y_min - ((y_max - y_min) * 0.5)
        fractal._y_max = y_max + ((y_max - y_min) * 0.5)
        coords_to_entry()
        return

    def go_up():
        print("Go up")
        y_min = fractal._y_min
        y_max = fractal._y_max
        fractal._y_min = y_min - ((y_max - y_min) * 0.25)
        fractal._y_max = y_max - ((y_max - y_min) * 0.25)        
        coords_to_entry()
        return
        
    def go_down():
        print("Go down")
        y_min = fractal._y_min
        y_max = fractal._y_max
        fractal._y_min = y_min + ((y_max - y_min) * 0.25)
        fractal._y_max = y_max + ((y_max - y_min) * 0.25)        
        coords_to_entry()
        return
        
    def go_left():
        print("Go left")
        x_min = fractal._x_min
        x_max = fractal._x_max
        fractal._x_min = x_min - ((x_max - x_min) * 0.25)
        fractal._x_max = x_max - ((x_max - x_min) * 0.25)
        coords_to_entry()
        return
        
    def go_right():
        print("Go right")
        x_min = fractal._x_min
        x_max = fractal._x_max
        fractal._x_min = x_min + ((x_max - x_min) * 0.25)
        fractal._x_max = x_max + ((x_max - x_min) * 0.25)
        coords_to_entry()
        return


    #configure and display the upper frame containing the canvas, create the fractal
    fr_upper = tk.Frame(window, borderwidth=5, relief=tk.GROOVE) 
    fractal = Fractal(-2.2, 1.2, -1.0, 1, WIDTH, HEIGHT, fr_upper)
    fractal._canvas.pack()
    fractal._canvas.create_image((WIDTH/2, HEIGHT/2), image=fractal._img, state="normal")
    fr_upper.pack(fill=tk.BOTH)
    fr_lower = tk.Frame(window, borderwidth=5, relief=tk.GROOVE)
    fr_lower.pack(fill=tk.BOTH)
    fr_lower.columnconfigure(0, minsize=220)
    fr_lower.columnconfigure([1,2], minsize=150)

    #configure and display second frame containing the iterations slider and coordinates
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

    #configure and display the third frame containing the zoom and shift controls
    fr01 = tk.Frame(fr_lower)
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


    #prepopulate entry elements and slider with values, create colors, start event handler
    coords_to_entry()
    colors = create_colors()
    sld0.set(1000)
    window.mainloop()