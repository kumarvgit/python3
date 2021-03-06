# try:
#     import tkinter
# except ImportError: # python 2
#     import Tkinter as tkinter
#
#
# def parablola(x):
#     y = x * x / 100
#     return y
#
#
# def draw_axes(canvas):
#     canvas.update()
#     x_origin = canvas.winfo_width() / 2
#     y_origin = canvas.winfo_height() / 2
#     canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
#     canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
#     canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
#
#
# def plot(canvas, x, y):
#     canvas.create_line(x, y, x + 1, y + 1, fill="red")
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("Parabola")
# mainWindow.geometry("640x480")
#
# canvas = tkinter.Canvas(mainWindow, width=640, height=480)
# canvas.grid(row=0, column=0)
#
# draw_axes(canvas)
#
# for x in range(-100, 100):
#     y = parablola(x)
#     plot(canvas, x, -y)
#
# mainWindow.mainloop()

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parablola(x):
    y = x * x / 100
    return y


def draw_axes(page):
    # we should not shadow the variables since there is no access modifiers in python
    page.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    # Print the local variables
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
canvas2.grid(row=0, column=1)

print(repr(canvas), repr(canvas2))
draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 100):
    y = parablola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()
