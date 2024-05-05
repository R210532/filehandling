import pickle
import csv
a=open("t.pkl",'rb')
b=pickle.load(a)
c=open("t.csv","w")
writer=csv.writer(c)
writer.writerow(b)
