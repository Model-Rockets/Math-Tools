# Author: Navid Ali Ahmadi
# Year 9 Algorithm Development
# January 2021

# Importing all the modules that are used.
from tkinter import *
from tkinter import ttk
from tkmacosx import *
from PIL import ImageTk, Image
from math import *
import webbrowser
from tkinter.messagebox import showinfo

# Setting up the GUI window with tkinter.
root = Tk()
root.title("Math Tools")
root.minsize(517, 378)
root.maxsize(517, 378)
root.geometry("517x378")

# Setting up the notebook style from ttk.
style = ttk.Style()
style.configure('TNotebook', tabposition='n')  # 'n' as in compass direction

# Setting up all the images that are used.
img = Image.open("triangle_image.jpg")
img = img.resize((400, 159), Image.ANTIALIAS)
triangle_image = ImageTk.PhotoImage(img)

img1 = Image.open("desmos.png")
img1 = img1.resize((400, 159), Image.ANTIALIAS)
desmos = ImageTk.PhotoImage(img1)

img2 = Image.open("Symbolab.png")
img2 = img2.resize((400, 159), Image.ANTIALIAS)
symbolab = ImageTk.PhotoImage(img2)

img3 = Image.open("google.png")
img3 = img3.resize((400, 159), Image.ANTIALIAS)
google = ImageTk.PhotoImage(img3)

img4 = Image.open("square.png")
img4 = img4.resize((300, 159), Image.ANTIALIAS)
squareImage = ImageTk.PhotoImage(img4)

img5 = Image.open("rectangle.png")
img5 = img5.resize((400, 159), Image.ANTIALIAS)
rectangleImage = ImageTk.PhotoImage(img5)

img6 = Image.open("circle.png")
img6 = img6.resize((350, 159), Image.ANTIALIAS)
circleImage = ImageTk.PhotoImage(img6)

img7 = Image.open("pentagon.png")
img7 = img7.resize((400, 159), Image.ANTIALIAS)
pentagonImage = ImageTk.PhotoImage(img7)

img8 = Image.open("hexagon.png")
img8 = img8.resize((375, 180), Image.ANTIALIAS)
hexagonImage = ImageTk.PhotoImage(img8)

# Degree variable for radians to degree conversion.
degree = pi / 180

# Entry box text variables for collecting the inputs
inputSideA = StringVar()
inputSideB = StringVar()
inputSideC = StringVar()
inputAngleA = StringVar()
inputAngleB = StringVar()
inputAngleC = StringVar()
inputSideSquare = StringVar()
inputPerimeterSquare = StringVar()
inputAreaSquare = StringVar()
inputLength = StringVar()
inputWidth = StringVar()
inputAreaRectangle = StringVar()
inputPerimeterRectangle = StringVar()
inputRadiusCircle = StringVar()
inputDiameterCircle = StringVar()
inputCircumference = StringVar()
inputAreaCircle = StringVar()
inputSidePentagon = StringVar()
inputAreaPentagon = StringVar()
inputPerimeterPentagon = StringVar()
inputSideHexagon = StringVar()
inputAreaHexagon = StringVar()
inputPerimeterHexagon = StringVar()

# Shows the popup in the beginning for the user.
showinfo("Introduction", "Welcome to the Math Tools Application. We hope that it will help you on your mathematics "
                         "journey. Good Luck!")

# Function definitons start here for the application.

# Opens the browser with the link to the websites for the graphing, CAS and 3D Shapes tool.
def Desmos():
    webbrowser.open('https://www.desmos.com/calculator', new=2, autoraise=True)


def Symbolab():
    webbrowser.open('https://www.symbolab.com/solver/step-by-step/', new=2, autoraise=True)


def cube():
    webbrowser.open('https://www.google.com/search?rlz=1C5GCEM_enCA935CA935&ei=g94EYP7bE8G7ggfrw7OQBQ&q=cube+surface+'
                    'area+and+volume&oq=cube+&gs_lcp=CgZwc3ktYWIQARgAMgcIABDJAxBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIAB'
                    'BDMgQIABBDMgQIABBDMgcIABCxAxBDMgIIADoECAAQR1CbJVibJWDbe2gBcAJ4AIABYYgBYZIBATGYAQCgAQGqAQdnd3Mtd2l6'
                    'yAEIwAEB&sclient=psy-ab', new=2, autoraise=True)


def cuboid():
    webbrowser.open('https://www.google.com/search?rlz=1C5GCEM_enCA935CA935&ei=4N4EYIP9BM25ggf3g5zwBw&q=rectangular+pri'
                    'sm&oq=rectangular+prism&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAA'
                    'QRzIECAAQR1AAWABgs6ECaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwiD7b'
                    'qOpaTuAhXNnOAKHfcBB34Q4dUDCA0&uact=5', new=2, autoraise=True)


def sphere():
    webbrowser.open('https://www.google.com/search?rlz=1C5GCEM_enCA935CA935&ei=4N4EYIP9BM25ggf3g5zwBw&q=sphere&oq=spher'
                    'e&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQyQMQQzIHCAAQsQMQQzIHCAAQsQMQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQ'
                    'zIECAAQQzIECAAQQzIECAAQQzoICAAQ6gIQjwFQmPgBWNSEAmCDhgJoAXABeACAAdIBiAG_BZIBBTQuMS4xmAEAoAEBqgEHZ3d'
                    'zLXdperABCsABAQ&sclient=psy-ab&ved=0ahUKEwiD7bqOpaTuAhXNnOAKHfcBB34Q4dUDCA0&uact=5'
                    , new=2, autoraise=True)


def cylinder():
    webbrowser.open('https://www.google.com/search?rlz=1C5GCEM_enCA935CA935&ei=Kd8EYJ7EBuSGggf20bXIDw&q=cylinder&oq=cyl'
                    'ine&gs_lcp=CgZwc3ktYWIQAxgAMgoIABCxAxDJAxBDMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMg'
                    'QIABBDMgQIABBDMgQIABBDOggIABDqAhCPAToECC4QQzoLCC4QsQMQxwEQowI6CAgAELEDEIMBOgcIABDJAxBDUMD9BljXi'
                    'AdgyJcHaAFwAXgAgAGWAYgB4wSSAQM0LjKYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab',
                    new=2, autoraise=True)


def pyramid():
    webbrowser.open('https://www.google.com/search?rlz=1C5GCEM_enCA935CA935&ei=8t8EYJLLLqO1ggeC35GAAw&q=pyramid+surfac'
                    'e+area&oq=pyramid+su&gs_lcp=CgZwc3ktYWIQAxgAMggIABDJAxCRAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyC'
                    'AguEMcBEK8BMgIIADoECAAQRzoKCAAQsQMQyQMQQzoECAAQQzoFCAAQsQM6CAgAELEDEIMBOgcIABCxAxBDOgUIABCRAjoFCA'
                    'AQiwM6DQguEMcBEK8BEAoQiwNQgyhY30NgoUtoAnAEeACAAXmIAaIDkgEDMi4ymAEAoAEBqgEHZ3dzLXdpesgBCLgBAsABAQ&'
                    'sclient=psy-ab', new=2, autoraise=True)


# Functions to simplify the main triangle solver function.
def aaas(D, E, F, f):
    # Solves the triangle when three angles and one side is known and returns the completed tuple.
    d = f * sin(D) / sin(F)
    e = f * sin(E) / sin(F)
    return d, e, f, D, E, F


def sss(d, e, f):
    # Solves the triangle when three sides are known and returns the completed tuple.
    if (d + e > f) and (e + f > d) and (f + d > e):
        F = acos((d ** 2 + e ** 2 - f ** 2) / (2 * d * e))
        E = acos((d ** 2 + f ** 2 - e ** 2) / (2 * d * f))
        D = pi - F - E
        return d, e, f, D, E, F
    else:
        # print("reassigning D, E, F to something other than None as this causes errors")
        F = -1
        E = -1
        D = -1
        return d, e, f, D, E, F


def sas(d, e, F):
    # Solves for the third side if two sides and an angle is known.
    # To simplify the code, we send the process over to the sss function to find angles.
    f = sqrt(d ** 2 + e ** 2 - 2 * d * e * cos(F))
    return sss(d, e, f)


