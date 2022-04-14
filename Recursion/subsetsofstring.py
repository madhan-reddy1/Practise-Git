def Generate_Subsets(word,index,curr_string):
	if index==len(word):
		print(curr_string)
		return 

	Generate_Subsets(word,index+1,curr_string+word[index]);
	Generate_Subsets(word,index+1,curr_string)



Generate_Subsets("abc",0,"")
