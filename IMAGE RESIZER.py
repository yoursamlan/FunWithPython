#IMAGE RESIZER
#version 0.1
#by Amlan Saha Kundu

#FunWithPython --- Day 0, Hour 1.

#==========================================================================================================================================================================================


from scipy.misc import *
from imageio import *
import skimage
from skimage import *

#Welcome User :)
print('Enter your name :')
user = input()
print('Hi '+ user + ' ! \n')
print('Welcome to IMAGE RESIZER v0.1')

#input the file location

print('Please ENTER the input file location below')
print('Remember USE FORWARD SLASH (/) instead of backslash (\\) while entering the file location.')
print('eg: C:/Users/ABC/Pictures/xyz.jpg')
print('Input your image location here :')
loc = input()

#reading the image...

img = imread(str(loc))
print (img.dtype, img.shape)

#Enter parameter:

print('Enter Height (px):')
h = input()
print('Enter Width (px):')
w = input()

#Enter output location:
print('Please ENTER the output file location along its name below')
print('Remember USE FORWARD SLASH (/) instead of backslash (\\) while entering the file location.')
print('eg: C:/Users/ABC/Pictures/xyz_resized.jpg')
print('Enter your Output image location here :')
loco = input()

#Resizing the image...
res_img = skimage.transform.resize(img, (int(h),int(w)))

#Save the output file:
imsave(str(loco),res_img)