def ssa(d, e, D):
    # print("examining SSA inputs")
    h = e * sin(D)

    '''print("d:" + str(d))
    print("e:" + str(e))
    print("D:" + str(D))
    print("h:" + str(h))'''

    # There are six cases to consider
    # The height, h of the triangle is given by h = e*Sin(D)

    # Case 0 if the triangle is a pythagorean pair.
    if isclose(D, 0.6435011087926651) and (d < e):
        # print("one solution")
        F = pi/2
        E = pi - D - F
        f = sqrt(d ** 2 + e ** 2)
        # This tests that the triangle is actually possible.
        # This is as we don't check if the entry is a pythagorean pair.
        test_triangle(d, e, f, D, E, F)
        return d, e, f, D, E, F

    # Case 1: If D is acute and d = h, then ONE RIGHT triangle exists
    elif D < 1.5708 and d == h:
        # print("one solution")
        F = pi / 2  # This is the right angle
        E = pi - F - D
        e, f, d, E, F, D = aaas(E, F, D, d)
        return d, e, f, D, E, F

    # Case 2: If D is acute and d > e, then ONE triangle exists
    elif D < 1.5708 and d > e:
        # print("one solution")
        sinE = sin(D) * e / d
        E = asin(sinE)
        F = pi - D - E
        e, f, d, E, F, D = aaas(E, F, D, d)
        return d, e, f, D, E, F

    # Case 3: If D is obtuse and d > e, then ONE triangle exists
    elif D > 1.5708 and (d > e):
        # print("one solution")
        sinE = sin(D) * e / d
        E = asin(sinE)
        F = pi - D - E
        e, f, d, E, F, D = aaas(E, F, D, d)
        return d, e, f, D, E, F

    # Case $: If D is acute and d < e, then ONE triangle exists
    elif D < 1.5708 and (d < e):
        sinE = (sin(D) * e) / d
        E = asin(sinE)
        F = pi - D - E
        e, f, d, E, F, D = aaas(E, F, D, d)
        return d, e, f, D, E, F

    # Case 4: If D is obtuse and d < e or d = e, then NO triangles exist
    elif D > 1.5708 and (d > e or d == e):
        # print("no solution")
        F = -1
        E = -1
        D = -1
        f = -1
        e = -1
        d = -1
        return d, e, f, D, E, F

    # Case 6: If D is acute and h < d < e, then TWO triangles exist
    elif D > 1.5708 and (h < d < e):
        # print("two solutions exist, no unique solution")
        F = -1
        E = -1
        D = -1
        f = -1
        e = -1
        d = -1
        return d, e, f, D, E, F

        # Case 1: If D is acute and d < h, then NO triangle exists
    elif D < 1.5708 and d < h:
        # print("no solution")
        F = -1
        E = -1
        D = -1
        f = -1
        e = -1
        d = -1
        return d, e, f, D, E, F

    else:
        # print("No solution found")
        F = -1
        E = -1
        D = -1
        f = -1
        e = -1
        d = -1
        return d, e, f, D, E, F


# The main function that uses the helper functions to solve for the triangle.

def solve(a=None, b=None, c=None, A=None, B=None, C=None):
    if sum(x is not None for x in (a, b, c, A, B, C)) != 3:
        labelTitle.configure(text="Enter exactly 3 inputs", font='Helvetica 16', fg='red')
        return

    if sum(x is None for x in (a, b, c)) == 3:
        labelTitle.configure(text="Enter at least 1 side length", font='Helvetica 16', fg='red')
        return
    try:
        assert all(x > 0 for x in (a, b, c, A, B, C) if x is not None)
    except AssertionError:
        labelTitle.configure(text="No value should be zero", font='Helvetica 16', fg='red')
        return
    try:
        assert all(x < pi for x in (A, B, C) if x is not None)
    except AssertionError:
        labelTitle.configure(text="No angle larger than 180", font='Helvetica 16', fg='red')
        return

    # Solving when three sides are known.
    if sum(x is not None for x in (a, b, c)) == 3:

        a, b, c, A, B, C = sss(a, b, c)

        '''print("examining output")
        print("a:" + str(a))
        print("b:" + str(b))
        print("c:" + str(c))
        print("A:" + str(A))
        print("B:" + str(B))
        print("C:" + str(C))
        '''

        if A < 0 or B < 0 or C < 0:
            labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
            entryAngleA.delete(0, END)
            entryAngleA.update()
            entryAngleB.delete(0, END)
            entryAngleB.update()
            entryAngleC.delete(0, END)
            entryAngleC.update()
        else:
            labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
            entrySideA.delete(0, END)
            entrySideA.insert(0, str(round(a, 10)))
            entrySideA.update()
            entrySideB.delete(0, END)
            entrySideB.insert(0, str(round(b, 10)))
            entrySideB.update()
            entrySideC.delete(0, END)
            entrySideC.insert(0, str(round(c, 10)))
            entrySideC.update()
            entryAngleA.delete(0, END)
            entryAngleA.insert(0, str(round(A / degree, 10)))
            entryAngleA.update()
            entryAngleB.delete(0, END)
            entryAngleB.insert(0, str(round(B / degree, 10)))
            entryAngleB.update()
            entryAngleC.delete(0, END)
            entryAngleC.insert(0, str(round(C / degree, 10)))
            entryAngleC.update()

    # Solving when two sides and an angle are known
    if sum(x is not None for x in (a, b, c)) == 2:
        # Solving with two sides and an angle that is not in between.
        if all(x is not None for x in (a, A, b)):

            a, b, c, A, B, C = ssa(a, b, A)

            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        elif all(x is not None for x in (a, A, c)):
            a, c, b, A, C, B = ssa(a, c, A)

            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        elif all(x is not None for x in (b, B, a)):
            b, a, c, B, A, C = ssa(b, a, B)

            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        elif all(x is not None for x in (b, B, c)):
            b, c, a, B, C, A = ssa(b, c, B)
            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        elif all(x is not None for x in (c, C, a)):
            c, a, b, C, A, B = ssa(c, a, C)
            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        elif all(x is not None for x in (c, C, b)):
            c, b, a, C, B, A = ssa(c, b, C)

            if A < 0 or B < 0 or C < 0 or a < 0 or b < 0 or c < 0:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return
            elif A > 0 and B > 0 and C > 0 and a > 0 and b > 0 and c > 0:
                labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')
                entrySideA.delete(0, END)
                entrySideA.insert(0, str(round(a, 10)))
                entrySideA.update()
                entrySideB.delete(0, END)
                entrySideB.insert(0, str(round(b, 10)))
                entrySideB.update()
                entrySideC.delete(0, END)
                entrySideC.insert(0, str(round(c, 10)))
                entrySideC.update()
                entryAngleA.delete(0, END)
                entryAngleA.insert(0, str(round(A / degree, 10)))
                entryAngleA.update()
                entryAngleB.delete(0, END)
                entryAngleB.insert(0, str(round(B / degree, 10)))
                entryAngleB.update()
                entryAngleC.delete(0, END)
                entryAngleC.insert(0, str(round(C / degree, 10)))
                entryAngleC.update()
                return
            else:
                labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
                return

        # Solving with two sides with an angle in between.
        elif all(x is not None for x in (a, b, C)):
            a, b, c, A, B, C = sas(a, b, C)

        elif all(x is not None for x in (b, c, A)):
            b, c, a, B, C, A = sas(b, c, A)

        elif all(x is not None for x in (c, a, B)):
            c, a, b, C, A, B = sas(c, a, B)

        else:
            return a, b, c, A, B, C

        # This is where we have the answers for "SAS" calculations
        # Now we update each of the Entry boxes as we have the data in hand!

        entrySideA.delete(0, END)
        entrySideA.insert(0, str(round(a, 10)))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(round(b, 10)))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(round(c, 10)))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(round(A / degree, 10)))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(round(B / degree, 10)))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(round(C / degree, 10)))
        entryAngleC.update()
        labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')

    # Solving with one side and two angles are known by first calculating the last angle.
    if sum(x is not None for x in (a, b, c)) == 1:
        # Solving for the remaining angle.
        if A is None:
            A = pi - B - C
        elif B is None:
            B = pi - A - C
        else:
            C = pi - A - B
        try:
            assert A > 0 and B > 0 and C > 0
        except AssertionError:
            labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
            return
        # Solving for the two remaining sides using functions.
        if c is not None:
            a, b, c, A, B, C = aaas(A, B, C, c)
        elif a is not None:
            b, c, a, B, C, A = aaas(B, C, A, a)
        else:
            c, a, b, C, A, B = aaas(C, A, B, b)

        '''print("a:" + str(a))
        print("b:" + str(b))
        print("c:" + str(c))
        print("A:" + str(A))
        print("B:" + str(B))
        print("C:" + str(C))'''

        entrySideA.delete(0, END)
        entrySideA.insert(0, str(round(a, 10)))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(round(b, 10)))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(round(c, 10)))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(round(A / degree, 10)))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(round(B / degree, 10)))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(round(C / degree, 10)))
        entryAngleC.update()
        labelTitle.configure(text="Solution found", font='Helvetica 16 bold', fg='green')

