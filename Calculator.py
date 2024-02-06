from tkinter import *
import math
import random
import cmath

#main window set up
root = Tk()
root.title("Calculator")
root.iconbitmap('blackheart.ico')

#frame set up that holds each button
frame1 = Frame(root)
frame1.grid(row=1, column=1)
frame2 = Frame(root)


# entry box
e = Entry(root, width=32, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

count = 0 #variable that determines if numbers are concatenated or replace string in entry box
secChoice = 0 #variable for 2nd button to swap out different buttons
userChoice = 'e' #variable that determines operation to perform
count2 = 0 #variable used in clear to remove all stored data
trigswap = 1 #variable for if calculator is in degree or radian mode
num1 = None

# button commands that enters numbers into entry box
def num_add(n) :
    global count
    
    if count == 0 :
        e.delete(0,END)

    current = e.get()
    e.delete(0, END)
    if n == 10:
        e.insert(0, str(current) + '.')
        count = 1
    elif n == 11:
        e.delete(0, END)
        e.insert(0, str(math.pi))
        count = 0
    elif n == 12:
        e.delete(0, END)
        e.insert(0, str(math.e))
        count = 0
    else :
        e.insert(0, str(current) + str(n))
        count = 1

# basic standard mode functions

# clears out the entry box
def clear_e():
    global count2
    global num1
    global userChoice
    userChoice = 'e'
    count2 = count2 + 1
    
    if count2 > 0 :
        num1 = None
        count2 = 0

    e.delete(0, END)

# multiplies numbers by -1 to swap the signs
def num_invert():
    num = e.get()
    invert = float(num) * (-1)
    
    if invert.is_integer() :
       invert = int(invert)
    e.delete(0, END)
    e.insert(0, invert)

# divides by 100 to change the entry to a percentage
def percentage():
    num = e.get()
    percent = float(num) / (100)

    if percent.is_integer() :
       percent = int(percent)
    e.delete(0, END)
    e.insert(0, percent)

# stores number into variable and changes the user choice 
# so that the operation performed is division
def divide():
    global userChoice
    global num1
    global count
    if userChoice != 'e' :
        eq()
        
    userChoice = 'd'
    num = e.get()
    num1 = float(num)
    count = 0

# stores number into variable and changes the user choice 
# so that the operation performed is multipulcation
def mult():
    global userChoice
    global num1
    global count
    if userChoice != 'e' :
        eq()
        
    userChoice = 'm'
    num = e.get()
    num1 = float(num)
    count = 0

# stores number into variable and changes the user choice 
# so that the operation performed is subtraction
def subtract():
    global userChoice
    global num1
    global count
    if userChoice != 'e' :
        eq()
        
    userChoice = 's'
    num = e.get()
    num1 = float(num)
    count = 0
    
# stores number into variable and changes the user choice 
# so that the operation performed is addition    
def addition():
    global userChoice
    global num1
    global count
    if userChoice != 'e' :
        eq()
        
    userChoice = 'a'
    num = e.get()
    num1 = float(num)
    count = 0

# uses a previously stored number and a second entered number to perform
# an operation depending on what the userChoice variable is
def eq():
    global userChoice
    global count
    count = 0
    num2 = float(e.get())
    match userChoice:
        case 'e':
            num3 = float(e.get())
            
        case 'a':
            num3 = num1 + num2
            
        case 's':
            num3 = num1 - num2
        
        case 'm':
            num3 = num1 * num2
            
        case 'd':
            num3 = num1 / num2
            
        case 'n':
            num3 = num1 ** num2
            
        case 'r':
            num3 = num1 ** (1. / num2)
                       
        case 'l':
            num3 = math.log(num1, num2)
             
        case 't':
            num3 = num1 * (10 ** num2)
    
    userChoice = 'e'
    if num3.is_integer() :
        num3 = int(num3)
    e.delete(0, END)
    e.insert(0, num3)

# scientific mode functions

# inverses the number by using 1/num
def revs() :
    global count
    count = 0
    num = e.get()
    flip = 1. / float(num)

    if flip.is_integer() :
       flip = int(flip)
    e.delete(0, END)
    e.insert(0, flip)

# squares the current number
def squared() :
    global count
    count = 0
    num = e.get()
    sq = float(num) ** 2
    
    if sq.is_integer() :
        sq = int(sq)
    e.delete(0, END)
    e.insert(0, sq)

# cubes the current number
def cubed() :
    global count
    count = 0
    num = e.get()
    cb = float(num) ** 3
    
    if cb.is_integer() :
       cb = int(cb)
    e.delete(0, END)
    e.insert(0, cb)

#takes the square root of the current number    
def sq_rt() :
    global count
    count = 0
    num = e.get()
    num2 = float(num) ** .5
    
    if num2.is_integer() :
        num2 = int(num2)
    e.delete(0, END)
    e.insert(0, num2)

#takes the cube root of the current number
def cb_rt() :
    global count
    count = 0
    num = e.get()
    num2 = float(num) ** (1. / 3.)

    if num2.is_integer() :
        num2 = int(num2)
    e.delete(0, END)
    e.insert(0, num2)
    
# raises the current number to a user entered power
def nthpwr() :
    global userChoice
    global num1
    if userChoice != 'e' :
        eq()
        
    userChoice = 'n'
    num = e.get()
    num1 = float(num)
    e.delete(0, END)

# takes the nth root of the current number
def nthRoot() :
    global userChoice
    global num1
    if userChoice != 'e' :
        eq()
        
    userChoice = 'r'
    num = e.get()
    num1 = float(num)
    e.delete(0, END)

# raises 10 to the power of the current number
def basT() :
    global count
    count = 0
    num = e.get()
    num2 = 10 ** float(num)
    
    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# raises 2 to the power of the current number
def baseTwo() :
    global count
    count = 0
    num = e.get()
    num2 = 2 ** float(num)
    
    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# raises e to the power of the current number
def etoN() : 
    global count
    count = 0
    num = e.get()
    num2 = math.e ** float(num)

    if num2.is_integer() :
        num2 = int(num2)
    e.delete(0, END)
    e.insert(0, num2)

# takes log base 10 of the current number
def logrithmic() :
    global count
    count = 0
    num = e.get()
    num2 = math.log(float(num), 10)
    
    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# takes log base 2 of the current number
def logTwoFunct() :
    global count
    count = 0
    num = e.get()
    num2 = math.log(float(num), 2)
    
    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# takes the natural log of the current number
def natLog() :
    global count
    count = 0
    num = e.get()
    num2 = math.log(float(num))
    
    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# takes the log of a base that the user enters of the current number
def logNFunct() :
    global userChoice
    global num1
    if userChoice != 'e' :
        eq()
        
    userChoice = 'l'
    num = e.get()
    num1 = float(num)
    e.delete(0, END)

# finds the factorial of the current number  
def factorial() :
    global count
    count = 0
    num = e.get()
    num2 = math.factorial(float(num))

    if num2.is_integer() :
        num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)

