import sys
from tkinter import *
import qrcode
from shutil import rmtree
import os
from PIL import Image, ImageTk

#Crear carpeta img
dirImg = "img"
try:
    os.mkdir(dirImg)
except OSError:
    print("La creación del directorio %s falló" % dirImg)
    rmtree("img/")
else:
    print("Se ha creado el directorio: %s" % dirImg)
    
##############

#QR DE ENTRADA EN CALOR
codigoQr= f'00000000000@LASTNAME@NAME@N@88888888@N@88/88/8888@00-00-0000'
#creacion de qr y formato
qr = qrcode.QRCode(version=1,box_size=10, border=5)
qr.add_data(codigoQr)
qr.make(fit=True)
#imagen qr y formato
img = qr.make_image(fill='black', back_color='white')
nombreImagen="TEST"
#guardar imagen qr
img.save(f"img/{nombreImagen}.png")

##############

app = Tk(className='QRcode')

app.title('QR')
app.geometry('732x504') #a 1024 se agrega la zona celeste(buscador)
app.iconphoto(True, PhotoImage(file="qrcode_icon.png"))
app.resizable(width=False, height=False)

##############

#QR (rojo)
qrCanvas = Canvas(height = 504, width = 440, background = '#ec7017')
qrCanvas.grid(row=0,column=1)

def generarQr():
    #variables
    dni = dniEntrada.get()
    apellido = apellidoEntrada.get() 
    nombre = nombreEntrada.get()
    nacimiento = nacimientoEntrada.get()
    #string del qr 
    codigoQr= f'00000000000@{apellido}@{nombre}@N@{dni}@N@{nacimiento}@00-00-0000'
    #creacion de qr y formato
    qr = qrcode.QRCode(version=1,box_size=10, border=5)
    qr.add_data(codigoQr)
    qr.make(fit=True)
    #imagen qr y formato
    img = qr.make_image(fill='black', back_color='white')
    nombreImagen=f"{apellido}_{nombre}"
    #guardar imagen qr
    img.save(f"img/{nombreImagen}.png")
    #renderizar imagen qr
    imgQr = Image.open(f"img/{nombreImagen}.png") #ImageTk.PhotoImage(
    resized_imageQr = imgQr.resize((344, 344), Image.ANTIALIAS)
    new_imageQr = ImageTk.PhotoImage(resized_imageQr)
    qrCanvas.create_image(220, 256, anchor='center', image=new_imageQr)
    def check():
        #label introduccion
        checkQr = Label(app, text=f"Qr de:", font=('monospace', 12, 'bold'), width=22, fg="#ec7017", bd=0, bg="#4e4e4e")
        checkQrW = formCanvas.create_window(146, 320, anchor="center", window=checkQr)
        #label nombre
        checkApellidoQr = Label(app, text=f"{apellido}", font=('monospace', 12, 'bold'), width=22, fg="#ec7017", bd=0, bg="#4e4e4e")
        checkApellidoQrW = formCanvas.create_window(146, 341, anchor="center", window=checkApellidoQr)
        #label apellido
        checkNombreQr = Label(app, text=f"{nombre}", font=('monospace', 12, 'bold'), width=22, fg="#ec7017", bd=0, bg="#4e4e4e")
        checkNombreQrW = formCanvas.create_window(146, 362, anchor="center", window=checkNombreQr)
    check()
##############

#FORMULARIO (negro)
formCanvas = Canvas(app, height = 504, width = 292, background = '#4b4a54')
formCanvas.grid(row=0,column=0)

#Entry's
#dni
dniLabel = Label(app, font=('monospace', 12, 'bold'), width=0, text='DNI', bd=0, foreground='#d2d1d0', background = '#4b4a54')
dniLabelW = formCanvas.create_window(178, 84, anchor='w', window=dniLabel)

dniEntrada = Entry(app, font=('monospace', 12, 'bold'), width=14, foreground='#33322f', bd=0, background='#d2d1d0')
dniW = formCanvas.create_window(88, 84, anchor="center", window=dniEntrada)

#apellido
apellidoLabel = Label(app, font=('monospace', 12, 'bold'), width=0, text='APELLIDO', bd=0, foreground='#d2d1d0', background = '#4b4a54')
apellidoLabelW = formCanvas.create_window(178, 126, anchor='w', window=apellidoLabel)

apellidoEntrada = Entry(app, font=('monospace', 12, 'bold'), width=14, foreground='#33322f', bd=0, background='#d2d1d0')
appelidoW = formCanvas.create_window(88, 126, anchor="center", window=apellidoEntrada)

#nombre
nombreLabel = Label(app, font=('monospace', 12, 'bold'), width=0, text='NOMBRE', bd=0, foreground='#d2d1d0', background = '#4b4a54')
nombreLabelW = formCanvas.create_window(178, 168, anchor='w', window=nombreLabel)

nombreEntrada = Entry(app, font=('monospace', 12, 'bold'), width=14, foreground='#33322f', bd=0, background='#d2d1d0')
nombreW = formCanvas.create_window(88, 168, anchor="center", window=nombreEntrada)

#nacimiento
nacimientoLabel = Label(app, font=('monospace', 12, 'bold'), width=0, text='NACIMIENTO', bd=0, foreground='#d2d1d0', background = '#4b4a54')
nacimientoLabelW = formCanvas.create_window(178, 210, anchor='w', window=nacimientoLabel)

nacimientoEntrada = Entry(app, font=('monospace', 12, 'bold'), width=14, foreground='#33322f', bd=0, background='#d2d1d0')
nacimientoW = formCanvas.create_window(88, 210, anchor="center", window=nacimientoEntrada)


#Button
#generadorQR
generadorQrBt = Button(app, text="Generar QR", font=('monospace', 12, 'bold'), width=14, fg="#33322f", bd=0, command=generarQr)
generadorQrBtW = formCanvas.create_window(146, 266, anchor="center", window=generadorQrBt)




##############

#BUSCADOR (celeste)
buscadorCanvas = Canvas(height = 504, width = 292, background = '#6897bb').grid(row=0,column=2)



##############

app = mainloop()

#Borrar carpeta img
try:
    rmtree("img/")
except OSError:
    print("No se pudo borrar el directorio %s falló" % dirImg)
else:
    print("Se ha boorado el directorio: %s " % dirImg)