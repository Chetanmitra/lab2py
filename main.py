# Author: Chetan Mitra czm5805@psu.edu 
# Collaborator: Joseph DeRosa jvd5943@psu.edu
# Collaborator: Kacey Lo kll5550@psu.edu
# Collaborator: Jiaxia Li jpl6290@psu.edu
# Collaborator: Kirtan Shah kps5871@psu.edu
# Section: 11R
# Breakout Room: 6

def getLetterGrade(grade):
  if grade >= 93:
    return print("Your letter grade for CMPSC 131 is A.") 
  if grade >= 90:
    return print("Your letter grade for CMPSC 131 is A-.") 
  if grade >= 87:
    return print("Your letter grade for CMPSC 131 is B+.") 
  if grade >= 83:
    return print("Your letter grade for CMPSC 131 is B.") 
  if grade >= 80:
    return print("Your letter grade for CMPSC 131 is B-.") 
  if grade >= 77:
    return print("Your letter grade for CMPSC 131 is C+.") 
  if grade >= 70:
    return print("Your letter grade for CMPSC 131 is C.") 
  if grade >= 60:
    return print("Your letter grade for CMPSC 131 is D.") 
  else:
    return print("Your letter grade for CMPSC 131 is F.") 

if __name__ == "__main__":
  getLetterGrade()

