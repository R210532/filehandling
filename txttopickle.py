import pickle
a=open("test.txt","r")
b=a.readline()
c=open("create.pkl","wb")
pickle.dump(b,c)

