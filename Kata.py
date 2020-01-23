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


    """

