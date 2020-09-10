# Author: Chetan Mitra czm5805@psu.edu 
# Collaborator: Joseph DeRosa jvd5943@psu.edu
# Collaborator: Kacey Lo kll5550@psu.edu
# Collaborator: Jiaxia Li jpl6290@psu.edu
# Collaborator: Kirtan Shah kps5871@psu.edu
# Section: 11R
# Breakout Room: 6

def getLetterGrade(grade):
  if grade >= 93:
    return "A" 
  if grade >= 90:
    return "A-" 
  if grade >= 87:
    return "B+" 
  if grade >= 83:
    return "B" 
  if grade >= 80:
    return "B-" 
  if grade >= 77:
    return "C+" 
  if grade >= 70:
    return "C" 
  if grade >= 60:
    return "D" 
  else:
    return "F" 
def run():
  number = float(input("Enter your CMPSC 131 grade: "))
  letter = getLetterGrade(number)
  print (f"Your letter grade for CMPSC 131 is {letter}.")

if __name__ == "__main__":
 run()

