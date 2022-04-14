def Towers_of_Hanoi(num,A,B,C):
	if num==1:
		print("Move 1 from "+A+" to "+C)
		return
	Towers_of_Hanoi(num-1,A,C,B)
	print("Move "+str(num)+" from "+A+" to "+C);
	Towers_of_Hanoi(num-1,B,A,C)


Towers_of_Hanoi(3,"A","B","C")
