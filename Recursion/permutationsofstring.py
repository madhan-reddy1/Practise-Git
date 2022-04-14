def permute(string,lstart,rend):
	if lstart==rend:
		print(''.join(string))
		return 
	for i in range(lstart,rend):
		string[lstart],string[i]=string[i],string[lstart]
		permute(string,lstart+1,rend)
		string[lstart],string[i]=string[i],string[lstart]


string="ABC"
n=len(string)
permute(list(string),0,n)