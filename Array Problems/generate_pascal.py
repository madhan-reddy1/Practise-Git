def gennerate(n):
	outer_list1=[]
	for i in range(0,n):
		inner_list=[]
		for j in range(0,i+1):
			if j==0 or j==i:
				inner_list.append(1)
			else:
				inner_list.append(outer_list1[i-1][j-1]+outer_list1[i-1][j])
		outer_list1.append(inner_list)
	return outer_list1

print(gennerate(5))