for i in range(1,100):
	n = i
	c =0
	a= False
	if n==1:
		a =True

	for j in range(1, n):
		if n % j == 0:
			c += 1
		if c > 1:

			a= True
			break
	if not a:
		print(i,"\t",end='')




