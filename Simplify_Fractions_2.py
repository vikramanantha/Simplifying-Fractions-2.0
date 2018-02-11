#SIMPLIFY FRACTIONS 2.py by Vikram Anantha

def smplFrctns():
	factors = []
	num = ''
	den = ''
	ind = -1
	print("Hi! This is a Simplify fractions Calcultor.")
	frac = input("Type your fraction below. Make sure to use '/' to separate the numerator and the denominator. \n")
	numDen = frac.split("/")
	num = numDen[0]
	den = numDen[1]
	den = int(den)
	num = int(num)
	num1 = num+1
	den1=den+1
	for i in range(1, num1):
		if num % i == 0 and den % i == 0:
			factors.append(i)

	cn = max(factors)
	upDen = den/cn
	upNum = num/cn
	upNum = int(upNum)
	upDen = int(upDen)
	print("Your number is", upNum, "/", upDen)
	input()
	smplFrctns();

smplFrctns();
