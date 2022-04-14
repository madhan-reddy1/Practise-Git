def susbet_sum_count(arr,n,target):
	if n==0:
		return 1 if target==0 else 0
	return susbet_sum_count(arr,n-1,target)+susbet_sum_count(arr,n-1,target-arr[n-1])


arr=[2,6,5,3,8,7,1,1]
target=8
print(susbet_sum_count(arr,len(arr),target))