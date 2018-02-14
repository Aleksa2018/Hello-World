# avg2.py
#    A simple program to avarage two exam scores
#    Illustrates use of multiple input

def main():
     print("This program computes the avarage of two exam scores.")
     
     score1, score2 = eval(input("Enter two scores separated by a comma: "))
     avarage = (score1 + score2) / 2

     print("The avarage of the scores is:", avarage)

main()