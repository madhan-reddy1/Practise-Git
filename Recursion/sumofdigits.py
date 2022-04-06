def sumofdidgits(num):
	if num<=9:
		return num
	return num%10+sumofdidgits(num//10)


print(sumofdidgits(134))