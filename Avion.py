"""
Describe your program.
First Last - Month Year
"""

def main() -> None:

  did_he_get_away: bool = True

  # input
  for i in range(5):
    blimp: str = input()
    if blimp.find("FBI") != -1:
      print(i+1)
      did_he_get_away = False
  # processing
  if did_he_get_away:
    print("HE GOT AWAY!")
  
  # output


if __name__ == "__main__":
  main()
    
