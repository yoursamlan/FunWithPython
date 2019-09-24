
#USER INPUT---------------------------------------------
name = input ("Enter your name : ")
sex = input ("Sex [Type m for Male or f for Female] : ")
dept = input ("Enter your department : ")
reg = input ("Enter your Regn. No.: ")
year = input ("Year of Exam : ")
print("Enter your marks below : ")
m1 = input ("Maths 1 : ")
m2 = input ("Maths 2 : ")
p  = input ("Physics : ")
c  = input ("Chemistry  : ")

#Calculation--------------------------------------------
if sex == 'm':
    sal = "Mr. "
elif sex == 'f':
    sal = "Ms. "
else:
    print("Please enter your sex properly.")
#----------------------------------------------
hons = int(m1) + int(m2)
tot = int(hons)+int(p)+int(c)
hons_per = int(hons) / 2
#----------------------------------------------

if int(hons) >= 70:
    verd = " H"
else:
    verd = " F"
#-----------------------------------------------
if int(m1) >= 35:
    verdm1 = " H"
else:
    verdm1 = " P"

if int(m2) >= 35:
    verdm2 = " H"
else:
    verdm2 = " P"

if int(p) >= 30:
    verdp = " P"
else:
    verdp = " F"

if int(c) >= 30:
    verdc = " P"
else:
    verdc = " F"

#-----------------------------------------------
'''
if int(hons_per) >= 60  :
    cls = " First"
elif int(hons_per) < 60 & int(hons_per) >= 40:
    cls = " Second"
elif int(hons_per) < 40 & int(hons_per) >= 35:
    cls = " Third"
else:
    cls = "Fail"
    
'''

#Output-------------------------------------------------
print("\n\n\n\n\n"+"=*"*30+"\n"+"=*"*30)
print("\n\n\t\t UNIVERSITY OF CALCUTTA\n\n")
print("\t\t  Marksheet cum Result\n\n\n\n")
print("\t Name of the student : "+sal+name)
print("\t          Discipline : "+dept+" Hons.")
print("\t    Registration No. : "+reg+"\n\n")
print("\t     Result for year : "+year+"\n\n")
print("   SUBJECT                 MARKS OBTAINED \t GRADE ")
print("-"*55+"\n")
print("MATHEMATICS - 1\t\t\t"+m1+" \t \t"+verdm1)
print("MATHEMATICS - 2\t\t\t"+m2+" \t \t"+verdm2)
print("PHYSICS        \t\t\t"+p+" \t \t"+verdp)
print("CHEMISTRY      \t\t\t"+c+" \t \t"+verdc)
print("\n"+"-"*55+"\n\n")
print("\tObtained marks  (H) : "+str(hons)+" / 200")
print("\tObtained marks  (T) : "+str(tot)+" / 400")
print("\t    percentage  (H) : "+str(hons_per)+" %")
print("\t            Verdict : "+str(verd))
#print("\t            Division: "+cls  +"\n\n")
print("\n\n\n\n\n"+"=*"*30+"\n"+"=*"*30)




