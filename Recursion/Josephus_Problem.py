def Josephus(num,kill_num):
 	if num==1:
 		return 0
 	return (Josephus(num-1,kill_num)+kill_num)%num

def  Josephus_helper(num,kill_num):
	return Josephus(num,kill_num)+1

def Josephus2(num,kill_num):
	if num==1:
		return 0
	sum=0
	for i in range(2,num+1):
		sum=(sum+kill_num)%i
	return sum+1

num=10
kill_num=2
print(Josephus_helper(num,kill_num))
print(Josephus2(num,kill_num))