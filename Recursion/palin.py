def recur_palindrome(text,start,end):
	if start>=end:
		return True

	return (text[start]==text[end]) and recur_palindrome(text,start+1,end-1)



text= "sai"
print(recur_palindrome(text,0,len(text)-1))