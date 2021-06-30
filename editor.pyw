from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from io import open

ruta = '' #La utilizaremos para almacenar la ruta del fichero

#configuracion de funciones del menu

def nuevo():
	global ruta 
	mensaje.set('# Fichero Nuevo #')
	ruta = ''
	texto.delete(1.0, 'end')
	FileDialog.asksaveasfile(title='Nuevo fichero', mode='w', defaultextension='*.txt')


def abrir():
	global ruta
	mensaje.set('# Abrir Fichero #')
	ruta = FileDialog.askopenfilename(title='Abrir fichero', initialdir='C:', filetypes=(('fichero de texto','*.txt'),('img','*.jpg'),('img','*.png'),))
	if ruta != '':
		fichero = open(ruta, 'r')
		contenido = fichero.read()
		texto.delete(1.0, 'end')
		texto.insert('insert', contenido)
		fichero.close()
		root.title(ruta + ' - V-Edict')
		print(ruta)
			
def guardar():
	mensaje.set('# Guardar Fichero #')
	if ruta != '':
		contenido= texto.get( 1.0 , 'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set('# Fichero Guardado Correctamente #')
	else:
		guardarcomo()

def guardarcomo():
	global ruta
	mensaje.set('# Guardar Fichero Como #')
	fichero = FileDialog.asksaveasfile(title='Guardar como', mode='w', defaultextension='.txt')
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0, 'end-1c')
		fichero = open(ruta,'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set('# Fichero Guardado Correctamente #')
	else:
		mensaje.set('# Guardar Cancelado #')
		ruta = ''

def test():
	try:
		fichero = open('border.txt','w')

		color = ColorChooser.askcolor(title = 'Insira un color')
		cor= color[1]
		root.config(bg=f'{color[1]}')
		monitor.config(bg=f'{color[1]}')
		mensaje.set('# Color agregado con sucesso #')

		fichero.write(str(cor))
		fichero.close()
	
	except:
		mensaje.set('# Nenhum color agregado #')


def textpantalla():
	try:	
		fichero = open('textpantalla.txt','w')
		
		color = ColorChooser.askcolor(title = 'Insira un color')
		cor= color[1]
		texto.config(bg=f'{color[1]}')
		
		mensaje.set('# Color agregado con sucesso #')
		fichero.write(str(cor))
		fichero.close()
		
	except:
		mensaje.set('# Nenhum color agregado #')


		
		
def menucolor():
	try:
		fichero = open('color1.txt', 'w')
		
		color = ColorChooser.askcolor(title = 'Insira un color')
		cor= color[1]
		colormenu.config(bg=f'{color[1]}')
		filemenu.config(bg=f'{color[1]}')
		menubar.config(bg=f'{color[1]}')
		mensaje.set('# Color agregado con sucesso #')

		fichero.write(str(cor))
		fichero.close()
	except:
		mensaje.set('# Nenhum color agregado #')

	
	

def fonttexto():
	try:
		fichero = open('fonttexto.txt', 'w')

		color = ColorChooser.askcolor(title= 'Insira un color')
		cor= color[1]
		texto.config(fg=f'{color[1]}')
		mensaje.set('# Color agregada con sucesso#')

		fichero.write(str(cor))
		fichero.close()

	except: 
		mensaje.set('# Nenhum color agregado #')



def fontmenu():
	try:
		fichero =  open('fontmenu.txt', 'w')

		color = ColorChooser.askcolor(title= 'Insira un color')
		cor= color[1]
		menubar.config(fg=f'{color[1]}')
		filemenu.config(fg=f'{color[1]}')
		colormenu.config(fg=f'{color[1]}')
		mensaje.set('# Color agregada con sucesso #')

		fichero.write(str(cor))
		fichero.close()
		
	except:
		mensaje.set('# Nenhum color agregado #')


def fontmonitor():
	try:
		fichero = open('fontmonitor.txt', 'w')

		color = ColorChooser.askcolor(title= 'Insira un color')
		cor= color[1]
		mensaje.set('# Color agregada con sucesso #')
		monitor.config(fg=f'{color[1]}')

		fichero.write(str(cor))
		fichero.close()
	except:
		mensaje.set('# Nenhum color agregado #')
def coressalvas():
	#	MENU COLOR:
	fichero = open('color1.txt', 'r')
	cormenu =  fichero.read()
	fichero.close()

	# TEXTO FONT COLOR:
	fichero = open('fonttexto.txt', 'r')
	corfonttexto = fichero.read()
	fichero.close()

	#	FONT MENU:
	fichero = open('fontmenu.txt', 'r')
	fontmenu = fichero.read()
	fichero.close()

	#	 FONT MONITOR:
	fichero = open('fontmonitor.txt', 'r')
	fontmonitor = fichero.read()
	fichero.close()
	#	FONT TEXTO PANTALLA:
	fichero = open('textpantalla.txt','r')
	textpantalla = fichero.read()
	fichero.close()

	#	BORDER: ROOT.CONFIG() Y MONITOR.CONFIG()
	fichero =  open('border.txt', 'r')
	bordercolor =  fichero.read()
	fichero.close()

		
	root.config(bg=f'{bordercolor}')
	monitor.config(bg=f'{bordercolor}', fg =f'{fontmonitor}')
	menubar.config(bg=f'{cormenu}', fg = f'{fontmenu}')
	filemenu.config(bg=f'{cormenu}', fg = f'{fontmenu}')
	colormenu.config(bg=f'{cormenu}', fg = f'{fontmenu}')
	texto.config(bg=f'{textpantalla}', fg =f'{corfonttexto}' )






root = Tk()
#configuraciones de la raiz 

root.title('V-Edict')
root.config(bd= 30)





#Menu superior....
menubar = Menu (root)
root.config(menu = menubar)


#FILEMENU
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command= nuevo)
filemenu.add_command(label='Abrir', command= abrir)
filemenu.add_command(label='Guardar', command= guardar)
filemenu.add_command(label='Guardar como', command= guardarcomo)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)

#COLORMENU
colormenu = Menu(menubar, tearoff=0)
colormenu.add_command(label='Color Border', command=test)
colormenu.add_command(label='Color Texto Pantalla', command=textpantalla)
colormenu.add_command(label='Menu Color', command= menucolor)
colormenu.add_separator()
colormenu.add_command(label='Texto Font Color', command = fonttexto)
colormenu.add_command(label='Menu Font Color', command = fontmenu)
colormenu.add_command(label='Monitor Font Color', command = fontmonitor)

menubar.add_cascade(menu= colormenu, label= 'Menu Color')



menubar.add_cascade(menu= filemenu, label='Archivo')


#caja de texto central

texto= Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd='20', font=('Consolas',12))


#Monitor 
mensaje = StringVar()
mensaje.set('#Bien Venido al editor de texto#')
monitor = Label(root, textvar=mensaje, justify= 'left')
monitor.pack(side='left')
monitor.config(font=('Retro Computer',9))

Button(root, text='Interface do Usuario', command=coressalvas).pack(anchor='e')












root.mainloop()