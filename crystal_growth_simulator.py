from tkinter import *
import tkinter.font as font
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
import math
import csv
from itertools import islice 
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x400")
root.title(" Crystal Growth Simulator")
#root.config(bg = "white")
######################### Frames, Windows and Tabs ###################################
frame_mid_section = Frame(root)
frame_mid_section.pack(fill = 'both', expand = True)

######################### Style ###################################
font1 = font.Font(size = 20)
font2 = font.Font(size = 10)
######################### Variables ###################################
v_pmax = 0
CsCo = []
data = {}

v_pmax = 0
flag1= 0
count_grad = 0
CsCo = []
data = {}
f = []
x = []
y = []
z = []

######################### CSV Parameters ###################################
csv_CsCo = []
csv_VsVo = []
csv_conc_solid_field = []

csv_vp = []

csv_temp = []
csv_v = []
csv_r = []

csv_growth = [[], [], [], [], [], []]

#### S
csv_column = []
csv_header = []
csv_values = []
csv_xvalues = []
csv_yvalues = []

csv_body_pr_cz = []
csv_body_gr = []

csv_body_pr_fz = []
csv_body_zl = []
csv_body_cr = []



############# Process Options #########
Crystal_Process = [
	"Czochralski Process",
	"Float Zone Process"
]

Dopant = [
	"Aluminium (Al)",
	"Antimony (Sb)",
	"Arsenic (As)",
	"Boron (B)",
	"Carbon (C)",
	"Gallium (Ga)",
	"Gold (Au)",
	"Oxygen (O)",
	"Phosphorous (P)",
	"Custom"
]

conv = [
	"mm <-> cm",
	"mm <-> inches",
	"mm <-> m",
	"cm <-> inches",
	"cm <-> m",
	"inches <-> m",
	"per hr <-> per min <-> per sec",
	"KJ/Kg <-> cal/gm",
	"gm/cm3 <-> kg/m3",
	"Celcius <-> Fahrenheit <-> Kelvin"

]	


############# FZ Variables #########
#### Maximum Zone Length Variables ####
g_acc = 9.81

############# CZ Variables #########
#### Maximum Pull Rate Variables ####
latent_heat_fusion_silicon = 430.00
density_silicon = 2.328
stefan_boltzmman_constant = 5.67e-5
emissivity_silicon = 0.55
thermal_conductivity_silicon = 0.048
meting_temp_silicon = 1690.00

specific_heat_silicon = 0.392e-3
thermal_conductivity = 0.02
ha = 6.43e-6
#### Segregation Coeff ####
k_Al = 0.002
k_Sb = 0.023
k_As = 0.3
k_B = 0.72
k_C = 0.07
k_Ga = 0.008
k_Au = 0.000025
k_O = 0.5
k_P =  0.35
k_custom = 1
kseg = [k_Al, k_Sb, k_As, k_B, k_C, k_Ga, k_Au, k_O, k_P, k_custom]

######################### Converter ###################################

def mm_cm_calc(answer0,answer1):
	r = float(entconv1.get())/10
	answer0.set(r)

	q = float(entconv2.get())*10
	answer1.set(q)

def mm_cm():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "mm: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "cm: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "cm: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "mm: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: mm_cm_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def mm_inches_calc(answer0,answer1):
	r = float(entconv1.get())/(10*2.54)
	answer0.set(r)

	q = float(entconv2.get())*10*2.54
	answer1.set(q)

def mm_inches():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "mm: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "inches: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "inches: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "mm: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: mm_inches_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def mm_m_calc(answer0,answer1):
	r = float(entconv1.get())/(1000)
	answer0.set(r)

	q = float(entconv2.get())*1000
	answer1.set(q)

def mm_m():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "mm: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "m: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "m: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "mm: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: mm_m_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def cm_inches_calc(answer0,answer1):
	r = float(entconv1.get())/(2.54)
	answer0.set(r)

	q = float(entconv2.get())*2.54
	answer1.set(q)

def cm_inches():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "cm: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "inches: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "inches: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "cm: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: cm_inches_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def cm_m_calc(answer0,answer1):
	r = float(entconv1.get())/(100)
	answer0.set(r)

	q = float(entconv2.get())*100
	answer1.set(q)

def cm_m():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "cm: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "m: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "m: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "cm: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: cm_m_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def inches_m_calc(answer0,answer1):
	r = float(entconv1.get())*2.54/100
	answer0.set(r)

	q = float(entconv2.get())*100/2.54
	answer1.set(q)

def inches_m():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "inches: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "m: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "m: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "inches: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: inches_m_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def per_hr_min_sec_calc(answer0,answer1, answer2,answer3, answer4,answer5):
	answer0.set(float(entconv1.get())/60)
	answer1.set(float(entconv2.get())*60)
	
	answer2.set(float(entconv1.get())/3600)
	answer3.set(float(entconv2.get())/60)

	answer4.set(float(entconv3.get())*3600)
	answer5.set(float(entconv3.get())*60)