def test_triangle(a,b,c,A,B,C):
    # Checks that the triangle satisfies the law of cosines and law of sines
    try:
        assert isclose(a/sin(A), b/sin(B))
    except AssertionError:
        labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
        entrySideA.delete(0, END)
        entrySideA.insert(0, str(sidea))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(sideb))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(sidec))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(anglea))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(angleb))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(anglec))
        entryAngleC.update()
        return
    try:
        assert isclose(a/sin(A), c/sin(C))
    except AssertionError:
        labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
        entrySideA.delete(0, END)
        entrySideA.insert(0, str(sidea))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(sideb))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(sidec))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(anglea))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(angleb))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(anglec))
        entryAngleC.update()
        return
    try:
        assert isclose(c**2, a**2 + b**2 - 2 * a * b * cos(C))
    except AssertionError:
        labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
        entrySideA.delete(0, END)
        entrySideA.insert(0, str(sidea))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(sideb))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(sidec))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(anglea))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(angleb))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(anglec))
        entryAngleC.update()
        return
    try:
        assert isclose(a**2, b**2 + c**2 - 2 * b * c * cos(A))
    except AssertionError:
        labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
        entrySideA.delete(0, END)
        entrySideA.insert(0, str(sidea))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(sideb))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(sidec))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(anglea))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(angleb))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(anglec))
        entryAngleC.update()
        return
    try:
        assert isclose(b**2, c**2 + a**2 - 2 * c * a * cos(B))
    except AssertionError:
        labelTitle.configure(text="No solution with given data", font='Helvetica 16', fg='red')
        entrySideA.delete(0, END)
        entrySideA.insert(0, str(sidea))
        entrySideA.update()
        entrySideB.delete(0, END)
        entrySideB.insert(0, str(sideb))
        entrySideB.update()
        entrySideC.delete(0, END)
        entrySideC.insert(0, str(sidec))
        entrySideC.update()
        entryAngleA.delete(0, END)
        entryAngleA.insert(0, str(anglea))
        entryAngleA.update()
        entryAngleB.delete(0, END)
        entryAngleB.insert(0, str(angleb))
        entryAngleB.update()
        entryAngleC.delete(0, END)
        entryAngleC.insert(0, str(anglec))
        entryAngleC.update()
        return


# Helper functions to support button action and implementation.
# This clear the entry boxes for the user to input new values.
def clear_triangle_inputs():
    labelTitle.configure(text="Enter 3 out of 6 values", font='Helvetica 16 bold', fg='black')
    labelTitle.update()
    entrySideA.delete(0, END)
    entrySideA.update()
    entrySideB.delete(0, END)
    entrySideB.update()
    entrySideC.delete(0, END)
    entrySideC.update()
    entryAngleA.delete(0, END)
    entryAngleA.update()
    entryAngleB.delete(0, END)
    entryAngleB.update()
    entryAngleC.delete(0, END)
    entryAngleC.update()


# Helper functions for checking the user inputs
def check_triangle_inputs():
    sidea = None
    sideb = None
    sidec = None
    anglea = None
    angleb = None
    anglec = None

    if len(entrySideA.get()) == 0:
        # First part of the function checks for empty entry boxes.
        sidea = None  ###
    if len(entrySideA.get()) != 0:
        # The second part of the function checks for string values.
        try:
            float(entrySideA.get())
            inta = float(inputSideA.get())
            sidea = inta
            # print("sidea: " + str(sidea))
        except ValueError:
            labelTitle.configure(text="Side A should be a number", font='Helvetica 16', fg='red')
            entrySideA.delete(0, END)
            entrySideA.update()
            return
    if len(entrySideB.get()) == 0:
        sideb = None  ###
    if len(entrySideB.get()) != 0:
        try:
            float(entrySideB.get())
            intb = float(inputSideB.get())
            sideb = intb
            # print("sideb: " + str(sideb))
        except ValueError:
            labelTitle.configure(text="Side B should be a number", font='Helvetica 16', fg='red')
            entrySideB.delete(0, END)
            entrySideB.update()
            return
    if len(entrySideC.get()) == 0:
        sidec = None  ###
    if len(entrySideC.get()) != 0:
        try:
            float(entrySideC.get())
            intc = float(inputSideC.get())
            sidec = intc
            # print("sidec: " + str(sidec))
        except ValueError:
            labelTitle.configure(text="Side C should be a number", font='Helvetica 16', fg='red')
            entrySideC.delete(0, END)
            entrySideC.update()
            return
    if len(entryAngleA.get()) == 0:
        anglea = None  ###
    if len(entryAngleA.get()) != 0:
        try:
            float(entryAngleA.get())
            intA = float(inputAngleA.get())
            anglea = intA * degree
            # print("anglea: " + str(anglea))
        except ValueError:
            labelTitle.configure(text="Angle A should be a number", font='Helvetica 16', fg='red')
            entryAngleA.delete(0, END)
            entryAngleA.update()
            return
    if len(entryAngleB.get()) == 0:
        angleb = None  ###
    if len(entryAngleB.get()) != 0:
        try:
            float(entryAngleB.get())
            intB = float(inputAngleB.get())
            angleb = intB * degree
            # print("angleb: " + str(angleb))
        except ValueError:
            labelTitle.configure(text="Angle B should be a number", font='Helvetica 16', fg='red')
            entryAngleB.delete(0, END)
            entryAngleB.update()
            return
    if len(entryAngleC.get()) == 0:
        anglec = None  ###
    if len(entryAngleC.get()) != 0:
        try:
            float(entryAngleC.get())
            intC = float(inputAngleC.get())
            anglec = intC * degree
            # print("anglec: " + str(anglec) + " radians")
        except ValueError:
            labelTitle.configure(text="Angle C should be a number", font='Helvetica 16', fg='red')
            entryAngleC.delete(0, END)
            entryAngleC.update()
            return

    '''print("Now we will call the solver function")
    print("a:" + str(sidea))
    print("b:" + str(sideb))
    print("c:" + str(sidec))
    print("A:" + str(anglea))
    print("B:" + str(angleb))
    print("C:" + str(anglec))'''
    # If the inputs are correct the solver function is called.
    solve(a=sidea, b=sideb, c=sidec, A=anglea, B=angleb, C=anglec)

# Functions for the 2D Shape solver.
# The first functions just set up the user interface for the selected shape.
# This is done by using the widget.place_forget() function as we use the place method.
# Once the place of a function is forgotten it must be restated again.
# If there was a widget.place_remove() like the function for grid that would be better
# as the program would remember the location.

# Square widget locations.
def square():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.place(x=293, y=55)
    labelInstruct.update()
    buttonRectangleSolve.place_forget()
    buttonRectangleClear.place_forget()
    entryLength.place_forget()
    entryWidth.place_forget()
    entryAreaRectangle.place_forget()
    entryPerimeterRectangle.place_forget()
    buttonCircleSolve.place_forget()
    buttonCircleClear.place_forget()
    entryRadiusCircle.place_forget()
    entryDiameterCircle.place_forget()
    entryAreaCircle.place_forget()
    entryCircumference.place_forget()
    buttonPentagonSolve.place_forget()
    buttonPentagonClear.place_forget()
    entrySidePentagon.place_forget()
    entryAreaPentagon.place_forget()
    entryPerimeterPentagon.place_forget()
    buttonHexagonSolve.place_forget()
    buttonHexagonClear.place_forget()
    entrySideHexagon.place_forget()
    entryAreaHexagon.place_forget()
    entryPerimeterHexagon.place_forget()
    rectangleCanvas.place_forget()
    circleCanvas.place_forget()
    pentagonCanvas.place_forget()
    hexagonCanvas.place_forget()
    buttonSquareSolve.place(x=282, y=100)
    buttonSquareClear.place(x=372, y=100)
    entrySideSquare.place(x=85, y=30)
    entryAreaSquare.place(x=85, y=60)
    entryPerimeterSquare.place(x=85, y=90)
    squareCanvas.place(x=145, y=145)
    label1.configure(text="Side:")
    label2.configure(text="Area:")
    label3.configure(text="Perimeter:")
    label4.configure(text="")
    label1.place(x=40, y=32)
    label2.place(x=40, y=62)
    label3.place(x=5, y=92)
    label4.place(x=0, y=122)

