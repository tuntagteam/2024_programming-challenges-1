from itertools import combinations
from sympy import isprime

def find_prime_combinations(arr, target_sum):
    result = []
    
    for r in range(1, len(arr) + 1):
        for comb in combinations(arr, r):
            comb_sum = sum(comb)
            if comb_sum == target_sum:
                if isprime(comb_sum):
                    result.append(list(comb))
    
    return result

arr = list(map(int, input("อาร์เรย์ของจำนวนเต็ม: ").split()))
target_sum = int(input("จำนวนเต็มหนึ่งจำนวน: "))

combinations = find_prime_combinations(arr, target_sum)
print("ลิสต์ของค่าผสมที่ผลรวมเป็นจำนวนเฉพาะ:", combinations)