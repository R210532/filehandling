import csv
with open("/home/rguktrkvalley/comma.csv","w") as f:
  f=csv.writer(f)
  f.writerow(['name','ID'])
  f.writerow(['sumithra','r210532'])
  f.writerow(['lavanya','r210001'])
with open("/home/rguktrkvalley/comma.csv","r") as f:
  f=csv.reader(f)
  for row in f:
    print(row)
  
  
