import math

def selectOperator():
	print ()
	print ()
	print ("Select Operation or Formula")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("1 >> Addition")
	print ("2 >> Subtraction")
	print ("3 >> Multiplication")
	print ("4 >> Division")
	print ("5 >> Squared")
	print ("6 >> Square Root")
	print ("7 >> Circumference")
	print ("8 >> Binary Multiplication")
	print ("9 >> Fibonacci Sequence")
	print ("s >> Sieve of Eratosthenes")
	print ("q >> Quit")
	print ()

	return input()

def doError(errorMessage):
	print(errorMessage)

def getNum(promptString):
	print (promptString)
	return(int(input()))


def doDivision():
	number1 = getNum("Enter first number")
	number2 = getNum("Enter second number")
	if (number2 == "0"):
		doError("Can't divide by zero")
	else:
		answer = number1 / number2
		print (str(number1) + " / " + str(number2) + " = " + str(answer))

def sieveOfEratosthenes(max):
	#initialize primeList to include all integers from 1 to max
	primeList = [x for x in range(max) if x > 0]

	#the outer loop only needs to iterate index from 1 to sqrt(max)
	index = 1
	print(primeList)
	while(primeList[index] < math.sqrt(max)):
		#the inner loop removes every multiple of primeList[index] from primeList[]
		multiple = 2
		print("Removing all multiples of " + str(primeList[index]))
		while ((primeList[index] * multiple) < max):
			notPrime = primeList[index] * multiple
			if(notPrime in set(primeList)):
				primeList.remove(notPrime)
			multiple += 1
		print(primeList)
		index += 1
	print("Final all Prime List")
	print (primeList)

def fibonacciSequence(max):
	nMinus2 = 0
	nMinus1 = 1
	n = 0
	while(n <= int(max)):
		print(str(n))
		nMinus2 = nMinus1
		nMinus1 = n
		n = nMinus1 + nMinus2

def binaryMultiplication(x, y):
	ans = 0;
	while (x != 0):
		if (x&1):
			ans = ans + y
		x = x >> 1
		y = y << 1
	return (ans)

def calculator():
	while (1):
		operator = selectOperator()

		if (operator == 'q'):
			exit()

		if (operator == '1') or (operator == '+'):
			print ("Enter first number")
			number1 = input()
			print ("Enter second number")
			number2 = input()
			answer = int(number1) + int(number2)
			print (number1 + " + " + number2 + " = " + str(answer))


		if (operator == '7'):
			print ("Enter radius")
			radius = int(input())
			answer = radius * radius * math.pi
			print ("Circumference = " + str(answer))


		if (operator == '2') or (operator == '-'):
			print ("Enter first number")
			number1 = input()
			print ("Enter second number")
			number2 = input()
			answer = int(number1) - int(number2)
			print (number1 + " - " + number2 + " = " + str(answer))


		if (operator == '4') or (operator == '/'):
			doDivision()


		if (operator == '3') or (operator == '*'):
			print ("Enter first number")
			number1 = input()
			print ("Enter second number")
			number2 = input()
			answer = int(number1) * int(number2)
			print (number1 + " * " + number2 + " = " + str(answer))


		if (operator == '5'):
			print ("Enter first number")
			number1 = input()
			answer = int(number1)* int(number1)
			print (number1 + " * " + number1 + " = " + str(answer))


		if (operator == '6'):
			print ("Enter first number")
			number1 = input()
			answer = math.sqrt (int(number1))
			print (number1 + " sqrt " + number1 + " = " + str(answer))


		if (operator == '8'):
			print ("Enter first number")
			number1 = input()
			print ("Enter second number")
			number2 = input()
			print (number1 + " * " + number2 + " = " + str(binaryMultiplication(int(number1), int(number2))))


		if (operator == '9'):
			max = getNum("Enter max")
			fibonacciSequence(max)

		if (operator == 's'):
			max = getNum("Enter max") + 1
			sieveOfEratosthenes(max)

calculator()