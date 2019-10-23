#GITHUB CALENDER IN AMLAN VERSION
#AMLAN SAHA KUNDU
#Python program to draw color filled square in turtle programming
import turtle,random
#186a3b 1d8348 239b56 28b463 2ecc71 58d68d 82e0aa

col = ["ffffff","58d68d","2ecc71","28b463","239b56","1d8348","186a3b"]
n = int(input("Enter No. of Entry : "))
#side = input("Enter side Length : ")
#z = input("Enter Gap in between : ")
l = []
for c in range (n):
    d = c+1
    st = random.randint(0,12)
    l.append(st)

t = turtle.Turtle()
t.ht()
x=0
y=0
t.penup()

for j in range(1,n+1):
    k = int(l[j-1])
    if k == 0:
        q = 0
    elif k>=10:
        q=6
    else :
        q = k//2+1
    t.begin_fill()
    for i in range(4):
        t.pendown()
        t.fillcolor('#'+col[q])
        t.forward(15)
        t.right(90)
        t.penup()
    t.end_fill()
    if j%7==0:
        x += int(20)
        y = 0
        
    else:
        y -=int(20)
    t.goto(x,y)

