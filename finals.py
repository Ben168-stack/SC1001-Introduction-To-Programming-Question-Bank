#N is number of words

#Write a function that takes the list of words, calculates the number of letters that only appear once in each
#E.g.Apple has 3 such letters 
#A L E (P appears twice and thus isn't counted)

#Return the word that has the highest number of letters that only appear once

#If multiple words have the same number of unique letters, return the one that appears first alphabetically 
#(Carrot and Pear both have 4 letters that only appear once.
#Output is Carrot because it appears first in the dictionary)

#ie list1 = [apple, banana, carrot, pear]

#listx = ['apple', 'banana', 'carrot', 'pear']

def numuniqueletters(x):
    count = {}
    for letter in x.lower():
        count[letter] = count.get(letter,0) + 1
    return sum(1 for numoccurrences in count.values() if numoccurrences == 1)

def maxunique(listx):
    best = -1
    bestword = None
    for words in listx:
        uniquecount = numuniqueletters(words) #yo idk anymore
        if uniquecount > best:
            best = uniquecount
            bestword = words
        elif uniquecount == best:
            if words.lower() < bestword.lower(): #alphabetically lower = smaller :D yipeyipyeypieypipie
                bestword = words
    return bestword

#print(maxunique(listx))

#You are given 2 lists. In list 1, Good Numbers are those that satisfy EITHER of these 2 criteria

#a)the number is a palindrome
#b)the digit 2 appears in the number EXACTLY once

#(5 is a palindrome, 12 contains the digit 2, 303 is a palindrome)
#(221 has 2 different 2's and isn't a palindrome, so it isn't a good number)

#Multiply all the Good numbers from list 1 with all the Odd numbers in list 2 and return the product

#(Only odd number in list 2 is 11)

#Output=5*12*303*11=199980

#If there are no Good Numbers in list 1 AND no odd numbers in list 2, 
# Return -1 instead

