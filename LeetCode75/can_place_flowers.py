# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if len(flowerbed) == 0:
        return False
    if n == 0:
        return True
    if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0:
        return True
    planted = 0
    pointer = 0
    lastspot = len(flowerbed)-1
    result = False
    # Walk the array
    for spot in flowerbed:
        # Is it a plantable spot    
        if spot == 0:
            canPlant = False
            print('Found an open spot at index ' + str(pointer))
            
            if pointer == 0 and flowerbed[1] == 0:
                # It's the first spot, and next one is open
                print('This is the first spot, and next one is open')
                canPlant = True
            if pointer == lastspot and flowerbed[pointer-1] == 0:
                # It's the last spot, and the previous one is open
                print('This is the last spot, and the previous one is open')
                canPlant = True
            if not pointer == 0 and not pointer == lastspot and flowerbed[pointer-1] == 0 and flowerbed[pointer+1] == 0:
                # Then check if adjacent plots are also viable
                print('Adjacent spots are also open')
                canPlant = True
            if canPlant:    
                # Plant it (flip it), and increase total count
                print('Plant at spot ' + str(pointer))
                flowerbed[pointer] = 1
                # spot = 1
                planted += 1
                print('Planted ' + str(planted) + ' so far, need ' + str(n) + ' total' )
                if planted >= n: # Have we reached the target number, flip result to True
                    print('all done')
                    result = True
                    break;
        pointer += 1
    # Then try the next one

    return result

print(canPlaceFlowers(flowerbed=[1,0,0,0,0,1], n=2))
exit(0)
# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

print(canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1))

# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

print(canPlaceFlowers(flowerbed=[1,0,0,0,1], n=2))

print(canPlaceFlowers(flowerbed=[1,0,1,0,1], n=2))

print(canPlaceFlowers(flowerbed=[1,0,0,0,1,1,0,0,0,1], n=2))

print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,0,0,0,0,1], n=3))
print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,0,0,0,0,1], n=4))
print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,0,0,0,0,1], n=5))

print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,1,0,0,0,1], n=3))
print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,1,0,0,0,1], n=4))
print(canPlaceFlowers(flowerbed=[1,0,0,0,0,0,1,0,0,0,1], n=5))
