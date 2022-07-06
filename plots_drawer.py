from tkinter.tix import Tree
import requests
import tkinter as tk
from tkinter import CENTER,ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import font as tkFont
from numpy import sin,cos,tan, log, pi 

expression = ""

root = tk.Tk()
# tytuł okna
root.title('Your Plots Drawer')
root.geometry('1310x800')
root.resizable(width=False, height=False)


def drawing_plots(func, dim, lenx, leny, name_x, name_y,title, leg):
    """Creating plot with given parametres and saving it to a file called 'fig_app.png'

    Keyword arguments:
    func -- chosen funcs
    """
    funcs = func.split(";")
    fig,ax = plt.subplots()
    dimx = tuple(map(int, lenx.split(',')))
    dimy = tuple(map(int, leny.split(',')))
    
    xs,xf = dimx
    x = np.arange(xs,xf,0.01)
    for f in funcs:
        if type(fun := eval(f)) == float : ax.hlines(fun,xmin = xs, xmax = xf)
        else : ax.plot(x,fun)    
    ax.set_xlim(dimx)
    if leg:
        ax.legend(funcs, loc = "upper right")
    ax.set_ylim(dimy)
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.set_title(title)
    ax.grid(True, linestyle = "-.")
    plt.savefig('fig_app.png')

def draw():
    drawing_plots(input.get(), x_dim.get(),  x_dim.get(),  y_dim.get(), x_title.get(),y_title.get(), title.get(), legend.get())
    plot = Image.open("fig_app.png")
    plot = ImageTk.PhotoImage(plot)
    plot_label = tk.Label(image = plot)
    plot_label.image = plot
    plot_label.place(x = 650, y = 100)

def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""

def delete():
    a = input.get()
    input.delete(first=len(a)-1,last="end")

expression = ""

helv = tkFont.Font(family='Helvetica', size=20, weight='bold')