# Rectangle widget locations.
def rectangle():
    labelInstruct.configure(text="Enter 2 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.place(x=293, y=55)
    labelInstruct.update()
    buttonSquareSolve.place_forget()
    buttonSquareClear.place_forget()
    entrySideSquare.place_forget()
    entryAreaSquare.place_forget()
    entryPerimeterSquare.place_forget()
    buttonCircleSolve.place_forget()
    buttonCircleClear.place_forget()
    entryRadiusCircle.place_forget()
    entryDiameterCircle.place_forget()
    entryAreaCircle.place_forget()
    entryCircumference.place_forget()
    buttonPentagonSolve.place_forget()
    buttonPentagonClear.place_forget()
    entrySidePentagon.place_forget()
    entryAreaPentagon.place_forget()
    entryPerimeterPentagon.place_forget()
    buttonHexagonSolve.place_forget()
    buttonHexagonClear.place_forget()
    entrySideHexagon.place_forget()
    entryAreaHexagon.place_forget()
    entryPerimeterHexagon.place_forget()
    squareCanvas.place_forget()
    circleCanvas.place_forget()
    pentagonCanvas.place_forget()
    hexagonCanvas.place_forget()
    buttonRectangleSolve.place(x=282, y=100)
    buttonRectangleClear.place(x=372, y=100)
    entryLength.place(x=85, y=30)
    entryWidth.place(x=85, y=60)
    entryAreaRectangle.place(x=85, y=90)
    entryPerimeterRectangle.place(x=85, y=120)
    rectangleCanvas.place(x=62, y=155)
    label1.configure(text="Length:")
    label2.configure(text="Width:")
    label3.configure(text="Area:")
    label4.configure(text="Perimeter:")
    label1.place(x=24, y=32)
    label2.place(x=30, y=62)
    label3.place(x=39, y=92)
    label4.place(x=5, y=122)

# Circle widget locations.
def circle():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.place(x=293, y=55)
    labelInstruct.update()
    buttonSquareSolve.place_forget()
    buttonSquareClear.place_forget()
    entrySideSquare.place_forget()
    entryAreaSquare.place_forget()
    entryPerimeterSquare.place_forget()
    buttonRectangleSolve.place_forget()
    buttonRectangleClear.place_forget()
    entryLength.place_forget()
    entryWidth.place_forget()
    entryAreaRectangle.place_forget()
    entryPerimeterRectangle.place_forget()
    buttonPentagonSolve.place_forget()
    buttonPentagonClear.place_forget()
    entrySidePentagon.place_forget()
    entryAreaPentagon.place_forget()
    entryPerimeterPentagon.place_forget()
    buttonHexagonSolve.place_forget()
    buttonHexagonClear.place_forget()
    entrySideHexagon.place_forget()
    entryAreaHexagon.place_forget()
    entryPerimeterHexagon.place_forget()
    squareCanvas.place_forget()
    rectangleCanvas.place_forget()
    pentagonCanvas.place_forget()
    hexagonCanvas.place_forget()
    buttonCircleSolve.place(x=282, y=100)
    buttonCircleClear.place(x=372, y=100)
    entryRadiusCircle.place(x=85, y=30)
    entryDiameterCircle.place(x=85, y=60)
    entryAreaCircle.place(x=85, y=90)
    entryCircumference.place(x=85, y=120)
    circleCanvas.place(x=130, y=155)
    label1.configure(text="Radius:")
    label2.configure(text="Diameter:")
    label3.configure(text="Area:")
    label4.configure(text="Perimeter:")
    label1.place(x=25, y=32)
    label2.place(x=13, y=62)
    label3.place(x=40, y=92)
    label4.place(x=5, y=122)

# Pentagon widget locations.
def pentagon():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.place(x=293, y=55)
    labelInstruct.update()
    buttonSquareSolve.place_forget()
    buttonSquareClear.place_forget()
    entrySideSquare.place_forget()
    entryAreaSquare.place_forget()
    entryPerimeterSquare.place_forget()
    buttonRectangleSolve.place_forget()
    buttonRectangleClear.place_forget()
    entryLength.place_forget()
    entryWidth.place_forget()
    entryAreaRectangle.place_forget()
    entryPerimeterRectangle.place_forget()
    buttonCircleSolve.place_forget()
    buttonCircleClear.place_forget()
    entryRadiusCircle.place_forget()
    entryDiameterCircle.place_forget()
    entryAreaCircle.place_forget()
    entryCircumference.place_forget()
    buttonHexagonSolve.place_forget()
    buttonHexagonClear.place_forget()
    entrySideHexagon.place_forget()
    entryAreaHexagon.place_forget()
    entryPerimeterHexagon.place_forget()
    squareCanvas.place_forget()
    rectangleCanvas.place_forget()
    circleCanvas.place_forget()
    hexagonCanvas.place_forget()
    buttonPentagonSolve.place(x=282, y=100)
    buttonPentagonClear.place(x=372, y=100)
    entrySidePentagon.place(x=85, y=30)
    entryAreaPentagon.place(x=85, y=60)
    entryPerimeterPentagon.place(x=85, y=90)
    pentagonCanvas.place(x=120, y=140)
    label1.configure(text="Side:")
    label2.configure(text="Area:")
    label3.configure(text="Perimeter:")
    label4.configure(text="")
    label1.place(x=40, y=32)
    label2.place(x=40, y=62)
    label3.place(x=5, y=92)
    label4.place(x=0, y=122)

# Hexagon widget locations.
def hexagon():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.place(x=293, y=55)
    labelInstruct.update()
    buttonSquareSolve.place_forget()
    buttonSquareClear.place_forget()
    entrySideSquare.place_forget()
    entryAreaSquare.place_forget()
    entryPerimeterSquare.place_forget()
    buttonRectangleSolve.place_forget()
    buttonRectangleClear.place_forget()
    entryLength.place_forget()
    entryWidth.place_forget()
    entryAreaRectangle.place_forget()
    entryPerimeterRectangle.place_forget()
    buttonCircleSolve.place_forget()
    buttonCircleClear.place_forget()
    entryRadiusCircle.place_forget()
    entryDiameterCircle.place_forget()
    entryAreaCircle.place_forget()
    entryCircumference.place_forget()
    buttonPentagonSolve.place_forget()
    buttonPentagonClear.place_forget()
    entrySidePentagon.place_forget()
    entryAreaPentagon.place_forget()
    entryPerimeterPentagon.place_forget()
    squareCanvas.place_forget()
    rectangleCanvas.place_forget()
    circleCanvas.place_forget()
    pentagonCanvas.place_forget()
    entrySideHexagon.place(x=85, y=30)
    entryAreaHexagon.place(x=85, y=60)
    entryPerimeterHexagon.place(x=85, y=90)
    buttonHexagonClear.place(x=372, y=100)
    buttonHexagonSolve.place(x=282, y=100)
    hexagonCanvas.place(x=120, y=140)
    label1.configure(text="Side:")
    label2.configure(text="Area:")
    label3.configure(text="Perimeter:")
    label4.configure(text="")
    label1.place(x=40, y=32)
    label2.place(x=40, y=62)
    label3.place(x=5, y=92)
    label4.place(x=0, y=122)

# These are the clear functions that clear the entry boxes so it can be used again quickly.
def clear_square():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.update()
    entrySideSquare.delete(0, END)
    entrySideSquare.update()
    entryAreaSquare.delete(0, END)
    entryAreaSquare.update()
    entryPerimeterSquare.delete(0, END)
    entryPerimeterSquare.update()


def clear_rectangle():
    labelInstruct.configure(text="Enter 2 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.update()
    entryLength.delete(0, END)
    entryLength.update()
    entryWidth.delete(0, END)
    entryWidth.update()
    entryAreaRectangle.delete(0, END)
    entryAreaRectangle.update()
    entryPerimeterRectangle.delete(0, END)
    entryPerimeterRectangle.update()


def clear_circle():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.update()
    entryRadiusCircle.delete(0, END)
    entryRadiusCircle.update()
    entryDiameterCircle.delete(0, END)
    entryDiameterCircle.update()
    entryAreaCircle.delete(0, END)
    entryAreaCircle.update()
    entryCircumference.delete(0, END)
    entryCircumference.update()


def clear_pentagon():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.update()
    entrySidePentagon.delete(0, END)
    entrySidePentagon.update()
    entryAreaPentagon.delete(0, END)
    entryAreaPentagon.update()
    entryPerimeterPentagon.delete(0, END)
    entryPerimeterPentagon.update()


def clear_hexagon():
    labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='black')
    labelInstruct.update()
    entrySideHexagon.delete(0, END)
    entrySideHexagon.update()
    entryPerimeterHexagon.delete(0, END)
    entryPerimeterHexagon.update()
    entryAreaHexagon.delete(0, END)
    entryAreaHexagon.update()

# These are the solve functions that solve fore the remaining variables.
def solve_square():
    if len(entrySideSquare.get()) != 0:
        try:
            float(entrySideSquare.get())
            varSideSquare = float(inputSideSquare.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entrySideSquare.delete(0, END)
            entrySideSquare.update()
            return
    if len(entryAreaSquare.get()) != 0:
        try:
            float(entryAreaSquare.get())
            varAreaSquare = float(inputAreaSquare.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryAreaSquare.delete(0, END)
            entryAreaSquare.update()
            return
    if len(entryPerimeterSquare.get()) != 0:
        try:
            float(entryPerimeterSquare.get())
            varPerimeterSquare = float(inputPerimeterSquare.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryPerimeterSquare.delete(0, END)
            entryPerimeterSquare.update()
            return
    if len(entryPerimeterSquare.get()) != 0 and len(entrySideSquare.get()) == 0 and len(entryAreaSquare.get()) == 0:
        sideSquare = varPerimeterSquare / 4
        areaSquare = sideSquare ** 2
        perimeterSquare = varPerimeterSquare
        if sideSquare > 0 and areaSquare > 0 and perimeterSquare > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideSquare.delete(0, END)
            entrySideSquare.insert(0, str(sideSquare))
            entrySideSquare.update()
            entryAreaSquare.delete(0, END)
            entryAreaSquare.insert(0, str(areaSquare))
            entryAreaSquare.update()
            entryPerimeterSquare.delete(0, END)
            entryPerimeterSquare.insert(0, str(perimeterSquare))
            entryPerimeterSquare.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterSquare.get()) == 0 and len(entrySideSquare.get()) != 0 and len(entryAreaSquare.get()) == 0:
        sideSquare = varSideSquare
        areaSquare = sideSquare ** 2
        perimeterSquare = sideSquare * 4
        if sideSquare > 0 and areaSquare > 0 and perimeterSquare > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideSquare.delete(0, END)
            entrySideSquare.insert(0, str(sideSquare))
            entrySideSquare.update()
            entryAreaSquare.delete(0, END)
            entryAreaSquare.insert(0, str(areaSquare))
            entryAreaSquare.update()
            entryPerimeterSquare.delete(0, END)
            entryPerimeterSquare.insert(0, str(perimeterSquare))
            entryPerimeterSquare.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterSquare.get()) == 0 and len(entrySideSquare.get()) == 0 and len(entryAreaSquare.get()) != 0:
        sideSquare = sqrt(varAreaSquare)
        areaSquare = varAreaSquare
        perimeterSquare = sideSquare * 4
        if sideSquare > 0 and areaSquare > 0 and perimeterSquare > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideSquare.delete(0, END)
            entrySideSquare.insert(0, str(sideSquare))
            entrySideSquare.update()
            entryAreaSquare.delete(0, END)
            entryAreaSquare.insert(0, str(areaSquare))
            entryAreaSquare.update()
            entryPerimeterSquare.delete(0, END)
            entryPerimeterSquare.insert(0, str(perimeterSquare))
            entryPerimeterSquare.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterSquare.get()) == 0 and len(entrySideSquare.get()) == 0 and len(entryAreaSquare.get()) == 0:
        labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='red')
        return
    else:
        labelInstruct.configure(text="Enter exactly 1 value", font='Helvetica 16 bold', fg='red')
        return


