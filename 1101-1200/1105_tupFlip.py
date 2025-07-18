def palindrome(r):
	end = len(r) -1
	start = 0
	while(start<end):
		if(r[start]!=r[end]):
			return False
		start+=1
		end-=1
	return True


r = (1,2,3,3,2,1)

if(palindrome(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")