def ispalindrome(x):
    x = str(x)
    i = 0
    j = len(x)-1
    while i < (len(x)-1) * 0.5 and j > (len(x)-1) * 0.5:
        if x[i] == x[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True

#ok or a shorter (but slower) code is if x == x[::-1] ie if x is same as reversed x then it is a palindrome.

def onetwo(x):
    return str(x).count('2') == 1

def good1(list1):
    res = []
    for number in list1:
        if ispalindrome(str(number)) or onetwo(str(number)):
            res.append(number)
    return res

def good2(list2):
    res2 = []
    for number in list2:
        if number % 2 == 1:
            res2.append(number)
    return res2

def ohmygod(res, res2):
    result = 1
    for i in res:
        result *= i
    for j in res2:
        result *= j
    return result

#list1 = [303, 5, 12, 3003, 13569]

#list2 = [11, 23, 24]

#res = good1(list1)
#res2 = good2(list2)

#print(res)
#print(res2)
#print(ohmygod(res, res2))
#print(303*5*12*11*23*3003)

#Input: a list of words.
#For each word, count how many vowels (a, e, i, o, u) appear exactly once.
#Return the word with the highest count.
#If tied, return the shortest word.

def countvowels(word):
    vowels = 'aeiou'
    res = 0
    for letter in vowels:
        if word.count(letter) == 1:
            res += 1
    return res

def highest(list1):
    bestword = None
    bestcount = 0
    for word in list1:
        count =  countvowels(word)
        if count > bestcount:
            bestword = word
            bestcount = count
        elif count == bestcount:
            if len(word) < len(bestword):
                bestcount = count
                bestword = word
    return bestword

#list1 = ['a','ae','aeiou','aaee','ppp','aaeeiioouu']
#print(highest(list1))

#Input: a list of integers.
#For each number, calculate the sum of its digits.
#Return the first number whose digit-sum is prime.
#If none exist, return -1.

def checkprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True 
    elif n%2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
    return True
        
def idek(leest):
    for integer in leest:
        sum = 0
        for number in str(integer):
            sum += int(number)
        if checkprime(sum):
            return integer
    return -1

list1 = [10, 22, 35, 99, 101, 123, 88, 41, 77, 56]
#print(idek(list1))

#Input:
#A dictionary like:
#{"Apple": 5, "Banana": 8, "Carrot": 10, "Berry": 4}
#Return the sum of values whose keys start with 'A' or 'B'.

#holy shit im so unfamiliar with dictionaries lmfao

def istilldk(dick):
    sum = 0
    for key in dick:
        kay = key.lower()
        if kay[0] == 'a'  or kay[0]== 'b':
            sum += dick.get(key)
    return sum

#deeck = {"Apple": 5, "Banana": 8, "Carrot": 10, "Berry": 4}
#print(istilldk(deeck))

#Write a function that takes a string and returns a dictionary mapping each character to the 
#number of times it appears, ignoring case.

def abcd(st):
    st = st.lower()
    res = {}
    for char in st:
        if char not in res:
            res[char] = 1
        elif char in res:
            res[char] += 1
    return res

#print(abcd("baNAnA"))

#Given a dictionary where values may repeat, return a list of all keys that have a given value.

def abcde(dick, value):
    res = []
    for key in dick:
        if dick[key] == value:
            res.append(key)
    return res

#d = {'a':2, 'b':3, 'c':2, 'd':5}

#print(abcde(d, 2))

#Given a dictionary, return a new dictionary with keys and values swapped.
#If two keys share the same value, store the keys in a list.

def swapvk(dick):
    res = {}
    for key, value in dick.items():
        if value not in res:
            res[value] = [key]
        else:
            res[value].append(key)
    return res

#d = {"a": 1, "b": 2, "c": 1}
#print(swapvk(d))

#wowowowow moving on!!!!!!!!!!!
#Given two dictionaries, combine them by adding values of matching keys.
#d1 = {'apple': 3, 'banana': 1}
#d2 = {'apple': 2, 'carrot': 5}

def mergedict(d1, d2):
    res = {}
    for key, value in d1.items():
        if key not in d2:
            res[key] = value
        elif key in d2:
            res[key] = value + d2[key]
    for key, value in d2.items():
        if key not in res:
            res[key] = value
    return res

#print(mergedict(d1,d2))

#Given a list of words, return the word that appears most frequently.
#If tied, return the alphabetically earliest.

def slaydiva(liste):
    wordfreq = {}
    for words in liste:
        wordfreq[words] = wordfreq.get(words, 0) + 1
    maxvalue = max(wordfreq.values())
    freqword = None
    for words in wordfreq:
        if wordfreq[words] == maxvalue:
            if freqword == None or words < freqword:
                freqword = words
    return freqword

#test = ["banana", "apple", "cat", "banana", "dog", "apple", "carrot","banana", "apple"]
#print(slaydiva(test))

#Given a list of words, group them into lists of anagrams.

#test = ["eat","tea","ate","bat","tab"]
def anagrams(lit):
    res = {}
    for word in lit:
        sorte = ''.join(sorted(word))
        if sorte not in res:
            res[sorte] = [word]
        else:
            res[sorte].append(word)
    return res

#print(anagrams(test))

#You get two dictionaries: stock (item → quantity), order (item → quantity wanted)
#Return a dictionary of:
#items successfully purchased
#items insufficient (available stock < ordered)

#Example:
stock = {'potion': 5, 'elixir': 1, 'bomb': 0}
order = {'potion': 3, 'bomb': 1, 'elixir': 2}

def potionshop(stock, order):
    purchased = {}
    insufficient = {}
    for key in stock:
        stork = stock[key]
        orde = order[key]
        if stork < orde:
            insufficient[key] = orde - stork
        elif stork >= orde:
            purchased[key] = orde
    return purchased, insufficient

#print(potionshop(stock, order))

#i mean def this is like shit for actual game implementatoin cuz i didnt add
#the part where stock changes when you purchase but oh well...

# sort

#Write a function that uses bubble sort to sort a list of integers in ascending order.
def bubblesort(lits):
    for _ in range(len(lits)):
        for i in range(len(lits)-1):
            if lits[i] > lits[i + 1]:
                temp = lits[i+1]
                lits[i+1] = lits[i]
                lits[i] = temp
    return lits

#lits = [6, 5, 4, 3, 2, 1]
#print(bubblesort(lits))

#Given a list and a target number, implement binary search and return:

def binarysearch(leest, target):
    leest = sorted(leest)
    for i in range(len(leest)):
        if leest[i] == target:
            return i
    return -1

#test1 = [1, 3, 5, 7, 9]

#print(binarysearch(test1, 7))
#print(binarysearch(test1, 6))

#Using linear search only, count how many times a target number appears in a list.
#lowkey still need to consider edge cases like empty list but lets ignore that lol

def linearocc(lis, target):
    count = 0
    for i in range(len(lis)):
        if lis[i] == target:
            count += 1
    return count

#lis = [0, 0, 3, 0, 5, 5, 6, 7 ,0]

#print(linearocc(lis, 0))


#Modify bubble sort so the output is sorted from largest → smallest.

def bubblesortupsidedown(lits):
    for _ in range(len(lits)-1):
        for i in range(len(lits)-1):
            if lits[i] > lits[i + 1]:
                temp = lits[i+1]
                lits[i+1] = lits[i]
                lits[i] = temp
    sortlits = lits[::-1]
    return sortlits

#lits = [6, 5, 4, 3, 2, 1]
#print(bubblesortupsidedown(lits))

#Given a sorted list and a target, return the index where the target should be 
#inserted to keep the list sorted.

def insertarg(lis, target):
    for i in range(len(lis)):
        if lis[i] >= target:
            lis.insert(i, target)
            return lis
    lis.append(target)
    return lis

#lis = [5, 10, 20]
#print(insertarg(lis, 3))

#Modify bubble sort to return how many swaps were performed during sorting.

def bubblesortcount(lits):
    swap = 0
    for _ in range(len(lits)):
        for i in range(len(lits)-1):
            if lits[i] > lits[i + 1]:
                temp = lits[i+1]
                lits[i+1] = lits[i]
                lits[i] = temp
                swap += 1
    return lits, swap

#lits = [6, 5, 4, 3, 2, 1]
#print(bubblesortcount(lits))

# i thk can optimise bub sort by stopping when list is sorted

def bubblesortopt(lits):
    swap = 0
    swapped = False
    for _ in range(len(lits)):
        for i in range(len(lits)-1):
            if lits[i] > lits[i + 1]:
                temp = lits[i+1]
                lits[i+1] = lits[i]
                lits[i] = temp
                swap += 1
                swapped = True
        if not swapped:
            break
    return lits, swap


#Write your own recursive merge sort that returns a new sorted list.

def merge(left, right):
    #2 lists
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


def mergesort(list):
    if len(list) == 1:
        return list
    
    mid = len(list)//2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])

    return merge(left, right)

#print(mergesort([5, 1, 4, 2, 8, 3]))

#retry merge sort ugh
#13. Merge Sort — Count Inversions
#An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
#Modify merge sort to count how many inversions are in the list.
#Example: [3,1,2] → 2 inversions (3 >1, 3>2)

def merge2(left, right): #comparison of left and right lists
    res = []
    i, j, inversion= 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            inversion += len(left) - i
            j += 1
    
    res.extend(left[i:])
    res.extend(right[j:])

    return res, inversion

def mergesort2(list):
    if len(list) == 1:
        return list, 0
    
    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge2(left, right)

#print(mergesort2([5, 1, 4, 2, 8, 3, 6, 7, 0, 23, 324]))

#Given a sorted list where numbers may repeat, return the index of the last occurrence of the target.

def lastocc(list, target):
    for i in range(len(list)):
        if list[i] == target:
            if list[i+1] != target:
                return i
    return -1

test = [1,2,2,2,3]

#print(lastocc(test, 2))

#Without sorting the entire list, merge two already-sorted lists into one sorted list.
#MAJULAHHHHHHHHHHHHHHHHHHHHHHHHHh
def merger(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
        else:
            res.append(l2[j])
    res.extend(l1[i:])
    res.extend(l2[j:])

    return res


#Search in a Rotated Sorted Array (Binary Search Logic) Example:

nums = [5,6,7,1,2,3,4]
#target = 3 → index = 5
#You must modify binary search to handle the rotation.

def rotbin(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return arr[mid]
        
        if arr[left] <= arr[mid]: #if left half is sorted...
            if arr[left] <= target < arr[mid]: #target in left
                right = mid - 1
            else: #target in right
                left = mid + 1
        
        else: #if right half is sorted
            if arr[mid] < target <= arr[right]: #target in right
                left = mid + 1 #search right
            else:
                right = mid - 1 #search left

    return -1

#print(rotbin(nums, 3)) 

#A "mountain array" increases then decreases.
Example =  [1,3,5,7,4,2] 
#peak is 7
#Use binary search to find the peak index

def mountain(arr):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right)//2
        if arr[mid] < arr[mid+1]: #mid is in the rising slope still(ie dont search left)
            left = mid+1
        if arr[mid] > arr[mid+1]: #mid is the peak or on falling slope, can ignore right.
            right = mid #ignores right bc we use while left < right. NOT mid-1 cuz mid could be the peak
    return left #can return left cuz eventually right == left at the peak yes

print(mountain(Example))
#Sort a list of dictionaries (e.g., students with name and score) using merge sort, based on:
#primary key: score (descending)
#secondary key: name (alphabetically ascending)



#Sort a list of strings alphabetically using bubble sort (case-insensitive).

#N is a big number, K is a single digit integer from 0-9
#Find sum of specific digits of N, where the condition is index of the digits must be a multiple of K
#If the sum is NOT a single digit, repeat the 2nd step recursively on the sum until sum becomes a single digit

#ok wait so... first add digits, then check if its single digit. if not, repeat function

def loop(n, k):
    n = str(n)
    res = 0
    singledigit = False
    while singledigit == False:
        for i in range(len(n)):
            if i % k == 0: #if index is multiple of k then add the digit
                res += int(n[i])
                print(res)
        if len(str(res)) == 1:
            singledigit = True
        else:
            n = str(res)
            res = 0
    return res

    
#print(loop(9876543210, 2))

#ok new one where n stays the same
#so uh put n digits divisible by k into a list
#then first sum those digits
#if res not single digit, sum digits that are in the dictionary

def loop2(n,k):
    digits = [] #list of n digits with index divisible by k
    n = str(n)
    res = 0
    singledigit = False
    while singledigit == False:
        for i in range(len(n)):
            if i % k == 0:
                digits.append(int(n[i]))
        for j in range(len(digits)):
            if str(digits[j]) in n:
                res += digits[j]
        if len(str(res)) == 1:
            singledigit = True
        else: 
            n = str(res)
            res = 0
    return res

print('Keep N same, no recursion:', loop2(9876543210, 2))

#recursive changing n
def looprecursive(n,k):
    n = str(n)
    if len(n) == 1:
        return n
    gooddigits = [int(n[i]) for i in range(len(n)) if i % k == 0]

    res = sum(gooddigits)

    return looprecursive(res,k)

print('Change N, recursion:', looprecursive(1034489941, 1))

def loop2recursive(n,k,res = None):
    n = str(n)
    if res == None:
        gooddigits = [int(n[i]) for i in range(len(n)) if i % k == 0]
        res = sum(gooddigits)
    
    if res < 10:
        return res
    
    res2 = sum(int(d) for d in res)

    return loop2recursive(n,k,res)

#print('Same N, recursion:', loop2recursive(9876543210, 2))

print('abcdefg'.find('d'))
list1 = [1,2]
list1.append([3,4])
print(list1)

list1.pop(-1)
print(list1)

test = {"a":1}
test.update({"b":2})
print(test)