def solve_rectangle():
    if len(entryLength.get()) != 0:
        try:
            float(entryLength.get())
            varLength = float(inputLength.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryLength.delete(0, END)
            entryLength.update()
            return
    if len(entryWidth.get()) != 0:
        try:
            float(entryWidth.get())
            varWidth = float(inputWidth.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryWidth.delete(0, END)
            entryWidth.update()
            return
    if len(entryAreaRectangle.get()) != 0:
        try:
            float(entryAreaRectangle.get())
            varAreaRectangle = float(inputAreaRectangle.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.update()
            return
    if len(entryPerimeterRectangle.get()) != 0:
        try:
            float(entryPerimeterRectangle.get())
            varPerimeterRectangle = float(inputPerimeterRectangle.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.update()
            return
    if len(entryLength.get()) != 0 and len(entryWidth.get()) != 0 and len(entryAreaRectangle.get()) == 0 and len(entryPerimeterRectangle.get()) == 0:
        length = varLength
        width = varWidth
        area = varLength * varWidth
        perimeter = (varWidth * 2) + (varLength * 2)
        if length > 0 and width > 0 and area > 0 and perimeter > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryLength.delete(0, END)
            entryLength.insert(0, str(length))
            entryLength.update()
            entryWidth.delete(0, END)
            entryWidth.insert(0, str(width))
            entryWidth.update()
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.insert(0, str(area))
            entryAreaRectangle.update()
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.insert(0, str(perimeter))
            entryPerimeterRectangle.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryLength.get()) != 0 and len(entryWidth.get()) == 0 and len(entryAreaRectangle.get()) != 0 and len(entryPerimeterRectangle.get()) == 0:
        length = varLength
        width = varAreaRectangle / varLength
        area = varAreaRectangle
        perimeter = (width * 2) + (varLength * 2)
        if length > 0 and width > 0 and area > 0 and perimeter > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryLength.delete(0, END)
            entryLength.insert(0, str(length))
            entryLength.update()
            entryWidth.delete(0, END)
            entryWidth.insert(0, str(width))
            entryWidth.update()
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.insert(0, str(area))
            entryAreaRectangle.update()
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.insert(0, str(perimeter))
            entryPerimeterRectangle.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryLength.get()) != 0 and len(entryWidth.get()) == 0 and len(entryAreaRectangle.get()) == 0 and len(entryPerimeterRectangle.get()) != 0:
        length = varLength
        width = (varPerimeterRectangle / 2) - varLength
        area = varLength * width
        perimeter = varPerimeterRectangle
        if length > 0 and width > 0 and area > 0 and perimeter > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryLength.delete(0, END)
            entryLength.insert(0, str(length))
            entryLength.update()
            entryWidth.delete(0, END)
            entryWidth.insert(0, str(width))
            entryWidth.update()
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.insert(0, str(area))
            entryAreaRectangle.update()
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.insert(0, str(perimeter))
            entryPerimeterRectangle.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryLength.get()) == 0 and len(entryWidth.get()) != 0 and len(entryAreaRectangle.get()) != 0 and len(entryPerimeterRectangle.get()) == 0:
        length = varAreaRectangle / varWidth
        width = varWidth
        area = length * varWidth
        perimeter = (varWidth * 2) + (length * 2)
        if length > 0 and width > 0 and area > 0 and perimeter > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryLength.delete(0, END)
            entryLength.insert(0, str(length))
            entryLength.update()
            entryWidth.delete(0, END)
            entryWidth.insert(0, str(width))
            entryWidth.update()
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.insert(0, str(area))
            entryAreaRectangle.update()
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.insert(0, str(perimeter))
            entryPerimeterRectangle.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryLength.get()) == 0 and len(entryWidth.get()) != 0 and len(entryAreaRectangle.get()) == 0 and len(entryPerimeterRectangle.get()) != 0:
        length = (varPerimeterRectangle / 2) - varWidth
        width = varWidth
        area = length * varWidth
        perimeter = varPerimeterRectangle
        if length > 0 and width > 0 and area > 0 and perimeter > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryLength.delete(0, END)
            entryLength.insert(0, str(length))
            entryLength.update()
            entryWidth.delete(0, END)
            entryWidth.insert(0, str(width))
            entryWidth.update()
            entryAreaRectangle.delete(0, END)
            entryAreaRectangle.insert(0, str(area))
            entryAreaRectangle.update()
            entryPerimeterRectangle.delete(0, END)
            entryPerimeterRectangle.insert(0, str(perimeter))
            entryPerimeterRectangle.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryLength.get()) == 0 and len(entryWidth.get()) == 0 and len(entryAreaRectangle.get()) != 0 and len(entryPerimeterRectangle.get()) != 0:
            labelInstruct.configure(text="One side is required", font='Helvetica 16 bold', fg='red')
            return            
    else:
        labelInstruct.configure(text="Enter exactly 2 values", font='Helvetica 16 bold', fg='red')
        return