# function for when users wants to use parentheses
def parent(n) :
    global savedUserChoice
    global num1
    global savedNum
    global userChoice
    global lParentheses
    global rParentheses
    global num1
    if n == 1:
        #left parentheses
        savedUserChoice = userChoice
        if num1 != None:
            savedNum = num1

        userChoice = 'e'

        parentheses.place(relx=.94, rely=.01)

        lParentheses.grid_forget()
        rParentheses.grid_forget()

        lParentheses = Button(frame2, text= '(', width=xp, height=yp, command= lambda: parent(1), state='disabled')
        rParentheses = Button(frame2, text= ')', width=xp, height=yp, command= lambda: parent(2))

        lParentheses.grid(row=0, column=0)
        rParentheses.grid(row=0, column=1)
        
    else :
        #right parentheses
        eq()

        userChoice = savedUserChoice
        num1 = savedNum

        parentheses.place_forget()
        lParentheses.grid_forget()
        rParentheses.grid_forget()

        lParentheses = Button(frame2, text= '(', width=xp, height=yp, command= lambda: parent(1))
        rParentheses = Button(frame2, text= ')', width= xp, height= yp, command= lambda: parent(2), state='disabled')

        lParentheses.grid(row=0, column=0)
        rParentheses.grid(row=0, column=1)
        