def per_hr_min_sec():
	global entconv1
	global entconv2
	global entconv3

	lbl1 = Label(bottomframe, text = "per hour: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	answer2 = IntVar()
	lbl3 = Label(bottomframe, text = "per min: ")
	lbl2 = Label(bottomframe, textvariable = answer0)
	lbl7 = Label(bottomframe, text = "per sec: ")
	lbl8 = Label(bottomframe, textvariable = answer2)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	lbl8.grid(row=3, column=1)
	lbl7.grid(row=3, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "per min ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	answer3 = IntVar()
	lbl5 = Label(bottomframe, text = "per hour: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	lbl9 = Label(bottomframe, text = "per sec: ")
	lbl10 = Label(bottomframe, textvariable = answer3)
	

	lbl4.grid(row=1, column=2, padx=(20,0))
	lbl5.grid(row=2, column=2, padx=(20,0))
	lbl6.grid(row=2, column=3)
	lbl9.grid(row=3, column=2, padx=(20,0))
	lbl10.grid(row=3, column=3)
	entconv2.grid(row=1,column=3)

	



	lbl11 = Label(bottomframe, text = "per sec: ")
	entconv3= Entry(bottomframe, text = "")
	entconv3.insert(END, '0')
	answer4 = IntVar()
	answer5 = IntVar()
	lbl12 = Label(bottomframe, text = "per hour: ")
	lbl13 = Label(bottomframe, textvariable = answer4)
	lbl14 = Label(bottomframe, text = "per min: ")
	lbl15 = Label(bottomframe, textvariable = answer5)

	lbl11.grid(row=1, column=4, padx=(20,0))
	lbl13.grid(row=2, column=5)
	lbl12.grid(row=2, column=4, padx=(20,0))
	lbl15.grid(row=3, column=5)
	lbl14.grid(row=3, column=4, padx=(20,0))
	entconv3.grid(row=1,column=5)


	mybutton = Button(bottomframe, text="Next", command = lambda: per_hr_min_sec_calc(answer0,answer1, answer2,answer3, answer4,answer5), width = 10, relief="raised",borderwidth = 3)
	mybutton.grid(row=4, column=3)

def kjkg_calgm_calc(answer0,answer1):
	r = float(entconv1.get())*0.239
	answer0.set(r)

	q = float(entconv2.get())*4.184
	answer1.set(q)

def kjkg_calgm():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "KJ/Kg: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "cal/gm: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "cal/gm: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "KJ/Kg: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: kjkg_calgm_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def gmcm3_kgm3_calc(answer0,answer1):
	r = float(entconv1.get())*1000
	answer0.set(r)

	q = float(entconv2.get())/1000
	answer1.set(q)

def gmcm3_kgm3():
	global entconv1
	global entconv2

	lbl1 = Label(bottomframe, text = "gm/cm3: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	lbl3 = Label(bottomframe, text = "kg/m3: ")
	lbl2 = Label(bottomframe, textvariable = answer0)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "kg/m3: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	lbl5 = Label(bottomframe, text = "gm/cm3: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	mybutton = Button(bottomframe, text="Next", command = lambda: gmcm3_kgm3_calc(answer0,answer1), width = 10, relief="raised",borderwidth = 3)

	lbl4.grid(row=1, column=2, padx=20)
	lbl5.grid(row=2, column=2, padx=20)
	lbl6.grid(row=2, column=3)
	entconv2.grid(row=1,column=3)

	mybutton.grid(row=3, column=2)

def c_f_calc(answer0,answer1, answer2,answer3, answer4,answer5):
	answer0.set((float(entconv1.get())*(9/5)) + 32.0)
	answer1.set((float(entconv2.get()) - 32.0)*(5/9))
	
	answer2.set(float(entconv1.get()) + 273.15)
	answer3.set((float(entconv2.get())-32.0)*(5/9) + 273.15)

	answer4.set((((float(entconv3.get()) - 273.15))*(9/5)) + 32.0)
	answer5.set(float(entconv3.get()) - 273.15)

def c_f():
	global entconv1
	global entconv2
	global entconv3

	lbl1 = Label(bottomframe, text = "Celcius: ")
	entconv1= Entry(bottomframe, text = "")
	entconv1.insert(END, '0')
	answer0 = IntVar()
	answer2 = IntVar()
	lbl3 = Label(bottomframe, text = "Fahrenheit: ")
	lbl2 = Label(bottomframe, textvariable = answer0)
	lbl7 = Label(bottomframe, text = "Kelvin: ")
	lbl8 = Label(bottomframe, textvariable = answer2)

	lbl1.grid(row=1, column=0)
	lbl2.grid(row=2, column=1)
	lbl3.grid(row=2, column=0)
	lbl8.grid(row=3, column=1)
	lbl7.grid(row=3, column=0)
	entconv1.grid(row=1,column=1)


	lbl4 = Label(bottomframe, text = "Fahrenheit: ")
	entconv2= Entry(bottomframe, text = "")
	entconv2.insert(END, '0')
	answer1 = IntVar()
	answer3 = IntVar()
	lbl5 = Label(bottomframe, text = "Celcius: ")
	lbl6 = Label(bottomframe, textvariable = answer1)
	lbl9 = Label(bottomframe, text = "Kelvin: ")
	lbl10 = Label(bottomframe, textvariable = answer3)
	

	lbl4.grid(row=1, column=2, padx=(20,0))
	lbl5.grid(row=2, column=2, padx=(20,0))
	lbl6.grid(row=2, column=3)
	lbl9.grid(row=3, column=2, padx=(20,0))
	lbl10.grid(row=3, column=3)
	entconv2.grid(row=1,column=3)

	



	lbl11 = Label(bottomframe, text = "Kelvin: ")
	entconv3= Entry(bottomframe, text = "")
	entconv3.insert(END, '0')
	answer4 = IntVar()
	answer5 = IntVar()
	lbl12 = Label(bottomframe, text = "Fahrenheit: ")
	lbl13 = Label(bottomframe, textvariable = answer4)
	lbl14 = Label(bottomframe, text = "Celcius: ")
	lbl15 = Label(bottomframe, textvariable = answer5)

	lbl11.grid(row=1, column=4, padx=(20,0))
	lbl13.grid(row=2, column=5)
	lbl12.grid(row=2, column=4, padx=(20,0))
	lbl15.grid(row=3, column=5)
	lbl14.grid(row=3, column=4, padx=(20,0))
	entconv3.grid(row=1,column=5)


	mybutton = Button(bottomframe, text="Next", command = lambda: c_f_calc(answer0,answer1, answer2,answer3, answer4,answer5), width = 10, relief="raised",borderwidth = 3)
	mybutton.grid(row=4, column=3)



def conv_option():
	for widget in bottomframe.winfo_children():
		widget.destroy()
	#mylabel = Label(bottomframe, text = clicked.get()).pack()

	if clicked.get() == conv[0]:
		mm_cm()
	elif clicked.get() == conv[1]:
		mm_inches()
	elif clicked.get() == conv[2]:
		mm_m()
	elif clicked.get() == conv[3]:
		cm_inches()
	elif clicked.get() == conv[4]:
		cm_m()
	elif clicked.get() == conv[5]:
		inches_m()
	elif clicked.get() == conv[6]:
		per_hr_min_sec()
	elif clicked.get() == conv[7]:
		kjkg_calgm()
	elif clicked.get() == conv[8]:
		gmcm3_kgm3()
	elif clicked.get() == conv[9]:
		c_f()

def converter_calc():
	global bottomframe
	global clicked

	top = Toplevel()
	top.geometry("600x200")
	top.title(" Converter")
	frame = Frame(top)
	frame.pack()

	bottomframe = Frame(top)
	bottomframe.pack(pady=20)


	clicked = StringVar()
	clicked.set(conv[0])

	drop = OptionMenu(frame, clicked, *conv).pack(side = LEFT)

	mybutton = Button(frame, text="Select", command = conv_option, width = 10, relief="raised",borderwidth = 3).pack(side = LEFT)
	#mybutton1 = Button(frame, text="Quit", command = main_window).pack(side = LEFT)

######################### Drop Down Menu ###################################

my_menu = Menu(root)
root.config(menu = my_menu)

# New Project
def new_proj():
	main_window()


def open_temp_gradient():
	x1 = []
	y1 = []
	z1 = []
	k1 = []
	r1 = []
	num = 0

	x1.clear()
	y1.clear()
	z1.clear()
	k1.clear()
	r1.clear()

	with open('Temperature Gradient vs Pull Rate_CZ.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x1.append(row)
			num = num + 1

	num = int((num - 2)/2)
	y1.append(x1[0])


	for i in range(1, num+1):
		z1.append(x1[2*i])

	#print(z)

	y1[0].pop(0)

	for i in range(num):
		temp = z1[i].pop(0)
		r1.append(temp)

	#print(z)

	a1 = []
	for i in z1:
		k1 = []
		for j in range(0, 10):
			k1.append(float(i[j])) 
		a1.append(k1)

	b1 = []
	for i in y1:
		k1 = []
		for j in range(0, 10):
			k1.append(float(i[j]))
		b1.append(k1) 

	#print(r1)

	num_only = [float(sub.split('=')[1]) for sub in r1] 
	#print(num_only)
	
	for i in range(num):
		plt.plot(b1[0], a1[i], label = "R=" + str(num_only[i]))

	ax = plt.gca()
	#plt.plot(x,y, label = "R="+str(r)+"mm")
	plt.ylabel('Temp Gradient: dT/dz (C/mm)')
	plt.xlabel('Pull Rate: v (mm/min) ')
	ax.set_title('Temerature Gradient VS Pull Rate')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5)
	plt.grid()
	plt.show()

def open_doping_vs_conc(option):
	x1 = []
	y1 = []
	z1 = []
	k1 = []
	Dopant1= []
	num = 0
	x1.clear()
	y1.clear()
	z1.clear()
	k1.clear()
	Dopant1.clear()


	if option == 1:
		filename = 'Doping Concentration vs Fraction Solidfied_CZ.csv'
	elif option == 5:
		filename = 'Doping Concentration vs Fraction Solidfied_FZ.csv'

	with open(filename,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x1.append(row)
			num = num + 1
			#y.append(row[1])

		num = int((num - 2)/2)
		y1.append(x1[0])


		for i in range(1, num+1):
			z1.append(x1[2*i])

	#print(z)

	y1[0].pop(0)

	for i in range(num):
		temp = z1[i].pop(0)
		Dopant1.append(temp)

	#print(z)

	a1 = []
	for i in z1:
		k1 = []
		for j in range(0, 10):
			k1.append(float(i[j])) 
		a1.append(k1)

	b1 = []
	for i in y1:
		k1 = []
		for j in range(0, 10):
			k1.append(float(i[j]))
		b1.append(k1) 

	#print(a)
	#print(b)
	#print(Dopant)

	for i in range(num):
		plt.semilogy(b1[0], a1[i], label = str(Dopant1[i]))

	ax = plt.gca()
	plt.tick_params(axis='y', which='minor')
	plt.grid()
	plt.ylabel('Cs/Co')
	plt.xlabel('Vs/Vo')
	ax.set_title('Doping Concentration vs Fraction Solidfied')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5)
	plt.tight_layout()
	plt.show()

def open_pull_rate(option):
	x1 = []
	z1 = []
	k1 = []
	r1 = []
	y1 = []
	num = 0

	x1.clear()
	y1.clear()
	z1.clear()
	k1.clear()
	r1.clear()

	if option == 2:
		filename = 'Maximum Pull Rate_CZ.csv'
	elif option == 6:
		filename = 'Maximum Pull Rate_FZ.csv'

	with open(filename,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x1.append(row)
			num = num + 1

	#print(x1)
	
	num = int((num - 2)/2)
	y1.append(x1[0])

	for i in range(1, num+1):
		z1.append(x1[2*i])

	#print(z)

	for i in range(num):
		temp = z1[i].pop(0)
		r1.append(temp)

	#print(z)

	a1 = []
	for i in z1:
		#k1.append(float(i[0])) 
		a1.append(float(i[0]))

	#print(r1)
	
	b1 = []
	for i in r1:
		#k1.append(float(i[0]))
		b1.append(float(i)) 

	print(a1)
	print(b1)
	print(y1)

	open_new_pull_rate_window = Toplevel()
	#t = Table(open_new_pull_rate_window)

	rows = len(a1)
	columns = len(y1[0])

	for i in range(rows+1):
		for j in range(columns):
			e = Entry(open_new_pull_rate_window, width=20, font=('Arial',16,'bold'))
			e.grid(row=i, column=j)
			if i==0:
				e.insert(END, y1[0][j])
			elif j == 0:
				e.insert(END, b1[i-1])
			elif j == 1:
				e.insert(END, a1[i-1])


def zonelength_coolingrate(option):
	x1 = []
	z1 = []
	k1 = []
	r1 = []
	y1 = []
	num = 0

	x1.clear()
	y1.clear()
	z1.clear()
	k1.clear()
	r1.clear()

	if option == 4:
		filename = 'Crytsal Growth Rate_CZ.csv'
	elif option == 7:
		filename = 'Maximum Zone Length_FZ.csv'
	elif option == 8:
		filename = 'Maximum Cooling Rate_FZ.csv'


	with open(filename,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x1.append(row)
			num = num + 1

	print(x1)
	
	num = int((num - 2)/2)

	for i in range(0, num+1):
		z1.append(x1[2*i])
	#print(z1)

	rows = len(z1)
	columns = len(z1[0])

	open_new_pull_rate_window = Toplevel()

	for i in range(rows):
		for j in range(columns):
			e = Entry(open_new_pull_rate_window, width=20, font=('Arial',16,'bold'))
			e.grid(row=i, column=j)
			e.insert(END, z1[i][j])


def open_option(option):
	if option == 1:
		open_doping_vs_conc(1)
	elif option == 2:
		open_pull_rate(2)
	elif option == 3:
		open_temp_gradient()
	elif option == 4:
		zonelength_coolingrate(4)	
	elif option == 5:
		open_doping_vs_conc(5)
	elif option == 6:
		open_pull_rate(6)
	elif option == 7:
		zonelength_coolingrate(7)
	elif option == 8:
		zonelength_coolingrate(8)


def open_proj():
	open_new = Toplevel()
	lbl = Label(open_new, text = "Select what to open").pack()

	r = IntVar()
	r.set("1")

	lbl2 = Label(open_new, text="Open Option For Czochralski").pack(anchor = W)
	Radiobutton(open_new, text="Doping Concentration vs Fraction Solidfied", variable=r, value=1).pack(anchor = W)
	Radiobutton(open_new, text="Pull Rate", variable=r, value=2).pack(anchor = W)
	Radiobutton(open_new, text="Temp Gradient vs Pull Velocity", variable=r, value=3).pack(anchor = W)
	Radiobutton(open_new, text="Groth Rate", variable=r, value=4).pack(anchor = W)

	lbl3 = Label(open_new, text="Open Option For Float Zone").pack(anchor = W)
	Radiobutton(open_new, text="Doping Concentration vs Fraction Solidfied", variable=r, value=5).pack(anchor = W)
	Radiobutton(open_new, text="Pull Rate", variable=r, value=6).pack(anchor = W)
	Radiobutton(open_new, text="Maximum Zone Length", variable=r, value=7).pack(anchor = W)
	Radiobutton(open_new, text="Maximum Cooling Rate", variable=r, value=8).pack(anchor = W)
	
	mybutton1 = Button(open_new, text="Select", command = lambda: open_option(r.get()), width = 10, relief="raised",borderwidth = 3).pack()


def clear_text():

	ent1.delete(0, END)
	ent2.delete(0, END)
	ent3.delete(0, END)
	ent4.delete(0, END)
	ent5.delete(0, END)


def cut_text():
	pass

def copy_text():
	pass

def paste_text():
	pass

def formula():
	webbrowser.open_new('Formula.pdf')

def manual():
	webbrowser.open_new('manual.pdf')
#################Create Menu Item ###################
##File Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label="New", command = new_proj)
file_menu.add_separator()
file_menu.add_command(label="Open", command = open_proj)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

##Edit Menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu = edit_menu)
edit_menu.add_command(label="Clear Input", command = clear_text)



##Help Menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu = help_menu)
help_menu.add_command(label="Converter", command = converter_calc)
help_menu.add_separator()
help_menu.add_command(label="View Formulas Used", command = formula)
help_menu.add_separator()
help_menu.add_command(label="View Manual", command = manual)
######################### CZ Window Display ###################################
def pull_rate_calc(answer):
	d = float(ent1.get())

	values = []
	values.append(d)

	r = d/2
	sq = (2*stefan_boltzmman_constant*emissivity_silicon*thermal_conductivity_silicon*(meting_temp_silicon**5)*(2.39e-8))/(3.0*r*2.54)
	v_pmax = 3600*(1/(latent_heat_fusion_silicon*density_silicon))*math.sqrt(sq)

	values.append(v_pmax)

	csv_values.clear()
	csv_values.append(values)
	
	answer.set(round(v_pmax,3))

def save_data_pr():
	for i in csv_values:
		csv_column.clear()
		csv_column.append("Diameter of Ingot Required (inches)")
		csv_column.append("Maximum Pull Rate (cm/hr)")
		
		csv_header.clear()
		csv_header.append(csv_column)

		if clicked_new.get() == "Czochralski Process":
			csv_body_pr_cz.append(csv_values[0])
			csv_temp = csv_body_pr_cz
			filename = "Maximum Pull Rate_CZ.csv"
		elif clicked_new.get() == "Float Zone Process":
			csv_body_pr_fz.append(csv_values[0])
			csv_temp = csv_body_pr_fz
			filename = "Maximum Pull Rate_FZ.csv"
			
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_header)
			csvwriter.writerows(csv_temp)

	csv_values.clear()

def max_pull_rate():
	root.geometry("450x400")
	for widget in frame_mid_section.winfo_children():
		widget.destroy()
	
	global ent1
	global lbl4
	
	lbl1 = Label(frame_mid_section, text="Maximum Pull Rate\n")
	lbl1['font'] = font1
	lbl2 = Label(frame_mid_section, text="Enter diameter of ingot required (inches): ")
	lbl3 = Label(frame_mid_section, text="Maximum Pull Rate (cm/hr): ")
	lbl2['font'] = font2
	lbl3['font'] = font2

	ent1 = Entry(frame_mid_section, text="")

	answer = IntVar()
	mybutton3 = Button(frame_mid_section, text="Enter", command = lambda: pull_rate_calc(answer), width = 10, relief="raised",borderwidth = 3)
	mybutton4 = Button(frame_mid_section, text="Back", command = process_window, width = 10, relief="raised",borderwidth = 3)
	mybutton5 = Button(frame_mid_section, text="Save Data", command = save_data_pr, width = 10, relief="raised",borderwidth = 3)

	lbl4 = Label(frame_mid_section, textvariable=answer)
	lbl4['font'] = font2

	lbl1.grid(row=0,column=0, columnspan=2)
	lbl2.grid(row=1,column=0)
	lbl3.grid(row=2,column=0)
	lbl4.grid(row=2,column=1)

	ent1.grid(row=1,column=1)

	mybutton3.grid(row=4,column=1,pady=10)
	mybutton4.grid(row=5,column=1,pady=10)
	mybutton5.grid(row=6,column=1,pady=10)

def plot_CsCo_cz():
	values = [(i, var.get()) for i, var in data.items()]
	custom_name = str(ent1.get())
	kseg[9] = float(ent2.get())
	print(kseg[9])
	CsCo.clear()
	csv_VsVo.clear()
	csv_CsCo.clear()

	for ko in kseg: 
		col = []
		x = []
		for i in np.arange(0,1,0.1):
			col.append(ko*((1-i)**(ko-1)))
			x.append(i)

		CsCo.append(col)

	k=0		
	if values[0][1] == 1:
		plt.semilogy(x,CsCo[0], label = "Aluminium")
		csv_CsCo.append(CsCo[0])
		csv_CsCo[k].insert(0, Dopant[0])
		k = k + 1
	if values[1][1] == 1:
		plt.semilogy(x,CsCo[1], label = "Antimony")
		csv_CsCo.append(CsCo[1])
		csv_CsCo[k].insert(0, Dopant[1])
		k = k + 1
	if values[2][1] == 1:
		plt.semilogy(x,CsCo[2], label = "Arsenic")
		csv_CsCo.append(CsCo[2])
		csv_CsCo[k].insert(0, Dopant[2])
		k = k + 1
	if values[3][1] == 1:
		plt.semilogy(x,CsCo[3], label = "Boron")
		csv_CsCo.append(CsCo[3])
		csv_CsCo[k].insert(0, Dopant[3])
		k = k + 1
	if values[4][1] == 1:
		plt.semilogy(x,CsCo[4], label = "Carbon")
		csv_CsCo.append(CsCo[4])
		csv_CsCo[k].insert(0, Dopant[4])
		k = k + 1
	if values[5][1] == 1:
		plt.semilogy(x,CsCo[5], label = "Gallium")
		csv_CsCo.append(CsCo[5])
		csv_CsCo[k].insert(0, Dopant[5])
		k = k + 1
	if values[6][1] == 1:
		plt.semilogy(x,CsCo[6], label = "Gold")
		csv_CsCo.append(CsCo[6])
		csv_CsCo[k].insert(0, Dopant[6])
		k = k + 1
	if values[7][1] == 1:
		plt.semilogy(x,CsCo[7], label = "Oxygen")
		csv_CsCo.append(CsCo[7])
		csv_CsCo[k].insert(0, Dopant[7])
		k = k + 1
	if values[8][1] == 1:
		plt.semilogy(x,CsCo[8], label = "Phosphorous")
		csv_CsCo.append(CsCo[8])
		csv_CsCo[k].insert(0, Dopant[8])
		k = k + 1
	if values[9][1] == 1:
		plt.semilogy(x,CsCo[9], label = custom_name)
		csv_CsCo.append(CsCo[9])
		csv_CsCo[k].insert(0, custom_name)
		k = k + 1
		
	if(k > 0):
		csv_VsVo.append(x)
		ax = plt.gca()
		plt.tick_params(axis='y', which='minor')
		plt.ylabel('Cs/Co')
		plt.xlabel('Vs/Vo')
		ax.set_title('Doping Concentration vs Fraction Solidfied')
		plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5)
		plt.tight_layout()
		plt.grid()
		plt.show()

def save_data_cz():
	for i in csv_VsVo:
		i.insert(0, "Fraction Solidfied-->")
		filename = "Doping Concentration vs Fraction Solidfied_CZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_VsVo)
			csvwriter.writerows(csv_CsCo)

	csv_VsVo.clear()
	csv_CsCo.clear()

def conc_impurities_solid_cz():
	global ent1 
	global ent2

	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	lbl1 = Label(frame_mid_section, text="Select the dopant for which Cs/Co vs Fraction of Melt Solidified graph is to be plotted (atleast one)\n")
	lbl1['font'] = font2
	lbl1.pack()

	for i in Dopant:
		var = IntVar()
		c = Checkbutton(frame_mid_section, text = i, variable = var, font = font2).pack(anchor = W, padx=20)
		data[i] = var

	ent1 = Entry(frame_mid_section, text="")
	ent1.pack(anchor = W, padx=30)
	ent1.insert(0,"Enter Name")
	ent2 = Entry(frame_mid_section, text="")
	ent2.pack(anchor = W, padx=30)
	ent2.insert(0, 1)

	mybutton1 = Button(frame_mid_section, text="Plot", command = plot_CsCo_cz, width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton2 = Button(frame_mid_section, text="Back", command = cz_window, width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton3 = Button(frame_mid_section, text="Save Data", command = save_data_cz, width = 10, relief="raised",borderwidth = 3).pack(pady=10)

def grad_calc():
	r = float(ent1.get())
	B = ha*r/(thermal_conductivity)
	x = []
	y = []
	Gs0 = (math.sqrt(8*B))*(1400 - 27)/(2*r)
	#print(Gs0)
	y.append(Gs0)
	x.append(0)
	for i in np.arange(0.1, 1, 0.05):
		W = (specific_heat_silicon*i*r)/(thermal_conductivity*60)
		Gs = (math.sqrt((8*B)+(W*W))-W)*(1400 - 27)/(2*r)
		#if i == 0.7:
		
		print(W)
		print(B)
		y.append(Gs)
		x.append(i)

		print(x)

	csv_xvalues.clear()
	#csv_yvalues.clear()
	global csv_y_temp

	csv_y_temp = y

	#print(csv_y_temp)
	csv_xvalues.append(x)
	#csv_yvalues.append(csv_y_temp)
	
	ax = plt.gca()
	plt.plot(x,y, label = "R="+str(r)+"mm")
	plt.ylabel('Temp Gradient: dT/dz (C/mm)')
	plt.xlabel('Pull Rate: v (mm/min) ')
	ax.set_title('Temerature Gradient VS Pull Rate')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5)
	plt.tight_layout()
	plt.grid()
	plt.show()

def save_data_tg():
	

	flag = 0
	for i in csv_xvalues:
		i.insert(0, "Pull Rate (mm/min) -->")
		flag=1
	if flag == 1:
		#print(csv_y_temp)
		csv_yvalues.append(csv_y_temp)
		#print(csv_yvalues)
		k=len(csv_yvalues)
		for i in csv_yvalues:
		#print(i)
			k = k - 1
			if k == 0:
				i.insert(0, "Temp Gradient (C/mm) for R = " + str(float(ent1.get())))

	#print(csv_xvalues)	
	#print(csv_yvalues)

	for i in csv_xvalues:
		#r = float(ent1.get())
		#csv_column.clear()
		#csv_column.append("Radius of Crystal (mm) -->")
		#csv_column.append(r)		
	
		csv_header.clear()
		csv_header.append(csv_column)
	
		filename = "Temperature Gradient vs Pull Rate_CZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			#csvwriter.writerows(csv_header)
			csvwriter.writerows(csv_xvalues)
			csvwriter.writerows(csv_yvalues)

	csv_xvalues.clear()
	#csv_yvalues.clear()

def temp_grad_boundary():
	root.geometry("400x400")
	csv_xvalues.clear()
	#csv_yvalues.clear()
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	global ent1
	lbl1 = Label(frame_mid_section, text="Temperature Gradient\n")
	lbl1['font'] = font1
	lbl2 = Label(frame_mid_section, text = "Enter radius of crystal (mm):")
	lbl2['font'] = font2
	ent1 = Entry(frame_mid_section, text="")

	lbl1.grid(row=0, column=0, columnspan=2)
	lbl2.grid(row=2, column=0)
	ent1.grid(row=2, column=1)

	mybutton1 = Button(frame_mid_section, text="Next", command = grad_calc, width = 10, relief="raised",borderwidth = 3)
	mybutton2 = Button(frame_mid_section, text="Back", command = cz_window, width = 10, relief="raised",borderwidth = 3)
	mybutton3 = Button(frame_mid_section, text="Save Data", command = save_data_tg, width = 10, relief="raised",borderwidth = 3)

	mybutton1.grid(row=5, column=1, pady = 10)
	mybutton2.grid(row=6, column=1, pady = 10)
	mybutton3.grid(row=7, column=1, pady = 10)

def growth_calc(answer):
	v = float(ent1.get())
	density_molten = float(ent2.get())
	density_solid = float(ent3.get())
	dia_crucible = float(ent4.get())
	dia_crystal = float(ent5.get())

	values = []
	values.append(v)
	values.append(density_molten)
	values.append(density_solid)
	values.append(dia_crucible)
	values.append(dia_crystal)

	f = v/(1-(density_solid/density_molten)*((dia_crystal/dia_crucible)**2))

	values.append(f)

	csv_values.clear()
	csv_values.append(values)
	
	answer.set(round(f,3))

def save_data_gr():
	for i in csv_values:
		csv_column.clear()
		csv_column.append("Pull Rate (mm/hr)")
		csv_column.append("Density of Molten State (g/cm^3)")
		csv_column.append("Density of Solid State (g/cm^3)")
		csv_column.append("Crucible Diameter (mm)")
		csv_column.append("Crystal Diameter (mm)")
		csv_column.append("Crystal Growth Rate (mm/hr)")		
		
		csv_header.clear()
		csv_header.append(csv_column)

		csv_body_gr.append(csv_values[0])
	
		filename = "Crytsal Growth Rate_CZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_header)
			csvwriter.writerows(csv_body_gr)

	csv_values.clear()

def crystal_growth_rate():
	root.geometry("450x500")
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	global ent1
	global ent2
	global ent3
	global ent4
	global ent5
	lbl1 = Label(frame_mid_section, text="Crystal Growth Rate\n")
	lbl1['font'] = font1
	lbl2 = Label(frame_mid_section, text = "Enter pull rate (mm/hr):")
	lbl2['font'] = font2
	lbl3 = Label(frame_mid_section, text = "Enter density of molten state (g/cm^3):")
	lbl3['font'] = font2
	lbl4 = Label(frame_mid_section, text = "Enter density of solid state: (g/cm^3)")
	lbl4['font'] = font2
	lbl5 = Label(frame_mid_section, text = "Enter crucible diameter (mm):")
	lbl5['font'] = font2
	lbl6 = Label(frame_mid_section, text = "Enter crystal diameter (mm):")
	lbl6['font'] = font2
	lbl7 = Label(frame_mid_section, text = "Crystal Growth Rate (mm/hr):")
	lbl7['font'] = font2
	
	ent1 = Entry(frame_mid_section, text="")
	ent2 = Entry(frame_mid_section, text="")
	ent3 = Entry(frame_mid_section, text="")
	ent4 = Entry(frame_mid_section, text="")
	ent5 = Entry(frame_mid_section, text="")

	lbl1.grid(row=0, column=0, columnspan=2, pady = 10)
	lbl2.grid(row=2, column=0)
	lbl3.grid(row=3, column=0)
	lbl4.grid(row=4, column=0)
	lbl5.grid(row=5, column=0)
	lbl6.grid(row=6, column=0)
	lbl7.grid(row=7, column=0, pady = 10)

	ent1.grid(row=2, column=1)
	ent2.grid(row=3, column=1)
	ent3.grid(row=4, column=1)
	ent4.grid(row=5, column=1)
	ent5.grid(row=6, column=1)


	answer = IntVar()
	mybutton1 = Button(frame_mid_section, text="Enter", command = lambda: growth_calc(answer), width = 10, relief="raised",borderwidth = 3)
	mybutton2 = Button(frame_mid_section, text="Back", command = cz_window, width = 10, relief="raised",borderwidth = 3)
	mybutton3 = Button(frame_mid_section, text="Save Data", command = save_data_gr, width = 10, relief="raised",borderwidth = 3)

	lbl8 = Label(frame_mid_section, textvariable=answer)
	lbl8['font'] = font2
	lbl8.grid(row=7, column=1)

	mybutton1.grid(row=8, column=1, pady=10)
	mybutton2.grid(row=9, column=1, pady=10)
	mybutton3.grid(row=10, column=1, pady=10)

def equation_option(option):
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	if(option == 1):
		root.title(" Maximum Pull Rate")
		max_pull_rate()
	if(option == 2):
		root.title(" Concentration Of Impurities In Solid Phase")
		conc_impurities_solid_cz()
	if(option == 3):
		root.title(" Crystal Growth Rate")
		crystal_growth_rate()
	if(option == 4):
		root.title(" Temperature Gradient At Boundary")
		temp_grad_boundary()


def cz_window():
	csv_values.clear()
	csv_VsVo.clear()
	csv_CsCo.clear()
	root.geometry("600x600")
	root.title(" Czochralski Process")
	
	for widget in frame_mid_section.winfo_children():
		widget.destroy()


	cz_lbl1 = Label(frame_mid_section, text = "Czochralski Process\n" , fg = 'red')
	cz_lbl1['font'] = font1
	cz_lbl1.pack(anchor = "n")

	cz_lbl2 = Label(frame_mid_section, text = "Select Appropriate Option", font = "Helvetica 10 bold")
	#cz_lbl2['font'] = font2
	cz_lbl2.pack(anchor = "w")
	r = IntVar()
	r.set("1")

	Radiobutton(frame_mid_section, text="Maximum Pull Rate", variable=r, value=1, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Concentration Of Impurities In Solid Phase", variable=r, value=2, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Crystal Growth Rate", variable=r, value=3, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Temperature Gradient At Boundary", variable=r, value=4, font = font2).pack(anchor = W)

	mybutton1 = Button(frame_mid_section, text="Select", command = lambda: equation_option(r.get()), width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton2 = Button(frame_mid_section, text="Back", command = main_window, width = 10, relief="raised",borderwidth = 3).pack(pady=10)

	my_img = ImageTk.PhotoImage(Image.open("Images/Webp.net-resizeimage.png"))
	img_lbl = Label(frame_mid_section, image = my_img)
	img_lbl.image = my_img
	img_lbl.pack()


######################### FZ Window Display ###################################

def plot_CsCo_fz():
	values = [(i, var.get()) for i, var in data.items()]
	custom_name = str(ent1.get())
	kseg[9] = float(ent2.get())
	CsCo.clear()
	csv_VsVo.clear()
	csv_CsCo.clear()

	for ko in kseg: 
		col = []
		x = []
		for i in np.arange(0,1,0.1):
			col.append(1-((1-ko)*np.exp(-1*ko*i)))
			x.append(i)

		CsCo.append(col)
	k=0		
	if values[0][1] == 1:
		plt.semilogy(x,CsCo[0], label = "Aluminium")
		csv_CsCo.append(CsCo[0])
		csv_CsCo[k].insert(0, Dopant[0])
		k = k + 1
	if values[1][1] == 1:
		plt.semilogy(x,CsCo[1], label = "Antimony")
		csv_CsCo.append(CsCo[1])
		csv_CsCo[k].insert(0, Dopant[1])
		k = k + 1
	if values[2][1] == 1:
		plt.semilogy(x,CsCo[2], label = "Arsenic")
		csv_CsCo.append(CsCo[2])
		csv_CsCo[k].insert(0, Dopant[2])
		k = k + 1
	if values[3][1] == 1:
		plt.semilogy(x,CsCo[3], label = "Boron")
		csv_CsCo.append(CsCo[3])
		csv_CsCo[k].insert(0, Dopant[3])
		k = k + 1
	if values[4][1] == 1:
		plt.semilogy(x,CsCo[4], label = "Carbon")
		csv_CsCo.append(CsCo[4])
		csv_CsCo[k].insert(0, Dopant[4])
		k = k + 1
	if values[5][1] == 1:
		plt.semilogy(x,CsCo[5], label = "Gallium")
		csv_CsCo.append(CsCo[5])
		csv_CsCo[k].insert(0, Dopant[5])
		k = k + 1
	if values[6][1] == 1:
		plt.semilogy(x,CsCo[6], label = "Gold")
		csv_CsCo.append(CsCo[6])
		csv_CsCo[k].insert(0, Dopant[6])
		k = k + 1
	if values[7][1] == 1:
		plt.semilogy(x,CsCo[7], label = "Oxygen")
		csv_CsCo.append(CsCo[7])
		csv_CsCo[k].insert(0, Dopant[7])
		k = k + 1
	if values[8][1] == 1:
		plt.semilogy(x,CsCo[8], label = "Phosphorous")
		csv_CsCo.append(CsCo[8])
		csv_CsCo[k].insert(0, Dopant[8])
		k = k + 1
	if values[9][1] == 1:
		plt.semilogy(x,CsCo[9], label = custom_name)
		csv_CsCo.append(CsCo[9])
		csv_CsCo[k].insert(0, custom_name)
		k = k + 1

	if(k > 0):
		csv_VsVo.append(x)
		ax = plt.gca()
		plt.tick_params(axis='y', which='minor')
		plt.ylabel('Cs/Co')
		plt.xlabel('Vs/Vo')
		ax.set_title('Doping Concentration vs Fraction Solidfied')
		plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5)
		plt.tight_layout()
		plt.grid()
		plt.show()

def save_data_fz():
	for i in csv_VsVo:
		i.insert(0, "Fraction Solidfied-->")
		filename = "Doping Concentration vs Fraction Solidfied_FZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_VsVo)
			csvwriter.writerows(csv_CsCo)

	csv_VsVo.clear()
	csv_CsCo.clear()

def conc_impurities_solid_fz():
	global ent1 
	global ent2

	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	lbl1 = Label(frame_mid_section, text="Select the dopant for which Cs/Co vs Fraction of Melt Solidified graph is to be plotted (atleast one)\n")
	lbl1['font'] = font2
	lbl1.pack()

	for i in Dopant:
		var = IntVar()
		c = Checkbutton(frame_mid_section, text = i, variable = var, font = font2).pack(anchor = W, padx=20)
		data[i] = var

	ent1 = Entry(frame_mid_section, text="")
	ent1.pack(anchor = W, padx=30)
	ent1.insert(0,"Enter Name")
	ent2 = Entry(frame_mid_section, text="")
	ent2.pack(anchor = W, padx=30)
	ent2.insert(0, 1)

	mybutton1 = Button(frame_mid_section, text="Plot", command = plot_CsCo_fz, width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton2 = Button(frame_mid_section, text="Back", command = fz_window, width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton3 = Button(frame_mid_section, text="Save Data", command = save_data_fz, width = 10, relief="raised",borderwidth = 3).pack(pady=10)

def zone_length_calc(answer):
	s = float(ent1.get())         
	d = float(ent2.get())

	values = []
	values.append(s)
	values.append(d)

	s = 10*s                 # N/m = kg m s-2 / m = 10 * g m s-2 / cm
	sq = s/(d*g_acc)
	zone_length = 2.84*math.sqrt(sq)

	values.append(zone_length)

	csv_values.clear()	
	csv_values.append(values)
	
	answer.set(round(zone_length,3))

def save_data_zl():
	for i in csv_values:
		csv_column.clear()
		csv_column.append("Surface Tension of the Melt (N/m): ")
		csv_column.append("Density of the Melt (g/cm^3): ")
		csv_column.append("Maximum Zone Length (cm): ")
		
		csv_header.clear()
		csv_header.append(csv_column)

		csv_body_zl.append(csv_values[0])
	
		filename = "Maximum Zone Length_FZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_header)
			csvwriter.writerows(csv_body_zl)

	csv_values.clear()

def max_zone_length():
	root.geometry("500x400")
	for widget in frame_mid_section.winfo_children():
		widget.destroy()
	
	global ent1, ent2
	
	lbl1 = Label(frame_mid_section, text="Maximum Zone Length \n")
	lbl1['font'] = font1
	lbl2 = Label(frame_mid_section, text="Enter surface tension of the melt (N/m)")
	lbl3 = Label(frame_mid_section, text="Enter density of the melt (g/cm^3)")
	lbl4 = Label(frame_mid_section, text="Maximum Zone Length (cm)")

	lbl2['font'] = font2
	lbl3['font'] = font2
	lbl4['font'] = font2

	ent1 = Entry(frame_mid_section, text="")
	ent2 = Entry(frame_mid_section, text="")

	answer = IntVar()
	mybutton3 = Button(frame_mid_section, text="Enter", command = lambda: zone_length_calc(answer), width = 10, relief="raised",borderwidth = 3)
	mybutton4 = Button(frame_mid_section, text="Back", command = fz_window, width = 10, relief="raised",borderwidth = 3)
	mybutton5 = Button(frame_mid_section, text="Save Data", command = save_data_zl, width = 10, relief="raised",borderwidth = 3)

	lbl5 = Label(frame_mid_section, textvariable=answer)
	lbl5['font'] = font2

	lbl1.grid(row=0,column=0, columnspan=2)
	lbl2.grid(row=1,column=0)
	lbl3.grid(row=2,column=0)
	lbl4.grid(row=3,column=0)
	lbl5.grid(row=3,column=1)

	ent1.grid(row=1,column=1)
	ent2.grid(row=2,column=1)

	mybutton3.grid(row=5,column=1,pady=10)
	mybutton4.grid(row=6,column=1,pady=10)
	mybutton5.grid(row=7,column=1,pady=10)

def cool_rate_calc(answer):
	Pmelt = float(ent1.get())
	del_T = float(ent2.get())
	vp = float(ent3.get())

	values = []
	values.append(Pmelt)
	values.append(del_T)
	values.append(vp)
	
	cool_rate = (Pmelt*del_T*vp)/meting_temp_silicon

	values.append(cool_rate)
	
	csv_values.clear()	
	csv_values.append(values)
	
	answer.set(round(cool_rate,3))

def save_data_cr():
	for i in csv_values:
		csv_column.clear()
		csv_column.append("Fraction of Lamp Power at Melting Point (%)")
		csv_column.append("Temperature Gradient in Upper Part of the Crystal (K/mm)")
		csv_column.append("Pulling Rate (mm/hr)")
		csv_column.append("Maximum Cooling Rate (%/hr)")		
		
		csv_header.clear()
		csv_header.append(csv_column)

		csv_body_cr.append(csv_values[0])
	
		filename = "Maximum Cooling Rate_FZ.csv"
		with open(filename, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(csv_header)
			csvwriter.writerows(csv_body_cr)

	csv_values.clear()

def max_cool_rate():
	root.geometry("600x400")
	for widget in frame_mid_section.winfo_children():
		widget.destroy()
	
	global ent1, ent2, ent3
	
	lbl1 = Label(frame_mid_section, text="Maximum Cool Rate\n")
	lbl1['font'] = font1

	lbl2 = Label(frame_mid_section, text="Enter fraction of lamp power at the melting point (%): ")
	lbl3 = Label(frame_mid_section, text="Enter temperature gradient in upper part of the crystal (K/mm): ")
	lbl4 = Label(frame_mid_section, text="Enter pulling rate (mm/hr): ")
	lbl5 = Label(frame_mid_section, text="Maximum Cooling Rate (%/hr): ")

	lbl2['font'] = font2
	lbl3['font'] = font2
	lbl4['font'] = font2
	lbl5['font'] = font2

	ent1 = Entry(frame_mid_section, text="")
	ent2 = Entry(frame_mid_section, text="")
	ent3 = Entry(frame_mid_section, text="")

	answer = IntVar()
	mybutton3 = Button(frame_mid_section, text="Enter", command = lambda: cool_rate_calc(answer), width = 10, relief="raised",borderwidth = 3)
	mybutton4 = Button(frame_mid_section, text="Back", command = fz_window, width = 10, relief="raised",borderwidth = 3)
	mybutton5 = Button(frame_mid_section, text="Save Data", command = save_data_cr, width = 10, relief="raised",borderwidth = 3)

	lbl6 = Label(frame_mid_section, textvariable=answer)
	lbl6['font'] = font2

	lbl1.grid(row=0,column=0, columnspan=2)
	lbl2.grid(row=1,column=0)
	lbl3.grid(row=2,column=0)
	lbl4.grid(row=3,column=0)
	lbl5.grid(row=4,column=0)
	lbl6.grid(row=4,column=1)

	ent1.grid(row=1,column=1)
	ent2.grid(row=2,column=1)
	ent3.grid(row=3,column=1)

	mybutton3.grid(row=5,column=1,pady=10)
	mybutton4.grid(row=6,column=1,pady=10)
	mybutton5.grid(row=7,column=1,pady=10)

def equation_select(option):
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	if(option == 1):
		root.title(" Maximum Pull Rate")
		max_pull_rate()         # common as in CZ process
	if(option == 2):
		root.title(" Concentration Of Impurities In Solid Phase")
		conc_impurities_solid_fz()
	if(option == 3):
		root.title(" Maximum Zone Length")
		max_zone_length()
	if(option == 4):
		root.title(" Maximum Cooling Rate")
		max_cool_rate()
	
def fz_window():
	csv_values.clear()
	csv_VsVo.clear()
	csv_CsCo.clear()

	root.title(" Float Zone Process")
	root.geometry("600x600")
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	cz_lbl1 = Label(frame_mid_section, text = "Float Zone Process\n" , fg = 'red')
	cz_lbl1['font'] = font1
	cz_lbl1.pack(anchor = "n")

	cz_lbl2 = Label(frame_mid_section, text = "Select Appropriate Option", font = "Helvetica 10 bold")
	#cz_lbl2['font'] = font2
	cz_lbl2.pack(anchor = "w")
	r = IntVar()
	r.set("1")
	
	Radiobutton(frame_mid_section, text="Maximum Pull Rate", variable=r, value=1, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Concentration Of Impurities In Solid Phase", variable=r, value=2, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Maximum Zone Length", variable=r, value=3, font = font2).pack(anchor = W)
	Radiobutton(frame_mid_section, text="Maximum Cooling Rate", variable=r, value=4, font = font2).pack(anchor = W)
	
	mybutton1 = Button(frame_mid_section, text="Select", command = lambda: equation_select(r.get()), width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton2 = Button(frame_mid_section, text="Back", command = main_window, width = 10, relief="raised",borderwidth = 3).pack(pady=10)

	my_img = ImageTk.PhotoImage(Image.open("Images/Webp.net-resizeimage (1).jpg"))
	img_lbl = Label(frame_mid_section, image = my_img)
	img_lbl.image = my_img
	img_lbl.pack()

######################### First Window Display ###################################


def process_window():
	#mylabel = Label(root, text = clicked.get()).pack()
	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	if clicked_new.get() == "Czochralski Process":
		cz_window()
	elif clicked_new.get() == "Float Zone Process":
		fz_window()

def main_window():
	root.title(" Crystal Growth Simulator")
	root.geometry("500x300")

	for widget in frame_mid_section.winfo_children():
		widget.destroy()

	lbl1 = Label(frame_mid_section, text = "Crystal Growth Simulator", fg = 'red' )
	lbl1['font'] = font1
	lbl1.pack(anchor = "center")

	lbl2 = Label(frame_mid_section, text = "\n\nSelect The Crystal Growth Process", font = "Helvetica 10 bold")
	#lbl3 = Label(root, text = "Test").pack()
	#lbl2['font'] = font2
	lbl2.pack()

	global clicked_new
	clicked_new = StringVar()
	clicked_new.set(Crystal_Process[0])

	drop = OptionMenu(frame_mid_section, clicked_new, *Crystal_Process)
	drop.config(bg = "white", highlightcolor = "blue")
	drop['font'] = font2
	drop.pack()

	mybutton1 = Button(frame_mid_section, text="Next", command = process_window, width = 10, relief="raised",borderwidth = 3).pack(pady=10)
	mybutton2 = Button(frame_mid_section, text="Manual", command = manual, width = 10, relief="raised",borderwidth = 3).pack(pady=10)

main_window()


root.mainloop()