def solve_circle():
    if len(entryRadiusCircle.get()) != 0:
        try:
            float(entryRadiusCircle.get())
            varRadius = float(inputRadiusCircle.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryRadiusCircle.delete(0, END)
            entryRadiusCircle.update()
            return
    if len(entryDiameterCircle.get()) != 0:
        try:
            float(entryDiameterCircle.get())
            varDiameter = float(inputDiameterCircle.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryDiameterCircle.delete(0, END)
            entryDiameterCircle.update()
            return
    if len(entryAreaCircle.get()) != 0:
        try:
            float(entryAreaCircle.get())
            varAreaCircle = float(inputAreaCircle.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryAreaCircle.delete(0, END)
            entryAreaCircle.update()
            return
    if len(entryCircumference.get()) != 0:
        try:
            float(entryCircumference.get())
            varCircumference = float(inputCircumference.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryCircumference.delete(0, END)
            entryCircumference.update()
            return
    if len(entryRadiusCircle.get()) != 0 and len(entryDiameterCircle.get()) == 0 and len(entryAreaCircle.get()) == 0 and len(entryCircumference.get()) == 0:
        radius = varRadius
        diameter = radius * 2
        areaCircle = radius * radius * pi
        circumference = radius * 2 * pi
        if radius > 0 and diameter > 0 and areaCircle > 0 and circumference > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryRadiusCircle.delete(0, END)
            entryRadiusCircle.insert(0, str(radius))
            entryRadiusCircle.update()
            entryDiameterCircle.delete(0, END)
            entryDiameterCircle.insert(0, str(diameter))
            entryDiameterCircle.update()
            entryAreaCircle.delete(0, END)
            entryAreaCircle.insert(0, str(areaCircle))
            entryAreaCircle.update()
            entryCircumference.delete(0, END)
            entryCircumference.insert(0, str(circumference))
            entryCircumference.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryRadiusCircle.get()) == 0 and len(entryDiameterCircle.get()) != 0 and len(entryAreaCircle.get()) == 0 and len(entryCircumference.get()) == 0:
        radius = varDiameter / 2
        diameter = varDiameter
        areaCircle = radius * radius * pi
        circumference = radius * 2 * pi
        if radius > 0 and diameter > 0 and areaCircle > 0 and circumference > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryRadiusCircle.delete(0, END)
            entryRadiusCircle.insert(0, str(radius))
            entryRadiusCircle.update()
            entryDiameterCircle.delete(0, END)
            entryDiameterCircle.insert(0, str(diameter))
            entryDiameterCircle.update()
            entryAreaCircle.delete(0, END)
            entryAreaCircle.insert(0, str(areaCircle))
            entryAreaCircle.update()
            entryCircumference.delete(0, END)
            entryCircumference.insert(0, str(circumference))
            entryCircumference.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryRadiusCircle.get()) == 0 and len(entryDiameterCircle.get()) == 0 and len(entryAreaCircle.get()) != 0 and len(entryCircumference.get()) == 0:
        radius = sqrt(varAreaCircle / pi)
        diameter = radius * 2
        areaCircle = varAreaCircle
        circumference = radius * 2 * pi
        if radius > 0 and diameter > 0 and areaCircle > 0 and circumference > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryRadiusCircle.delete(0, END)
            entryRadiusCircle.insert(0, str(radius))
            entryRadiusCircle.update()
            entryDiameterCircle.delete(0, END)
            entryDiameterCircle.insert(0, str(diameter))
            entryDiameterCircle.update()
            entryAreaCircle.delete(0, END)
            entryAreaCircle.insert(0, str(areaCircle))
            entryAreaCircle.update()
            entryCircumference.delete(0, END)
            entryCircumference.insert(0, str(circumference))
            entryCircumference.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryRadiusCircle.get()) == 0 and len(entryDiameterCircle.get()) == 0 and len(entryAreaCircle.get()) == 0 and len(entryCircumference.get()) != 0:
        radius = varCircumference / pi / 2
        diameter = radius * 2
        areaCircle = radius * radius * pi
        circumference = varCircumference
        if radius > 0 and diameter > 0 and areaCircle > 0 and circumference > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entryRadiusCircle.delete(0, END)
            entryRadiusCircle.insert(0, str(radius))
            entryRadiusCircle.update()
            entryDiameterCircle.delete(0, END)
            entryDiameterCircle.insert(0, str(diameter))
            entryDiameterCircle.update()
            entryAreaCircle.delete(0, END)
            entryAreaCircle.insert(0, str(areaCircle))
            entryAreaCircle.update()
            entryCircumference.delete(0, END)
            entryCircumference.insert(0, str(circumference))
            entryCircumference.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryRadiusCircle.get()) == 0 and len(entryDiameterCircle.get()) == 0 and len(entryAreaCircle.get()) == 0 and len(entryCircumference.get()) == 0:
        labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='red')
        return
    else:
        labelInstruct.configure(text="Enter exactly 1 value", font='Helvetica 16 bold', fg='red')
        return


def solve_pentagon():
    if len(entrySidePentagon.get()) != 0:
        try:
            float(entrySidePentagon.get())
            varSidePentagon = float(inputSidePentagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entrySidePentagon.delete(0, END)
            entrySidePentagon.update()
            return
    if len(entryAreaPentagon.get()) != 0:
        try:
            float(entryAreaPentagon.get())
            varAreaPentagon = float(inputAreaPentagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryAreaPentagon.delete(0, END)
            entryAreaPentagon.update()
            return
    if len(entryPerimeterPentagon.get()) != 0:
        try:
            float(entryPerimeterPentagon.get())
            varPerimeterPentagon = float(inputPerimeterPentagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryPerimeterPentagon.delete(0, END)
            entryPerimeterPentagon.update()
            return
    if len(entryPerimeterPentagon.get()) != 0 and len(entrySidePentagon.get()) == 0 and len(entryAreaPentagon.get()) == 0:
        sidePentagon = varPerimeterPentagon / 5
        areaPentagon = (5 * (sidePentagon ** 2)) / (4 * (sqrt(5-(2 * sqrt(5)))))
        perimeterPentagon = varPerimeterPentagon
        if sidePentagon > 0 and areaPentagon > 0 and perimeterPentagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySidePentagon.delete(0, END)
            entrySidePentagon.insert(0, str(sidePentagon))
            entrySidePentagon.update()
            entryAreaPentagon.delete(0, END)
            entryAreaPentagon.insert(0, str(areaPentagon))
            entryAreaPentagon.update()
            entryPerimeterPentagon.delete(0, END)
            entryPerimeterPentagon.insert(0, str(perimeterPentagon))
            entryPerimeterPentagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterPentagon.get()) == 0 and len(entrySidePentagon.get()) != 0 and len(entryAreaPentagon.get()) == 0:
        sidePentagon = varSidePentagon
        areaPentagon = (5 * (sidePentagon ** 2)) / (4 * (sqrt(5-(2 * sqrt(5)))))
        perimeterPentagon = sidePentagon * 5
        if sidePentagon > 0 and areaPentagon > 0 and perimeterPentagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySidePentagon.delete(0, END)
            entrySidePentagon.insert(0, str(sidePentagon))
            entrySidePentagon.update()
            entryAreaPentagon.delete(0, END)
            entryAreaPentagon.insert(0, str(areaPentagon))
            entryAreaPentagon.update()
            entryPerimeterPentagon.delete(0, END)
            entryPerimeterPentagon.insert(0, str(perimeterPentagon))
            entryPerimeterPentagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterPentagon.get()) == 0 and len(entrySidePentagon.get()) == 0 and len(entryAreaPentagon.get()) != 0:
        sidePentagon = (25 ** 0.75) * ((sqrt(varAreaPentagon)) / 8.77166)
        areaPentagon = varAreaPentagon
        perimeterPentagon = sidePentagon * 5
        if sidePentagon > 0 and areaPentagon > 0 and perimeterPentagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySidePentagon.delete(0, END)
            entrySidePentagon.insert(0, str(sidePentagon))
            entrySidePentagon.update()
            entryAreaPentagon.delete(0, END)
            entryAreaPentagon.insert(0, str(areaPentagon))
            entryAreaPentagon.update()
            entryPerimeterPentagon.delete(0, END)
            entryPerimeterPentagon.insert(0, str(perimeterPentagon))
            entryPerimeterPentagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterPentagon.get()) == 0 and len(entrySidePentagon.get()) == 0 and len(entryAreaPentagon.get()) == 0:
        labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='red')
        return
    else:
        labelInstruct.configure(text="Enter exactly 1 value", font='Helvetica 16 bold', fg='red')
        return