# performs different trig functions, based on button choice, on current number
def trig(n) :
    global count
    global trigswap
    count = 0
    num = float(e.get())
    match n :
        case 1 :
            #sin
            if trigswap == 1 :
                num2 = math.sin(math.radians(num))
            else :
                num2 = math.sin(num)
            
        case 2 :
            #cos
            if trigswap == 1 :
                num2 = math.cos(math.radians(num))
            else :
                num2 = math.cos(num)
            
        case 3 :
            #tan
            if trigswap == 1 :
                num2 = math.tan(math.radians(num))
            else :
                num2 = math.tan(num)
            
        case 4 :
            #arcsin
            if trigswap == 1 :
                num2 = math.asin(math.radians(num))
            else :
                num2 = math.asin(num)
            
        case 5 :
            #arccos
            if trigswap == 1 :
                num2 = math.acos(math.radians(num))
            else :
                num2 = math.acos(num)
            
        case 6 :
            #arctan
            if trigswap == 1 :
                num2 = math.atan(math.radians(num))
            else :
                num2 = math.atan(num)
            
        case 7 :
            #sinh
            if trigswap == 1 :
                num2 = cmath.sinh(math.radians(num))
            else :
                num2 = cmath.sinh(num)
            
        case 8 :
            #cosh
            if trigswap == 1 :
                cmath.cosh(math.radians(num))
            else :
                num2 = cmath.cosh(num)
            
        case 9 :
            #tanh
            if trigswap == 1 :
                num2 = cmath.tanh(math.radians(num))
            else :
                num2 = cmath.tanh(num)
            
        case 10 :
            #arcsinh
            if trigswap == 1 :
                num2 = cmath.asinh(math.radians(num))
            else :
                num2 = cmath.asinh(num)
            
        case 11 :
            #arccosh
            if trigswap == 1 :
                num2 = cmath.acosh(math.radians(num))
            else :
                num2 = cmath.acosh(num)
            
        case 12 :
            #arctanh
            if trigswap == 1 :
                num2 = cmath.atanh(math.radians(num))
            else :
                num2 = cmath.atanh(num)
            
    
    if num2.is_integer() :
       num2 = int(num2)

    e.delete(0, END)
    e.insert(0, num2)
    
# changes mode from either radians or degree
def trigswitch(n) :
    global trigswap
    if n == 1 :
        trigswap = n
        degree.grid_forget()
        radians.grid_forget()
        deg.place_forget()
        rad.place_forget()
        radians.grid(row=4, column=0)
        deg.place(relx=.02, rely=.01)

    else :
        trigswap = n
        radians.grid_forget()
        degree.grid_forget()
        deg.place_forget()
        rad.place_forget()
        degree.grid(row=4, column=0)
        rad.place(relx=.02, rely=.01)

# swaps out specific buttons 
def secondCommand() :
    global secChoice
    
    if secChoice == 0:
        sine.grid_forget()
        cosine.grid_forget()
        tangent.grid_forget()
        sinh.grid_forget()
        cosh.grid_forget()
        tanh.grid_forget()
        baseTen.grid_forget()
        naturalLog.grid_forget()
        logBtn.grid_forget()
        baseW.grid(row=1, column=5)
        logN.grid(row=2, column=4)
        logTwo.grid(row=2, column=5)
        invSine.grid(row=3, column=1)
        invCosine.grid(row=3, column=2)
        invTangent.grid(row=3, column=3)
        invSinh.grid(row=4, column=1)
        invCosh.grid(row=4, column=2)
        invTanh.grid(row=4, column=3)
        secChoice = 1
    else :
        baseW.grid_forget()
        logN.grid_forget()
        logTwo.grid_forget()
        invSine.grid_forget()
        invCosine.grid_forget()
        invTangent.grid_forget()
        invSinh.grid_forget()
        invCosh.grid_forget()
        invTanh.grid_forget()
        baseTen.grid(row=1, column=5)
        naturalLog.grid(row=2, column=4)
        logBtn.grid(row=2, column=5)
        sine.grid(row=3, column=1)
        cosine.grid(row=3, column=2)
        tangent.grid(row=3, column=3)
        sinh.grid(row=4, column=1)
        cosh.grid(row=4, column=2)
        tanh.grid(row=4, column=3)
        secChoice = 0

# will store a number so that the user can use that number at a later time
def memory(n) :
    global memNum
    global memoryRecall
    global count
    match n :
        case 1:
            #memory clear
            memNum = None
            memoryRecall.grid_forget()
            memoryRecall = Button(frame2, text='mr', width=xp, height=yp, command=lambda : memory(4), state='disabled')
            memoryRecall.grid(row=0, column=5)
        case 2:
            #memory add
            memNum = float(e.get())
            count = 0
            memoryRecall.grid_forget()
            memoryRecall = Button(frame2, text='mr', width=xp, height=yp, command=lambda : memory(4))
            memoryRecall.grid(row=0, column= 5)
        case 3:
            #memory subtract
            num = float(e.get())
            if num == memNum :
                memNum = 0
        case 4:
            #memory recall
            e.delete(0, END)
            count = 0
            e.insert(0, memNum)

# enters a random number from 0 - 1 
def rand() :
    global count
    rand = random.random()
    e.delete(0, END)
    count = 0
    e.insert(0, rand)

# multiplies the current number by 10 to a user defined number
def sciNot() :
    global userChoice
    global num1
    global count
    if userChoice != 'e' :
        eq()
        
    userChoice = 't'
    num = e.get()
    num1 = float(num)
    count = 0

