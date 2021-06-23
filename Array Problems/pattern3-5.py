# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
def pattern3(n):
	for i in range(n):
		for j in range(i+1):
			print(n-i,end=" ")
		print()

# pattern3(5)

# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1 

def pattern4(n):
	for i in range(n):
		for j in range(i+1):
			print(n-j,end=" ")
		print()
# pattern4(5)

# 5 
# 4 5 
# 3 4 5 
# 2 3 4 5 
# 1 2 3 4 5 

def pattern5(n):
	for i in range(n):
		for j in range(i,-1,-1):
			print(n-j,end=" ")
		print()

pattern5(5)