def solve_hexagon():
    if len(entrySideHexagon.get()) != 0:
        try:
            float(entrySideHexagon.get())
            varSideHexagon = float(inputSideHexagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entrySideHexagon.delete(0, END)
            entrySideHexagon.update()
            return
    if len(entryAreaHexagon.get()) != 0:
        try:
            float(entryAreaHexagon.get())
            varAreaHexagon = float(inputAreaHexagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryAreaHexagon.delete(0, END)
            entryAreaHexagon.update()
            return
    if len(entryPerimeterHexagon.get()) != 0:
        try:
            float(entryPerimeterHexagon.get())
            varPerimeterHexagon = float(inputPerimeterHexagon.get())
        except ValueError:
            labelInstruct.configure(text="Input numbers only", font='Helvetica 16 bold', fg='red')
            entryPerimeterHexagon.delete(0, END)
            entryPerimeterHexagon.update()
            return
    if len(entryPerimeterHexagon.get()) != 0 and len(entrySideHexagon.get()) == 0 and len(entryAreaHexagon.get()) == 0:
        sideHexagon = varPerimeterHexagon / 6
        areaHexagon = 2.59807 * (sideHexagon ** 2)
        perimeterHexagon = varPerimeterHexagon
        if sideHexagon > 0 and areaHexagon > 0 and perimeterHexagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideHexagon.delete(0, END)
            entrySideHexagon.insert(0, str(sideHexagon))
            entrySideHexagon.update()
            entryAreaHexagon.delete(0, END)
            entryAreaHexagon.insert(0, str(areaHexagon))
            entryAreaHexagon.update()
            entryPerimeterHexagon.delete(0, END)
            entryPerimeterHexagon.insert(0, str(perimeterHexagon))
            entryPerimeterHexagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterHexagon.get()) == 0 and len(entrySideHexagon.get()) != 0 and len(entryAreaHexagon.get()) == 0:
        sideHexagon = varSideHexagon
        areaHexagon = 2.59807 * (sideHexagon ** 2)
        perimeterHexagon = varSideHexagon * 6
        if sideHexagon > 0 and areaHexagon > 0 and perimeterHexagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideHexagon.delete(0, END)
            entrySideHexagon.insert(0, str(sideHexagon))
            entrySideHexagon.update()
            entryAreaHexagon.delete(0, END)
            entryAreaHexagon.insert(0, str(areaHexagon))
            entryAreaHexagon.update()
            entryPerimeterHexagon.delete(0, END)
            entryPerimeterHexagon.insert(0, str(perimeterHexagon))
            entryPerimeterHexagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterHexagon.get()) == 0 and len(entrySideHexagon.get()) == 0 and len(entryAreaHexagon.get()) != 0:
        sideHexagon = (3 ** 0.25) * (sqrt(2 * (varAreaHexagon / 9)))
        areaHexagon = varAreaHexagon
        perimeterHexagon = sideHexagon * 6
        if sideHexagon > 0 and areaHexagon > 0 and perimeterHexagon > 0:
            labelInstruct.configure(text="Solution Displayed", font='Helvetica 16 bold', fg='green')
            labelInstruct.update()
            entrySideHexagon.delete(0, END)
            entrySideHexagon.insert(0, str(sideHexagon))
            entrySideHexagon.update()
            entryAreaHexagon.delete(0, END)
            entryAreaHexagon.insert(0, str(areaHexagon))
            entryAreaHexagon.update()
            entryPerimeterHexagon.delete(0, END)
            entryPerimeterHexagon.insert(0, str(perimeterHexagon))
            entryPerimeterHexagon.update()
            return
        else:
            labelInstruct.configure(text="Positive values only", font='Helvetica 16 bold', fg='red')
            return
    if len(entryPerimeterHexagon.get()) == 0 and len(entrySideHexagon.get()) == 0 and len(entryAreaHexagon.get()) == 0:
        labelInstruct.configure(text="Enter 1 of the values", font='Helvetica 16 bold', fg='red')
        return
    else:
        labelInstruct.configure(text="Enter exactly 1 value", font='Helvetica 16 bold', fg='red')
        return


planner = ttk.Notebook(root, width=450, height=315)

# Create the frames with specific pixel dimensions with the applications
# Next all the tabs are made with all the tkinter widgets for each being created.

######################################## Start Frame 1 ###################################

tab1 = Frame(planner, bg='light blue', width=200, height=200)

# Note that instead of root as the first attribute, tab1 is used so that the widget only shows in that tab.

