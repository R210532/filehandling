import csv
a=open("t.csv","r")
reader=csv.reader(a)
b=open("new.txt","w+")
for data in reader:
    b.write(str(data))

