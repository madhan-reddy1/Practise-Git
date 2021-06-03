#CSES1
# You are given all numbers between 1,2,…,n except one.
# Your task is to find the missing number.
n=int(input())
array = [int(num) for num in input().split()]
# while i<=n:
# 	if i in array:
# 		i=i+1
# 	else:
# 		print(i)
# 		break
out=(n*(n+1))//2-sum(array)
print(out)	