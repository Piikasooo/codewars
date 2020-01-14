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
    """

