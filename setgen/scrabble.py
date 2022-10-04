from itertools import product
from string import ascii_lowercase

def createfolders():
  alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  full = []
  combo4 = [''.join(i) for i in product(ascii_lowercase, repeat = 4)]
  combo3 = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]
  combo2 = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]
  combo1 = [''.join(i) for i in product(ascii_lowercase, repeat = 1)]

  for comb1 in combo1:
    full.append(comb1)

  for comb2 in combo2:
    full.append(comb2)

  for comb3 in combo3:
    full.append(comb3)

  for comb4 in combo4:
    full.append(comb4)

  for combo in full:
    f = open(f"newset/{combo}S.txt", "a")

def main():
  dictionary = open("dictionary.txt", "r")
  words = dictionary.readlines()

  for word in words:
    word = word.lower()
    word = word.strip()

    if len(word) == 1:
      f = open(f"newset/{word}S.txt", "a")
      f.write(f"{word}\n")
      f.close()
    elif len(word) == 2:
      f = open(f"newset/{word[0]}{word[1]}S.txt", "a")
      f.write(f"{word}\n")
      f.close()
    elif len(word) == 3:
      f = open(f"newset/{word[0]}{word[1]}{word[2]}S.txt", "a")
      f.write(f"{word}\n")
      f.close()
    elif len(word) >= 4:
      f = open(f"newset/{word[0]}{word[1]}{word[2]}{word[3]}S.txt", "a")
      f.write(f"{word}\n")
      f.close()

print("Creating folders...")
createfolders()
print("Creating files...")
main()
