
import matplotlib.pyplot as plt
file = open("found.txt","r")
string=file.readlines()
length= len(string)
test_data=int(0.8*length) #finding data of 80% values
x=y=xy=x_square=y_square=Merror=0
for i in range(test_data):
	e= string[i].split(';')
	x+= float(e[1]) #sum of all values of x
	x_square+=float(e[1])**2
	y+= float(e[2]) #sum of all values of y
	y_square+= float(e[2])**2
	xy+= float(e[1])*float(e[2])

a=(test_data*xy-x*y)/(test_data*x_square-x**2) #formula to find a
b = (y-a*x)/test_data #formula to find b
d=1
c = ((test_data*xy-x*y)/((test_data*x_square-(x**2))*(test_data*y_square-(y**2)))**0.5)
print("value of a is ", a)
print("value of b is", b)
print("coorelation coefficient is", c)
for i in range(test_data,length):
	e= string[i].split(';')
	y= a*float(e[1])+b
	Merror += (y-float(e[2]))**2
	#using formula y=ax+b
print("Regression line: " "y = ",a,"x +" , b )
print("error between predicted and actual impact factor is " ,Merror/(length-test_data))

#2nd part

file2 = open("pns2.csv", "r")
import csv
reader = csv.reader(file2,delimiter=";")
fields =['NAME','H INDEX','IMPACT FACTOR']
rows =[]
columns=[]
i = 0
for line in reader:
	if(i>0):
		k =[]
		typee=a*(float(line[7]))+b
		k.append(line[2])
		b=b
		k.append(str(line[7]))
		
		k.append(str(typee))
		rows.append(k)
	i+=1
file3 = "confrence_final.csv"
with open(file3, 'w') as csvfile: 
	csvwriter = csv.writer(csvfile) 
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)