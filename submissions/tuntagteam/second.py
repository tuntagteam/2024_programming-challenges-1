def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

# Get user input
s = input("กรอกสตริง: ")

# Check if the string is a Pangram
if is_pangram(s):
    longest = longest_word(s)
    print("คำที่ยาวที่สุดในสตริงที่เป็น Pangram คือ:", longest)
else:
    print("ไม่ใช่ Pangram")