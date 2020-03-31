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
          
          
          
    Sort Out The Men From Boys (Python)      
          
          def men_from_boys(arr):
    mens = [x for x in sorted(set(arr)) if x % 2 == 0]
    boys = [x for x in sorted(set(arr), key=lambda n: -n) if x % 2 == 1]
    return mens + boys
    
    
    
  Form The Minimum (Python)
  
    def min_value(digits):
    listt = list(set(digits))
    listt.sort()
    result = ''
    for i in listt:
        result += str(i)
    return int(result)
    
    
    
    def top3(products, amounts, prices):
    dict = {product: amount * price for product, amount,
         price in zip(products, amounts, prices)}
    return sorted(dict.keys(), key=lambda x: dict[x], reverse=True)[:3]
    
    
  The fusc function -- Part 1 (Python)
  
    def fusc(n):
    if not n: return 0
    elif n == 1: return 1
    new = n // 2
    if n % 2: return fusc(new) + fusc(new + 1)
    return fusc(new)
    
    
    
   Selective fear of numbers (Python) 
    
    def am_I_afraid(day,num):
    if day == 'Monday' and num == 12: return True
    if day == 'Tuesday' and num > 95:return True
    if day == 'Wednesday' and num == 34: return True
    if day == 'Thursday' and num == 0: return True
    if day == 'Friday' and num%2 == 0: return True
    if day == 'Saturday' and num == 56: return True
    if day == 'Sunday' and (num == 666 or num == -666): return True
    return False
    
    
    
    Polydivisible Numbers
    
    def polydivisible(x):
    s = str(x)
    num = ''
    kount = 1
    for i in s:
        num += i
        if int(num) % kount != 0:
            return False
        kount += 1
    return True
    
    
    
    How many urinals are free? (Python)
    
    def get_free_urinals(urinals):
    if urinals.count("11") > 0:
        return -1   
    urinals = "0" + urinals + "0"
    kount = 0
    while "000" in urinals:    
        urinals = urinals.replace("000", "010", 1)
        kount += 1      
    return kount
    
    
    
    
    String ends with? (Python)
    def solution(string, ending):
    
    if string[len(string) - len(ending):] == ending:
        return True
    else:
        return False
        
    
    
    Complete The Pattern #1
    def pattern(n):
    result = ''
    for i in range(n):
        result += f'{str(i+1) * (i+1)}\n'
    return result[:-1]
    
    
    
    
    
    Complete The Pattern #2 (Python)
    
    def pattern(n):
    s = str(n)
    if n < 1:
        return ''
    lst = []
    lst.append(s)
    while n > 1:
        n -= 1
        s+=str(n)
        lst.append(s)
    return '\n'.join(lst[::-1])
    
 
 
 
 See You Next Happy Year (Python)   
    
    def next_happy_year(year):
  year += 1
  while True:
    if len(set(str(year))) == 4:
      return year
    else:
      year += 1
      
      
      
   Row Weights (Python)
   
      def row_weights(array):
    return sum(array[::2]), sum(array[1::2])
    
    
    
 Growth of a Population (Python)   
    
    def nb_year(p0, percent, aug, p):
    percent = percent / 100
    count = p0
    year = 0
    while p > count:
        count += count * percent + aug
        year += 1
    return year
    
    
    
    Extra Perfect Numbers (Special Numbers Series #7) (Python)
    
    def extra_perfect(n):
    result = []
    for i in range(1,n+1):
        if bin(i)[2] == bin(i)[-1]:
            result.append(i)
    return(result)
    
    
    
    
   Two Oldest Ages (Python) 
    
    def two_oldest_ages(ages):
  ages.sort()
  return ages[-2:]
  
  
  
  Looking for a benefactor (Python)
  
  import math
def new_avg(arr, newavg): 
    result = math.ceil(float((len(arr)+1))*newavg - sum(arr))
    if result < 0:
        raise ValueError
    else:
        return result
 
 
 
 Consecutive Ducks (Python)
 
 def consecutive_ducks(num):
    sum = 0
    for i in range(1,num//2):
        sum += i
        if sum > num:
            continue
        if (num-sum) % (i+1) == 0:
            return True
    return False
    
    
    
    The Office VI - Sabbatical (Python)
    
    def sabb(s, value, happiness):
    str = 'sabbatical'
    for i in s:
        if i in str:
            value += 1
    if value + happiness > 22:
        return 'Sabbatical! Boom!'
    else:
        return "Back to your desk, boy."
        
        
   
   Greatest Common Divisor Bitcount (Python)
        
    def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b)

def binary_gcd(x, y):
    result = hcfnaive(x,y)
    if result > 0:
        s = bin(result)[2:]
    else:
        s = bin(result)[3:]
    result = 0
    print(s)
    for i in s:
        result += int(i)
    return result
    
    
    
    Tidy Number (Special Numbers Series #9) (Python)
    
    def tidyNumber(n):
    s = str(n)
    for i in range(1,len(s)):
        if int(s[i]) < int(s[i-1]):
            return False
    return True
    
    
    
    Automorphic Number (Special Numbers Series #6) (Python)
    
    def automorphic(n):
    if str(n) == str(n*n)[len(str(n*n))-len(str(n)):]:
        return "Automorphic"
    else:
        return "Not!!"
        
              
        
        def make_move(sticks):
    return sticks%4
    
    
    
  List of all Rationals (Python)  
    
  def all_rationals():
    tree = [(1, 1)]
    for number in tree:
        left, right = number
        tree.append((left, left+right))
        tree.append((left+right, right))
        yield number
        
        
        
  Product Array (Array Series #5) (Python)      
        
   def product_array(numbers):
    result = []
    for i in range(len(numbers)):
        mul = 1
        for index, value in enumerate(numbers):
            if index != i :
                mul *= value
        result.append(mul)
    return(result)     
        
        
     Nth Smallest Element (Array Series #4)   
        
        def nth_smallest(arr, pos):
    arr.sort()
    return arr[pos-1]
    
    
    
    Easy Line (Python)
    
    import math as m
def easyline(n):
    return m.factorial(2*n)//(m.factorial(n)**2)
    
    
    
    Thinkful - Number Drills: Blue and red marbles
    
    def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue_in = blue_start - blue_pulled
    red_in = red_start - red_pulled
    result = blue_in / (blue_in + red_in)
    return result
    
    
   No oddities here (Python) 
    
    def no_odds(values):
    return [x for x in values if x%2==0]
    
    
    
    Alternate capitalization (Python)
    
def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        if i % 2:
            result[0] += c.lower() 
            result[1] += c.upper() 
        else:
            result[0] +=  c.upper()
            result[1] +=  c.lower()
    return result




Persistent Bugger. (Python)

def persistence(n):
    count = 0
    while n > 9:
        k = 1
        for i in str(n):
            k = k * int(i)
        n = k
        count += 1
    return count
    
    
   Sum of Digits / Digital Root (Python) 
    
  def digital_root(n):
    c = 0
    while n > 9:
        for i in str(n):
            c += int(i)
        n, c = c, 0
    return n
    
    
    
    
    Detect Pangram (Python)
    
    import string

def is_pangram(s):
    for i in string.ascii_lowercase:
        if i not in s.lower():
            return False
    return True
    
    
    Duplicate Encoder (Python)
    
    def duplicate_encode(word):
    res = ""
    word=word.lower()
    for i in word:
        if word.count(i) >1:
            res+=")"
        else:
            res+="("
    return res
    
    
    
    Consonant value
    
    import string 
def count_cost(s):
    d = {}
    for i , j in enumerate(string.ascii_lowercase):
        d[j] = i+1
    res = 0
    for i in s:
        res += d[i]
    return res


def solve(s):
    lst = []
    let = "aeiou"
    i = 0
    str = ''
    while i < len(s):
        if s[i] not in let:
            str += s[i]
        else:
            if str != '':
                lst.append(str)
            str = ''
        i += 1
    if str != '':
        lst.append(str)
    
    res = 0
    for i in lst:
        if count_cost(i) > res:
            res = count_cost(i)
    return res
    
  
  
  More Zeros than Ones
    
   def decode(s):
    bin_arr = s.encode()
    bin_int = int.from_bytes(bin_arr, "big")
    bin_str = bin(bin_int)
    if len(bin_str[2:]) != 7:
        bin_str = f'0{bin_str}'
    return bin_str[2:]


def more_zeros(s):
    res = []
    for i in s:
        if decode(i).count('0') > decode(i).count('1') and i not in res:
            res.append(i)
    return res 
    
    
    
    
    
    Sums of Parts
    
    
    def parts_sums(ls):
    res = []
    count = sum(ls)
    for i in ls :
        res.append(count)
        count -= i
    res.append(0)
    return res
    
    
    
    
    Expressions Matter (Python)
    def expression_matter(a, b, c):
     return max(a + b + c, (a + b) * c, a * (b + c), a * b * c)
     
     
     
     Will you make it? (Python)
     
     
     def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False
    """
