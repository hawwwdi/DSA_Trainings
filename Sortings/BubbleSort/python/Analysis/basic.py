import random

START = 0
STOP = 9999
max_num = 100
comparisons = 0
swaps = 0

def bubble_sort(numbers): 
	global comparisons
	global swaps
	n = len(numbers) 
	for i in range(n): 
		for j in range(0, n-i-1): 
			if numbers[j] > numbers[j+1] : 
				numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 
				swaps += 1
			comparisons += 1	

def numbers_generator():
    global max_num
    return [random.randint(START, STOP) for i in range(0, max_num)]


if( __name__=='__main__'):
    numbers = numbers_generator()
    print(" << ", end="")
    print(*numbers, sep="  ")
    bubble_sort(numbers)
    print(" >> ", end="")
    print(*numbers, sep="  ")
    print(f"Total comparisons of {max_num} numbers = {comparisons} times / with {swaps} swaps.")