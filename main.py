from tkinter import *

from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    # print('Button clicked')  # test
    radius = user_input.get() # radius is string
    # print(radius)  # test
    if is_float(radius):
        user_input.delete(0, END)  # Clear input
        radius = float(radius)  # now is radius float
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # can change field
        txt_field.delete('1.0', END) # Delete alates esimesest reast kuni lõpuni
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Diameter: ' + str(circle.get_diameter()) + '\n')
        txt_field.insert(END, 'Perimeter: ' + str(circle.get_perimeter()) + '\n')
        txt_field.insert(END, 'Area: ' + str(circle.get_area()) + '\n')
        txt_field['state'] = 'disabled'  # User can't change field
        # print('Number')  # Test
    # else:
        # print('Error')  # Test

window = Tk()  # loob graafilise akna
window.title('Geometry - Circle')  #Title text
#window.geometry('400x500')  # põhiakna suurus w=400 h=500
window.resizable(False, False)  # True - saab muuta, False - muuta ei saa


# Frames
frame_top = Frame(window, bg='#89CFF0', height=50) #bg-background color
frame_top.pack(fill='both') # täita nii horisontaalis ja vertikaalis; x - horisontaalis, y - vertikaalis

frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)  # pack paneb frame peale loodud objektid

# First line in frame top
lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')
lbl.pack(side='left')

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus()  # tekitab akna aktiivseks, et pea hiirega aktriveerima

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))
btn_calc.pack(side=LEFT, padx=2, pady=2)  #pad muudab frame nupust kaugemale

# Second line, one big textfield
txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side='left', padx=2, pady=2)


# Bind Entry key tuvasta Enter vajutamist
window.bind('<Return>', lambda event: calculate(event))  # enteri vajutamisega kutsub calculate funktsiooni

# No MVC last line
window.mainloop()