# changes calculator into standard mode
def standard() :
    global e
    e.grid_forget()
    e = Entry(root, width=32, borderwidth=5)
    e.grid(row=0, column=0, columnspan=4)
    frame2.grid_forget()
    deg.place_forget()
    rad.place_forget()

# changes calculator into scientific mode
def scientific() :
    global e
    e = Entry(root, width=70, borderwidth=5)
    e.grid(row=0, column=0, columnspan=4)
    frame2.grid(row=1, column=0)
    if trigswap == 1 :
        deg.place(relx=.02, rely=.01)
    else :
        rad.place(relx=.02, rely =.01)



# menu options

menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='Standard', command=standard)
fileMenu.add_command(label="Scientific", command=scientific)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)
menuBar.add_cascade(label='File', menu=fileMenu)

# Label setup
deg = Label(root, text='Deg')
rad = Label(root, text='Rad')
parentheses = Label(root, text='( )')

#default width and height
xp = 6
yp = 2

# button creation for standard mode
clear_btn = Button(frame1, text='C', width= 6, height= 2, command=clear_e)

zero_btn = Button(frame1, text= '0', width= xp * 2 + 1, height= yp,padx=2.4999, command= lambda: num_add(0))
one_btn = Button(frame1, text= '1', width= xp, height= yp, command= lambda: num_add(1))
two_btn = Button(frame1, text= '2', width= xp, height= yp, command= lambda: num_add(2))
three_btn = Button(frame1, text= '3', width= xp, height= yp, command= lambda: num_add(3))
four_btn = Button(frame1, text= '4', width= xp, height= yp, command= lambda: num_add(4))
five_btn = Button(frame1, text= '5', width= xp, height= yp, command= lambda: num_add(5))
six_btn = Button(frame1, text= '6', width= xp, height= yp, command= lambda: num_add(6))
seven_btn = Button(frame1, text= '7', width= xp, height= yp, command= lambda: num_add(7))
eight_btn = Button(frame1, text= '8', width= xp, height= yp, command= lambda: num_add(8))
nine_btn = Button(frame1, text= '9', width= xp, height= yp, command= lambda: num_add(9))
dot_btn = Button(frame1, text= '.', width= xp, height= yp, command= lambda: num_add(10))

eq_btn = Button(frame1, text='=', width= xp, height= yp, command=eq)
percent_btn = Button(frame1, text='%', width= xp, height= yp, command=percentage)
div_btn = Button(frame1, text='/', width= xp, height= yp, command=divide)
mult_btn = Button(frame1, text='*', width= xp, height= yp, command=mult)
sub_btn = Button(frame1, text='-', width= xp, height= yp, command=subtract)
add_btn = Button(frame1, text='+', width= xp, height= yp, command=addition)
invert_btn = Button(frame1, text='+/-', width= xp, height= yp, command= num_invert)

# button creation for scientific mode

rev = Button(frame2, text= '1/x', width=xp, height=yp, command=revs)

square = Button(frame2, text='x\u00B2', width=xp, height=yp, command=squared)
cube = Button(frame2, text='x\u00B3', width=xp, height=yp, command=cubed)
nth = Button(frame2, text= 'x\u207F', width=xp, height=yp, command=nthpwr)
sqrt = Button(frame2, text= '\u221Ax', width=xp,height=yp, command=sq_rt)
cbrt = Button(frame2, text= '\u221Bx', width=xp, height=yp, command=cb_rt)
nthRt  = Button(frame2, text= '\u207F\u221Ax', width=xp, height=yp, command=nthRoot)

eulerPwr = Button(frame2, text= 'e\u207F', width=xp, height=yp, command=etoN)
baseTen = Button(frame2, text= '10\u207F', width=xp, height=yp, command= basT)
baseW = Button(frame2, text='2\u207F', width=xp, height=yp, command=baseTwo)
logBtn = Button(frame2, text = 'log', width=xp, height=yp, command= logrithmic)
logTwo = Button(frame2, text= 'log\u0032', width=xp, height=yp, command= logTwoFunct)
naturalLog = Button(frame2, text= 'ln', width=xp , height=yp , command= natLog)
logN = Button(frame2, text= 'log\u2099', width=xp, height=yp, command=logNFunct)

fact = Button(frame2, text= 'x!', width= xp, height= yp, command= factorial)

piBtn = Button(frame2, text= '\u03C0', width=xp, height=yp, command= lambda: num_add(11))
eulerBtn = Button(frame2, text = 'e', width= xp, height=yp, command= lambda: num_add(12))

