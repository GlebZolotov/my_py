#!/usr/bin/env python3

print("Hello!")

w=input()

if w:
	try:
		n=int(w);
		
		x=[]
		for i in range(2, n):
			if n%i == 0: 
				while n%i == 0:
					print(i)
					x.append(i)
					n//=i
					
		print(x)			
	except ValueError as err:
		print(err, ":(");			