logo = Image.open("logo_math.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid()

input_text = tk.StringVar()
input_text.set("")
input = tk.Entry(root, width = 60, bg = "white", bd = 5, textvariable=input_text, font = helv, justify=CENTER)
input.place(x = 150, y = 150, height=50, width=360)

#BUTTONS_NUM
button_1 = tk.Button(text = "(", width = 2, height=2, bg = "white", font = helv, command = lambda : click("("))
button_1.place(x = 150, y = 220)
button_2 = tk.Button(text = ")", width = 2, height=2, bg = "white", font = helv, command = lambda : click(")"))
button_2.place(x = 225, y = 220)
button_pi = tk.Button(text = "\u03C0", width = 2, height=2, bg = "white", font = helv, command = lambda : click("pi"))
button_pi.place(x = 300, y = 220)
button_x = tk.Button(text = "x", width = 2, height=2, bg = "white", font = helv, command = lambda : click("x"))
button_x.place(x = 375, y = 220)
button_plus = tk.Button(text = "+", width = 2, height=2, bg = "white", font = helv, command = lambda : click("+"))
button_plus.place(x = 450, y = 220)
button_minus = tk.Button(text = "-", width = 2, height=2, bg = "white", font = helv, command = lambda : click("-"))
button_minus.place(x = 450, y = 300)
button_sin = tk.Button(text = "sin", width = 2, height=2, bg = "white", font = helv, command = lambda : click("sin"))
button_sin.place(x = 150, y = 300)
button_cos = tk.Button(text = "cos", width = 2, height=2, bg = "white", font = helv, command = lambda : click("cos"))
button_cos.place(x = 225, y = 300)
button_tg = tk.Button(text = "tg", width = 2, height=2, bg = "white", font = helv, command = lambda : click("tan"))
button_tg.place(x = 300, y = 300)
button_ctg = tk.Button(text = "ctg", width = 2, height=2, bg = "white", font = helv, command = lambda : click("ctag"))
button_ctg.place(x = 375, y = 300)
button_zero = tk.Button(text = "0", width = 2, height=2, bg = "white", font = helv, command = lambda : click(0))
button_zero.place(x = 150, y = 380)
button_one = tk.Button(text = "1", width = 2, height=2, bg = "white", font = helv, command = lambda : click(1))
button_one.place(x = 225, y = 380)
button_two = tk.Button(text = "2", width = 2, height=2, bg = "white", font = helv, command = lambda : click(2))
button_two.place(x = 300, y = 380)
button_three = tk.Button(text = "3", width = 2, height=2, bg = "white", font = helv, command = lambda : click(3))
button_three.place(x = 375, y = 380)
button_div = tk.Button(text = "/", width = 2, height=2, bg = "white", font = helv, command = lambda : click("/"))
button_div.place(x = 450, y = 380)
button_ln = tk.Button(text = "ln", width = 2, height=2, bg = "white", font = helv, command = lambda : click("log"))
button_ln.place(x = 150, y = 460)
button_four = tk.Button(text = "4", width = 2, height=2, bg = "white", font = helv, command = lambda : click("4"))
button_four.place(x = 225, y = 460)
button_five = tk.Button(text = "5", width = 2, height=2, bg = "white", font = helv, command = lambda : click("5"))
button_five.place(x = 300, y = 460)
button_six = tk.Button(text = "6", width = 2, height=2, bg = "white", font = helv, command = lambda : click("6"))
button_six.place(x = 375, y = 460)
button_mult = tk.Button(text = "*", width = 2, height=2, bg = "white", font = helv, command = lambda : click("*"))
button_mult.place(x = 450, y = 460)
button_log = tk.Button(text = ".", width = 2, height=2, bg = "white", font = helv, command = lambda : click("."))
button_log.place(x = 150, y = 540)
button_7 = tk.Button(text = "7", width = 2, height=2, bg = "white", font = helv, command = lambda : click("7"))
button_7.place(x = 225, y = 540)
button_8 = tk.Button(text = "8", width = 2, height=2, bg = "white", font = helv, command = lambda : click("8"))
button_8.place(x = 300, y = 540)
button_9 = tk.Button(text = "9", width = 2, height=2, bg = "white", font = helv, command = lambda : click("9"))
button_9.place(x = 375, y = 540)
button_eq = tk.Button(text = "=", width = 2, height=2, bg = "white", font = helv, command = lambda : click("="))
button_eq.place(x = 450, y = 540)

#ax x
ax_x_title = tk.Label(text = "x title:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
ax_x_title.place(x = 125, y = 640)
x_title = tk.Entry(root, width = 20, bg = "white", bd = 5, font = helv, justify=CENTER)
x_title.place(x = 275, y = 640, height=50, width=200)
#xrange
x_range = tk.Label(text = "x range:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
x_range.place(x = 125 , y = 725)
x_dim = tk.Entry(root, width = 20, font = helv, bg = "white", bd = 5, justify=CENTER)
x_dim.place(x = 265, y = 725,height=50, width=150)
#ax y
ax_y_title = tk.Label(text = "y title:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
ax_y_title.place(x = 525, y = 640)
y_title = tk.Entry(root, width = 20, bg = "white", bd = 5, font = helv, justify=CENTER)
y_title.place(x = 675, y = 640, height=50, width=200)
#yrange
y_range = tk.Label(text = "y range:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
y_range.place(x = 455 , y = 725)
y_dim = tk.Entry(root, width = 20, font = helv, bg = "white", bd = 5, justify=CENTER)
y_dim.place(x = 605, y = 725,height=50, width=150)
#title
ax_title= tk.Label(text = "title:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
ax_title.place(x = 925, y = 640)
title = tk.Entry(root, width = 20, bg = "white", bd = 5, font = helv, justify=CENTER)
title.place(x = 1075, y = 640, height=50, width=200)
#legend
legend_label = tk.Label(text = "legend:", height = 1, width = 8, font = helv, bg = "white", bd = 5)
legend_label.place(x = 800, y = 725)
legend = ttk.Combobox(height = 1, width = 8, font = helv)
legend["values"] = [True, False]
legend.place(x = 950, y = 725 )


#draw
button_draw = tk.Button(text = "Draw!", width = 5, height=2, bg = "white", font = helv, command = draw)
button_draw.place(x = 525, y = 150)
#clear
clear = tk.Button(text = "Clear!", width = 5, height = 2, bg = "white", command =clear, font = helv)
clear.place(x = 525, y = 220)
#quit
quit_button = tk.Button(text = "Quit", width = 10, height= 1,font = helv,bg = "white", command = root.quit)
quit_button.place(x = 1090, y = 725)


root.mainloop()