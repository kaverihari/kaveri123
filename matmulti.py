c1=input("enter columns for m1:")
r1=input("enter rows of m1:")
c2=input("enter columns form2:")
r2=input("enter rows for m2:")
m1={};
m2={};
if(c1==r2):
	a={};
	print("enter elements for a matrix")
	for i in range(0,r1):
		for j in range(0,c1):
			a[i,j]=int(input())
	b={};
	print("enter elements for b matrix")
	for i in range(0,r2):
		for j in range(0,c2):
			b[i,j]=int(input())
	r={}
	for i in range(0,r1):
		for j in range(0,c2):
			r[i,j]=0;
			for k in range(0,r2):
				r[i,j]=r[i,j]+a[i,k]*b[k,j]
	print("print mulltiplication")
	for i in range(0,r1):
		for j in range(0,c2):
			print(r[i,j])
else:
	print("muliplication is not possible")

		
  		