# Buttons used to choose the shape of the tool.
buttonSquare = Button(tab1, text="Square", command=square, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonSquare.place(x=0, y=0)

buttonRectangle = Button(tab1, text="Rectangle", command=rectangle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonRectangle.place(x=89, y=0)

buttonCircle = Button(tab1, text="Circle", command=circle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonCircle.place(x=189, y=0)

buttonPentagon = Button(tab1, text="Pentagon", command=pentagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonPentagon.place(x=278, y=0)

buttonHexagon = Button(tab1, text="Hexagon", command=hexagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonHexagon.place(x=373, y=0)

labelInstruct = Label(tab1, text='Pick the shape above to use the tool!', bg='light blue', font='Helvetica 16 bold',
                      fg='black')
labelInstruct.place(x=100, y=100)

label1 = Label(tab1, bg='light blue', font='Helvetica 14 bold')
label2 = Label(tab1, bg='light blue', font='Helvetica 14 bold')
label3 = Label(tab1, bg='light blue', font='Helvetica 14 bold')
label4 = Label(tab1, bg='light blue', font='Helvetica 14 bold')

# Solve buttons below
# No locations are given as that is in the setup functions.
buttonSquareSolve = Button(tab1, text="Solve", command=solve_square, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonRectangleSolve = Button(tab1, text="Solve", command=solve_rectangle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonCircleSolve = Button(tab1, text="Solve", command=solve_circle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonPentagonSolve = Button(tab1, text="Solve", command=solve_pentagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonHexagonSolve = Button(tab1, text="Solve", command=solve_hexagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

# Clear Buttons
# No locations are given as that is in the setup functions.
buttonSquareClear = Button(tab1, text="Clear", command=clear_square, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonRectangleClear = Button(tab1, text="Clear", command=clear_rectangle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonCircleClear = Button(tab1, text="Clear", command=clear_circle, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonPentagonClear = Button(tab1, text="Clear", command=clear_pentagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonHexagonClear = Button(tab1, text="Clear", command=clear_hexagon, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

# All the entry boxes for user inputs
# No locations are given as that is in the setup functions.
entrySideSquare = Entry(tab1, textvariable=inputSideSquare)

entryPerimeterSquare = Entry(tab1, textvariable=inputPerimeterSquare)

entryAreaSquare = Entry(tab1, textvariable=inputAreaSquare)

entryLength = Entry(tab1, textvariable=inputLength)

entryWidth = Entry(tab1, textvariable=inputWidth)

entryPerimeterRectangle = Entry(tab1, textvariable=inputPerimeterRectangle)

entryAreaRectangle = Entry(tab1, textvariable=inputAreaRectangle)

entryRadiusCircle = Entry(tab1, textvariable=inputRadiusCircle)

entryDiameterCircle = Entry(tab1, textvariable=inputDiameterCircle)

entryAreaCircle = Entry(tab1, textvariable=inputAreaCircle)

entryCircumference = Entry(tab1, textvariable=inputCircumference)

entrySidePentagon = Entry(tab1, textvariable=inputSidePentagon)

entryAreaPentagon = Entry(tab1, textvariable=inputAreaPentagon)

entryPerimeterPentagon = Entry(tab1, textvariable=inputPerimeterPentagon)

entrySideHexagon = Entry(tab1, textvariable=inputSideHexagon)

entryAreaHexagon = Entry(tab1, textvariable=inputAreaHexagon)

entryPerimeterHexagon = Entry(tab1, textvariable=inputPerimeterHexagon)

squareCanvas = Canvas(tab1, bg="white", height=145, width=175)
squareCanvas.create_image(88, 75, image=squareImage)

rectangleCanvas = Canvas(tab1, bg="white", height=149, width=330)
rectangleCanvas.create_image(170, 78, image=rectangleImage)

circleCanvas = Canvas(tab1, bg="white", height=152, width=200)
circleCanvas.create_image(103, 79, image=circleImage)

pentagonCanvas = Canvas(tab1, bg="white", height=159, width=215)
pentagonCanvas.create_image(108, 82, image=pentagonImage)

hexagonCanvas = Canvas(tab1, bg="white", height=165, width=220)
hexagonCanvas.create_image(110, 87, image=hexagonImage)

######################################## End Frame 1 ###################################

####################################### Start Frame 2 ##################################

tab2 = Frame(planner, bg='light blue', width=200, height=200)

labelSymbolab = Message(tab2, text='We  are  currently  working  on a built-in 3D Shape tool for  this application. '
                                  'In the meanwhile, press the button below to open the Google calculator for the'
                                  'required shape. Thanks for your patience and understanding.', bg='light blue',
                                   font='Helvetica 16 bold', fg='black', width=420)

labelSymbolab.place(x=15, y=10)

buttonCube = Button(tab2, text="Cube", command=cube, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonCube.place(x=8, y=100)

buttonCuboid = Button(tab2, text="Cuboid", command=cuboid, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonCuboid.place(x=98, y=100)

buttonSphere = Button(tab2, text="Sphere", command=sphere, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonSphere.place(x=188, y=100)

buttonCylinder = Button(tab2, text="Cylinder", command=cylinder, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonCylinder.place(x=278, y=100)

buttonPyramid = Button(tab2, text="Pyramid", command=pyramid, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonPyramid.place(x=368, y=100)

shapecanvas = Canvas(tab2, bg="white", height=159, width=400)
shapecanvas.create_image(203, 82, image=google)
shapecanvas.place(x=30, y=140)

######################################## End Frame 2 ###################################

####################################### Start Frame 3 ##################################

tab3 = Frame(planner, bg='light blue', width=200, height=200)

# Creating all of the labels with the text information
# Based on mathematical convention, sides use lowercase letter a,  and angles use capital letters.
labelTitle = Label(tab3, text='Enter 3 out of 6 values', bg='light blue', font='Helvetica 16 bold', fg='black')
labelSideA = Label(tab3, text='a:', bg='light blue', font='Helvetica 14 bold')
labelSideB = Label(tab3, text='b:', bg='light blue', font='Helvetica 14 bold')
labelSideC = Label(tab3, text='c:', bg='light blue', font='Helvetica 14 bold')
labelAngleA = Label(tab3, text='A:', bg='light blue', font='Helvetica 14 bold')
labelAngleB = Label(tab3, text='B:', bg='light blue', font='Helvetica 14 bold')
labelAngleC = Label(tab3, text='C:', bg='light blue', font='Helvetica 14 bold')

# Arranging all of the labels in with coordinates using place.
labelTitle.place(x=20, y=10)
labelSideA.place(x=10, y=42)
labelSideB.place(x=10, y=72)
labelSideC.place(x=10, y=102)
labelAngleA.place(x=230, y=42)
labelAngleB.place(x=230, y=72)
labelAngleC.place(x=230, y=102)

# All the entries for the sides and angles with positions in the GUI.
entrySideA = Entry(tab3, textvariable=inputSideA)

entrySideA.place(x=30, y=40)

entrySideB = Entry(tab3, textvariable=inputSideB)

entrySideB.place(x=30, y=70)

entrySideC = Entry(tab3, textvariable=inputSideC)

entrySideC.place(x=30, y=100)

entryAngleA = Entry(tab3, textvariable=inputAngleA)

entryAngleA.place(x=255, y=40)

entryAngleB = Entry(tab3, textvariable=inputAngleB)

entryAngleB.place(x=255, y=70)

entryAngleC = Entry(tab3, textvariable=inputAngleC)

entryAngleC.place(x=255, y=100)

# Here is where we set up the button to perform "call" the calculation
# Calculation is performed when the "clicked" function is called
buttonSolve = Button(tab3, text="Solve", command=check_triangle_inputs, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonSolve.place(x=255, y=10)

buttonClear = Button(tab3, text="Clear", command=clear_triangle_inputs, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')
buttonClear.place(x=355, y=10)

trianglecanvas = Canvas(tab3, bg="blue", height=159, width=400)
trianglecanvas.create_image(203, 82, image=triangle_image)
trianglecanvas.place(x=30, y=140)

######################################## End Frame 3 ###################################

####################################### Start Frame 4 ##################################

tab4 = Frame(planner, bg='light blue', width=200, height=200)

# Creating all of the labels with the text information
labelSymbolab = Message(tab4, text='We  are  currently  working  on a built-in CAS tool for  this application. '
                                  'In the meanwhile, press the  button  below to open the Symbolab Step-by-Step '
                                  'Symbolic Calculator. Thanks for your patience and understanding.', bg='light blue',
                                   font='Helvetica 16 bold', fg='black', width=420)

labelSymbolab.place(x=15, y=10)

# Here is where we set up the button to open Desmos in a browser
buttonSymbolab = Button(tab4, text="Click to open Symbolab", command=Symbolab, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonSymbolab.place(x=150, y=100)

# This is for the placement of the image of the Symbolab logo
symbolabcanvas = Canvas(tab4, bg="white", height=159, width=400)
symbolabcanvas.create_image(203, 82, image=symbolab)
symbolabcanvas.place(x=30, y=140)

######################################## End Frame 4 ###################################

####################################### Start Frame 5 ##################################

tab5 = Frame(planner, bg='light blue', width=200, height=200)

# Creating all of the labels with the text information
labelDesmos = Message(tab5, text='We  are  currently  working  on a built-in Graphing tool for this application. '
                                  'In the meanwhile, press the button below to open the Desmos Advanced Graphing '
                                  'Calculator. Thanks for your patience and understanding.', bg='light blue',
                                   font='Helvetica 16 bold', fg='black', width=420)

labelDesmos.place(x=15, y=10)

# Here is where we set up the button to open Desmos in a browser
buttonDesmos = Button(tab5, text="Click to open Desmos", command=Desmos, background='#7A7A7A', overbackground='#7A7A7B',
                     foreground='#FFFFFF')

buttonDesmos.place(x=150, y=100)

# This is for the placement of the image of the Desmos logo
desmoscanvas = Canvas(tab5, bg="white", height=159, width=400)
desmoscanvas.create_image(203, 82, image=desmos)
desmoscanvas.place(x=30, y=140)


######################################## End Frame 5 ###################################

# Add the tabs/frames to the notebook object called "planner"
planner.add(tab1, text='2D Shapes')
planner.add(tab2, text='3D Shapes')
planner.add(tab3, text='Triangle Solver')
planner.add(tab4, text="CAS")
planner.add(tab5, text="Graphing")

# Tabs will be added to the "top" of the "frame"
planner.grid(row=0, column=0)

# Main tkinter loop so that the program runs until closed.
root.mainloop()
