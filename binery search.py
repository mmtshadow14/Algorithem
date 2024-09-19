
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

targetNum = int(input('please enter the num you are looking for: '))

rightIndex = int(len(numList))-1
leftIndex = 0

num = 0

while num != targetNum:

    midIndex = round((rightIndex+leftIndex)/2)

    if numList[midIndex] == targetNum :

        print(f'the {targetNum} is in index {midIndex} . ')
        num = numList[midIndex]

    elif numList[midIndex] < targetNum :

        leftIndex = midIndex

    else :

        rightIndex = midIndex

