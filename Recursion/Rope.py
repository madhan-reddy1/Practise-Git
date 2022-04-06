def max_pieces(num,a,b,c):
	if num==0:
		return 0
	if num<0:
		returmn -1
	res= max(
			max_pieces(num-a,b,c),
			max_pieces(a,num-b,c),
			max_pieces(a,b,num-c))

	if res==-1:
		return -1

	return res	