"""Square Every Digit (Python)


def square_digits(num):
    result = ''
    for i in str(num):
        result += f"{int(i) ** 2}"

    return int(result)


Multiples of 3 or 5 (Python)


def solution(number):
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


Tetris Series #1 — Scoring System (Python)

    def get_score(arr) -> int:
    lvl = 1
    lines = 0
    score = 0
    bal = {0:0, 1:40, 2:100, 3:300, 4:1200}
    for i in arr:
        if lines >= 10:
            lines -= 10
            lvl += 1
        lines += i
        score += bal[i]*lvl
        #print(f"i={i} lines={lines} bal[i]={bal[i]} lvl={lvl} score={score} ")

    return score



Find the odd int

def find_it(seq):
    set_l = set(seq)
    for i in set_l:
        if not seq.count(i) % 2 == 0:
            return i



Substring fun (Python)

def nth_char(words):
    result = ''
    for num, i in enumerate(words):
        result += i[num]
    return result


Decoded String by the Numbers (Python)


def decode(str):
    result = []
    if str == '' :
        return result
    i =0
    while i < len(str):
        if str[i] == '\\':
            i += 1
            num = ''
            while str[i] in ['0','1','2','3','4','5','6','7','8','9']:
                num += str[i]
                i += 1
            num = int(num)
            if num > len(str[i:]):
                result.append(str[i:])
                return result
            else:
                result.append(str[i:i+num])
                i = i + num
        else:
            result.append(str[i])
            i += 1

    return result



Array.diff (Python)


def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

def array_diff(a, b):
    return diff(a,b)




 Thinking & Testing : Something capitalized (Python)

def testit(s):
    if s == "":
        return ""
    l = s.split(' ')
    result =''
    for i in l:
        result += f"{i[:-1]}{i[-1].upper()} "
    return result[:-1]


Arrh, grabscrab! (Python)

def eq(a, b):
    d = {}
    for i in a:
        if i not in d.keys():
            d[i] = a.count(i)
    for by in d.keys():
        if b.count(by) != d[by]:
            return False
    return True


def grabscrab(word, possible_words):
    result = []
    for i in possible_words:
        if len(i) == len(word):
            if eq(word, i):
                result.append(i)
    return result



Are they the "same"? (Python)

    def comp(array1, array2):
    print(array1)
    if array1 is None or array2 is None:
        return False
    a = []
    for i in array1:
        a.append(i*i)
    a.sort()
    array2.sort()
    if a == array2:
        return True
    else:
        return False



Dark Souls: Prepare To Die - Soul Level (Python)

from math import pow
def souls(character, build):
    dict = { 'warrior': (4,86), 'knight':(5,86), 'wanderer':(3,86),\
              'thief':(5,86), 'bandit':(4,86), 'hunter':(4,86), 'sorcerer':(3,82), 'pyromancer':(1,84),\
              'cleric':(2,84), 'deprived':(6,88)}
    lvl = dict[character][0]+(sum(build)-dict[character][1])
    soul = [0,0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829]
    ksoul = 0
    for i in range(dict[character][0]+1,lvl+1):
        print(f"-----")
        temp = ksoul
        print(f"{i} {ksoul}")
        if i <= 11:
            ksoul += soul[i]
        else:
            ksoul += round(pow(i, 3) * 0.02 + pow(i, 2) * 3.06 + 105.6 * i - 895)
        print(f"{i} {ksoul} {ksoul- temp}")

    return f"Starting as a {character}, level {lvl} will require {ksoul} souls."



Keep Hydrated! (SQL)

    select id, hours, floor(hours * 0.5) as liters FROM cycling


Convert number to reversed array of digits (Python)

    def digitize(n):
    res = []
    while n>0:
        res.append(n%10)
        n=n//10
    return res


What's the real floor? (Python)
    def get_real_floor(num):
    if num <= 0:
        return num
    if num < 13:
        return num-1
    if num > 13:
        return num-2



No zeros for heros (Python)

def no_boring_zeros(n):
    if n == 0:
        return n
    while n%10 == 0:
        n = n//10
    return n


Beginner Series #1 School Paperwork (Python)
    def paperwork(n, m):
    if n<0 or m <0:
        return 0
    return n*m


Beginner Series #2 Clock (Python)
    def past(h, m, s):
    return s * 1000 + 60000 * m + 60000*60*h




Sum of Minimums! (Python)

    def sum_of_minimums(numbers):
    result = 0
    for i in numbers:
        i.sort()
        result += i[0]
    return result
    
    
    
 Drying Potatoes (Python)   
   def potatoes(p0, w0, p1):
    result = w0 * (100 - p0) // (100 - p1)
    return result 


Will you survive the zombie onslaught? (Python)

def zombie_shootout(zombies, distance, ammo):
    range = distance * 2
    if zombies > ammo < range: 
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."
    elif zombies > range: 
        return f"You shot {range} zombies before being eaten: overwhelmed."
    return f"You shot all {zombies} zombies."    
    
    
  Tetris Series #1 — Scoring System (Python)
  
    def get_score(arr) -> int:
    lvl = 1
    lines = 0 
    score = 0
    bal = {0:0, 1:40, 2:100, 3:300, 4:1200}
    for i in arr:
        if lines >= 10:
            lines -= 10
            lvl += 1
        lines += i
        score += bal[i]*lvl
        #print(f"i={i} lines={lines} bal[i]={bal[i]} lvl={lvl} score={score} ")

    return score
    
Regexp Basics - is it a eight bit unsigned number? (Python)

  def eight_bit_number(n):
    print(n)
    if n == "":
        return False
    try:
        if 0 <= int(n) < 256 and str(int(n))==n:
            return True
        else:
            return False
    except:
        return False
        
        
        
  Regexp Basics - is it a six bit unsigned number? (Python)      
        
        def six_bit_number(n):
    try:        
        return int(n) >= 0 and int(n) < 64 and str(int(n)) == n
    except:
        return False
        
        
        
 Help Bob count letters and digits. (Python)       
        
    import string

def count_letters_and_digits(s):
    list = string.ascii_lowercase
    list2 = string.ascii_uppercase
    digits = string.digits
    count = 0
    for i in s:
        if i in list or i in list2 or i in digits:
            count += 1
    return count


Number Of Occurrences (Python)

def number_of_occurrences(element, sample):
    return sample.count(element)


Lottery machine (Python)

def lottery(s):
    digit = '0123456789'
    result = ''
    for i in s:
        if i in digit and i not in result:
            result += i
    if result == '':
        return "One more run!"
    else:
        return result
        
  
  Absent vowel (Python)
  
        def absent_vowel(s): 
    list = 'aeiou'
    for i, v in enumerate(list):
        if v not in s:
            return i
            
 Sum of angles (Python)
 
  def angle(n):
    return 180 * (n - 2)          
            
"""
