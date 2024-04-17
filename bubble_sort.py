def bubblesort(numbers):
    n = len(numbers)

    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    print(numbers)
