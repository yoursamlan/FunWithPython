#RANDOM NUMBER DATASET GENERATOR
#version 2.0
#by Amlan Saha Kundu
#FunWithPython --- Day 3, Hour 4.

#===================================================================================================================================================================================
import os, random, sys,time
from time import strftime

#Welcome User :) -------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('Enter your name :')
user = input()
print('\n Hi '+ user + ' ! \n')
print(' '+'='*50+'\n'+' Welcome to RANDOM NUMBER DATASET GENERATOR v2.0'+'\n'+' '+'='*50+'\n ')

#Input no. of data set want & size of each dataset----------------------------------------------------------------------------------------------------------------------------------
print('Number of Dataset you want to create :')
n = input()
print('Number of generated random integer in each DATASET:')
num = input()
print('Please input the range of generated random integer in each DATASET below.')
print('Enter the lower RANGE [DEFAULT is 0]:')
lran = input()
if len(lran) == 0:
    lran = 0
print('Enter the upper RANGE [DEFAULT is 9]:')
uran = input()
if len(uran) == 0:
    uran = 9
flag = 0
while True:
    print(' Choose whether each data is separated by " " or not ? ')
    print('\n Enter 1 to insert " " between each data.')
    print('\n Enter 2 for continuous data output.')
    print('\n Please Enter your choice below : ')
    choice = input()
    if choice == '1':
        flag = 1
        break
    elif choice == '2':
        flag = 2
        break
    else:
        flag = 0
        continue
print('Enter the path of your directory [DEFAULT is your current working directory]: ')
dirpath =  input()
if len(dirpath)==0:
    dirpath = str(os.getcwd())
print('Enter the name of dataset directory [DEFAULT is "GENERATED DATA(timestamp)"]: ')
dirname =  input()
timestamp = strftime("%d-%m-%Y , %H-%M")
if len(dirname)==0:
    dirname = 'GENERATED DATA on '+str(timestamp)+'  '+str(time.time())
print('Enter the name of your Datafile [Default is "DATASET[i]"]:')
fname = input()
if len(fname)==0:
      fname = 'DATASET'

      
path = str(dirpath)+'\\'+str(dirname) 
os.mkdir(path)
      
i = 0
while i< int(n):
    filename = str(fname)+str(int(i)+1)
    filepath = str(path)+'\\'+str(filename)+'.txt'
    f = open(str(filepath),"w")
    for x in range (0,int(num)):
        f.write(str(random.randint(int(lran),int(uran))))
        if flag == 1:
            f.write(' ')
    f.close()
    i+=1;

#METADATA CREATION-------------------------------------------------------------------------------------------------------------------------------------------------------------------

metadatapath = str(path)+'\\00. metadata.txt'
m = open(str(metadatapath), "w")
m.write('\n                          Path of the directory : '+str(dirpath))
m.write('\n                          Total no. of datasets : '+str(n))
m.write('\n No. of randomly generated data in each dataset : '+str(num))
m.write('\n      Lower range of randomly generated integer : '+str(lran)
m.write('\n      Upper range of randomly generated integer : '+str(uran)
m.write('\n            Decoded timestamp in directory name : '+str(time.ctime()))
m.write('\n                         Prefix of each dataset : '+str(fname))
m.write('\n   Randomly generated datasets are requested by : '+str(user)+'\n\n')
m.write('\n                      Datasets are generated by : RANDOM NUMBER DATASET GENERATOR')
m.write('\n                                        Version : 2.0')
m.write('\n                                     Created by : Amlan Saha Kundu')
m.close()

        

    


        

    
