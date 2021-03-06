#QR CODE GENERATOR
#version 1.2
#by Amlan Saha Kundu
#FunWithPython --- Day 1, Hour 3.

#===================================================================================================================================================================================

import pyqrcode, sys

#Welcome User :) -------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('Enter your name :')
user = input()
print('\n Hi '+ user + ' ! \n')
print(' '+'='*33+'\n'+' Welcome to QR Code Generator v1.2'+'\n'+' '+'='*33+'\n ')

#input value. ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\n Please enter the value, you want to save in QRcode :')
value = input()

#Color Option-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\n YOUR DEFAULT QR CODE COLOR IS BLACK & BACKGROUND COLOR IS WHITE. \n\n But you can change it  below. \n Press ENTER to skip changing and set back to defaults.\n')
colflag = 0;
while colflag != 1:
    print(' Enter the QR code color (in hex)(Do not use #)[Default is BLACK]:')
    qrcolor = input()
    if  ( len(qrcolor)==3 or len(qrcolor)==6 or len(qrcolor)==0):
        colflag = 1
    else:
        print(' Sorry the Color you have entered is not valid. Please enter it again.')
        colflag = 0
if len(qrcolor)==0:
    qrcolor = '000'
else:
    qrcolor = qrcolor
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
bgflag = 0;
while bgflag != 1:
    print(' Enter the background color (in hex)(Do not use #)[Default is WHITE]:')
    bgcolor = input()
    if  ( len(bgcolor)==3 or len(bgcolor)==6 or len(bgcolor)==0):
        bgflag = 1
    else:
        print(' Sorry the Color you have entered is not valid. Please enter it again.')
        bgflag = 0
if len(bgcolor)==0:
    bgcolor = 'fff'
else:
    bgcolor = bgcolor
#Size---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\n Default Size of the QR code is 10. \n But you can change it below. \n Press ENTER to skip changing and set back to defaults.')
size = input()
if len(size)== 0:
    size = 10

#Generate QR code.--------------------------------------------------------------------------------------------------------------------------------------------------------------------
qr = pyqrcode.create(str(value))

#Export QR code_______________________________________________________________________________________________________________________________________________________________________

#Output Path:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\n Please ENTER the output folder location below.')
print(' Remember USE FORWARD SLASH (/) instead of backslash (\\) while entering the file location.')
print(' eg: C:/Users/ABC/Pictures')
while True:
    print(' Enter your Output folder Path here :')
    fol = input()
    if len(fol)==0:
        print('PATH can not be empty. Please enter a valid folder path ,eg. C:/Users/ABC/Pictures')
        continue
    else:
        break

#Filename-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
print(' Your default file name is QR. \n Enter Your new file name below or press ENTER to keep it default.')
print(' Enter your File Name :')
fn = input()
if( len(fn) == 0):
    name = 'QR'
else:
    name = str(fn)

#Extension----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    print(' Please choose your preffered output format. \n      Enter 1 for PNG  \n      Enter 2 for SVG \n Enter your choice below :')
    mat = input()
    if (int(mat) == 1 or int(mat) == 2):
        break
    else:
        continue
    
#Generating Output-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
if int(mat)==1:
    dest = str(fol)+'/'+str(name)+'.png'
    qr.png(str(dest), scale = int(size), module_color = ('#'+str(qrcolor)) , background = ('#'+str(bgcolor)))
else:
    dest = str(fol)+'/'+str(name)+'.svg'
    qr.svg(str(dest), scale = int(size), module_color = ('#'+str(qrcolor)) , background = ('#'+str(bgcolor)))




        


      
