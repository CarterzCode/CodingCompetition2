"""
Prints every other word to n
Carter Quarles - September 2026
"""

def main() -> None:


  # input
  n: int = int(input())
  # processing
  for i in range(n):
    if ((i+1)%2) == 0:
      input()
    else:
      print(input())





if __name__ == "__main__":
  main()
    
