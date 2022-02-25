N = 1001
M = 1
while True:
	M += 1
	if M % 2 == 1:
		N -= M
	elif M % 2 == 0:
		N += M
	if N < 0:
		print(M-1)
		break