lParentheses = Button(frame2, text= '(', width=xp, height=yp, command= lambda: parent(1))
rParentheses = Button(frame2, text= ')', width= xp, height= yp, command= lambda: parent(2), state='disabled')

sine = Button(frame2, text= 'sin', width= xp, height=yp, command= lambda: trig(1))
cosine = Button(frame2, text= 'cos', width= xp, height=yp, command= lambda: trig(2))
tangent = Button(frame2, text= 'tan', width= xp, height=yp, command= lambda: trig(3))
invSine = Button(frame2, text='sin\u207B\u00B9', width=xp, height= yp, command= lambda : trig(4))
invCosine = Button(frame2, text='cos\u207B\u00B9', width=xp, height= yp, command= lambda : trig(5))
invTangent = Button(frame2, text='tan\u207B\u00B9', width=xp, height= yp, command= lambda : trig(6))
sinh = Button(frame2, text='sinh', width=xp, height=yp, command= lambda : trig(7))
cosh = Button(frame2, text='cosh', width=xp, height=yp, command= lambda : trig(8))
tanh = Button(frame2, text='tanh', width=xp, height=yp, command= lambda : trig(9))
invSinh = Button(frame2, text='sinh\u207B\u00B9', width=xp, height= yp, command= lambda : trig(10))
invCosh = Button(frame2, text='cosh\u207B\u00B9', width=xp, height= yp, command= lambda : trig(11))
invTanh = Button(frame2, text='tanh\u207B\u00B9', width=xp, height= yp, command= lambda : trig(12))
degree = Button(frame2, text='Deg', width=xp, height=yp, command= lambda : trigswitch(1))
radians = Button(frame2, text='Rad', width=xp, height=yp, command= lambda : trigswitch(2))

second = Button(frame2, text= '2nd', width=xp, height=yp, command= secondCommand)

memoryClear = Button(frame2, text= 'mc', width=xp, height=yp, command=lambda : memory(1))
memoryAdd = Button(frame2, text='m+', width=xp, height=yp, command=lambda : memory(2))
memorySub = Button(frame2, text='m-', width=xp, height=yp, command=lambda : memory(3))
memoryRecall = Button(frame2, text='mr', width=xp, height=yp, command=lambda : memory(4), state='disabled')

randomBtn = Button(frame2, text='Rand', width=xp, height=yp, command=rand)

scientificNotation = Button(frame2, text= 'EE', width=xp, height=yp, command=sciNot)



# button placing
clear_btn.grid(row=1,column=0)
invert_btn.grid(row=1,column=1)
percent_btn.grid(row=1,column=2)
div_btn.grid(row=1,column=3)

seven_btn.grid(row=2,column=0)
eight_btn.grid(row=2,column=1)
nine_btn.grid(row=2,column=2)
mult_btn.grid(row=2,column=3)

four_btn.grid(row=3,column=0)
five_btn.grid(row=3,column=1)
six_btn.grid(row=3,column=2)
sub_btn.grid(row=3,column=3)

one_btn.grid(row=4,column=0)
two_btn.grid(row=4,column=1)
three_btn.grid(row=4,column=2)
add_btn.grid(row=4,column=3)

zero_btn.grid(row=5,column=0, columnspan=2)
dot_btn.grid(row=5, column=2)
eq_btn.grid(row=5,column=3)

# scientific btn placing
lParentheses.grid(row=0, column=0)
rParentheses.grid(row=0, column=1)
memoryClear.grid(row=0, column=2)
memoryAdd.grid(row=0, column=3)
memorySub.grid(row=0, column=4)

memoryRecall.grid(row=0, column=5)
second.grid(row=1, column=0)
square.grid(row=1, column=1)
cube.grid(row=1, column=2)
nth.grid(row=1, column=3)
eulerPwr.grid(row=1, column=4)
baseTen.grid(row=1, column=5)

rev.grid(row=2, column=0)
sqrt.grid(row=2, column=1)
cbrt.grid(row=2, column=2)
nthRt.grid(row=2, column=3)
naturalLog.grid(row=2, column=4)
logBtn.grid(row=2, column=5)

fact.grid(row=3, column=0)
sine.grid(row=3, column=1)
cosine.grid(row=3, column=2)
tangent.grid(row=3, column=3)
eulerBtn.grid(row=3, column=4)
scientificNotation.grid(row=3, column=5)

radians.grid(row=4, column=0)
sinh.grid(row=4, column=1)
cosh.grid(row=4, column=2)
tanh.grid(row=4, column=3)
piBtn.grid(row=4, column=4)
randomBtn.grid(row=4, column=5)


root.config(menu=menuBar)
root.mainloop()


exit()
