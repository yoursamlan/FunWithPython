#GOOGLE TRANSLATOR
#version 0.1
#by Amlan Saha Kundu
#FunWithPython --- Day 2, Hour 1.

#===================================================================================================================================================================================
import googletrans, sys
from googletrans import Translator

#Welcome User :) -------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('Enter your name :')
user = input()
print('\n Hi '+ user + ' ! \n')
print(' '+'='*33+'\n'+' Welcome to GOOGLE TRANSLATOR v0.1'+'\n'+' '+'='*33+'\n ')

#translator-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translator = Translator()
while True:
    print('\n Please enter the value you want to translate: ')
    val = input()
    print(' Please Enter your preffered Output Language (Default is "en"):')
    lan = input()
    if len(lan)==0:
        lan = 'en'
    print(' '+'='*33+'\n''Input: '+ str(val)+'\n')
    print('Prefered Output Language: '+str(lan)+'\n')
    translations = translator.translate( [str(val)], dest = str(lan))
    for translation in translations:
        print('Output :'+ str(translation.text)+'\n'+'='*33+'\n\n\n' )
        print('Do you want to translate again ?(Press y for "yes")')
        res = input()
        if res == 'y':
            continue
        else:
            sys.exit()
    
