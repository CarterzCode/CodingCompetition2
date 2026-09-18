"""
Sorts two numbers based on value
Carter Quarles - September 2026
"""

def main() -> None:
  # input
  a,b = input().split()
  a: int = int(a)
  b: int = int(b)

  # processing
  if a >= b:
    #output
    print(b,a)
  else:
    print(a,b)
  


if __name__ == "__main__":
  main()
    
