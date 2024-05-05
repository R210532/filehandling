import csv
a=open("cl.txt","r")
b=a.readline()
c=open("t.csv","w")
writer=csv.writer(c)
writer.writerow(b)
