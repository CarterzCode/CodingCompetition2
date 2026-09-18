"""
Checks what type of word the inputted word is based on the number of b's and k's
Carter Quarles - September 2026
"""

def main() -> None:
  # input
  word: str = input()

  # processing
  b:int = word.count("b")
  k:int = word.count("k")
  
  # output
  if b > k:
    print("boba")
  elif b < k:
    print("kiki")
  elif (b+k) == 0:
    print("none")
  else:
    print("boki")
if __name__ == "__main__":
  main()
    
