"""
Checks if a word is a palindrome
Carter Quarles - September 2026
"""

def main() -> None:
  # input
  word: str = input()
  flipped_word:str = word[::-1]
  # processing
  if word == flipped_word:
    print("Palindrome!")
  else:
    print("Nothing special about this string :(")
  # output


if __name__ == "__main__":
  main()
    
