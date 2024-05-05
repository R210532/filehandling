
import pickle
a=open("t.pkl","rb")
b=pickle.load(a)
c=open("t2.txt","w")
c.write(b)
