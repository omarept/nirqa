d = {0:'---',1:'--x',2:'-w-',3:'-wx',4:'r--',5:'r-x',6:'rw-',7:'rwx'}

def chmodtest(f,p):
  l = list(str(p))
  print('{\'',f,'\':\'',sep='',end='')
  for j in l:

    for i in d:
        if i == int(j):
          print(d[i],end='')
  print('\'}')

chmodtest('test',777)