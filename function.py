# how to write a function 

def multiplyTwo(ingredient):
# part1 --> def, the function name, input 
	
	# part 2 
	ingredient = ingredient * 2 

	# part 3 -- output 
	print(ingredient)

# calling the function 
# multiplyTwo(7)


# def evenOdd(number): 
# 	if number % 2 == 1: 
# 		print("ODD")
# 	if number % 2 == 0: 			# else:
# 		print("EVEN")

# evenOdd(3)

# Inside a function, use return instead of print 

def evenOdd(number): 
	if number % 2 == 1: 
		return("ODD")
	if number % 2 == 0: 			# else:
		return("EVEN")

# print(evenOdd(3))

##### print vs. return ##### 
# print shows the value in the output box 
# we use print when there is an error (to debug! to check the value!)
# print is for scanning ; return delivers the value 



# exercise 1
# given num of eggs, return num of cartons needed 
# 1 carton == 12 eggs 

def numOfCartons(eggs): 
	cartons = eggs // 12 		# quotient 
	if eggs % 12 != 0: 		# leftover NOT equal to 
		cartons = cartons + 1 
	return cartons 

print(numOfCartons(13)) 

# print(10 // 3)			 # whole number 
# print(10 / 3)			# exact value 
	

# return number of eggs needed to make it a full carton 	
def fullCarton(eggs): 
	# return 12 - eggs % 12 
	extraEggs = eggs % 12 
	full = 12 
	answer = full - extraEggs

	return answer 

# print(fullCarton(17))


# min, max 
print(max(10, 3, 9))
print(min(1, 2, 3))
# perimeter = s1 + s2 + s3

# define whether two shorter sides > longest side (legal triangle)
def legalTriangle(s1, s2, s3):
	# assume s1 is the longest side 
	if s1 > s2 and s1 > s3: 
		if s2 + s3 > s1: 
			return True 
		else: 
			return False 
	if s2 > s1 and s2 > s3: 
		if s1 + s3 > s2: 
			return True 
		else: 
			return False 
	else: 
		if s2 + s1 > s3: 
			return True 
		else: 
			return False 


if 10 > 3: 
	print(True)
else: 
	print(False)

# same thing...
print(10 > 3)



def legalTriangle2(s1, s2, s3):
	# assume s1 is the longest side 
	if s1 > s2 and s1 > s3: 
		return s2 + s3 > s1 
	if s2 > s1 and s2 > s3: 
		return s1 + s3 > s2
	else: 
		return s2 + s1 > s3 


def legalTriangle3(s1, s2, s3): 
	perimeter = s1 + s2 + s3 
	longestSide = max(s1, s2, s3)
	# perimeter - longestSide			# two shorter sides added 
	return longestSide < (perimeter - longestSide)







