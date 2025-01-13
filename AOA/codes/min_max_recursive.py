# Recursive Python 3 program to 
# find maximum 

# function to return maximum element 
# using recursion 
def findMaxRec(A, n): 

	# if n = 0 means whole array 
	# has been traversed 
	if (n == 1): 
		return A[0] 
	return max(A[n - 1], findMaxRec(A, n - 1)) 

# Driver Code 
if __name__ == "__main__": 
	
	A = [1, 4, 45, 6, -50, 10, 2] 
	n = len(A) 
	print(findMaxRec(A, n)) 

# This code is contributed by ita_c 

