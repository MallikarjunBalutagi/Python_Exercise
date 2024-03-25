# Brilliant School sets an exam wherein, 
#     English exam is for 80 marks, 
#     Science for 90 marks and 
#     Mathematics for 100 marks. 

# Ask the student to enter the marks scored in each of these exams. 
# Calculate the total percentage marks and rank the student as below :
#   - First Class if score is more than or equal to 90 %
#   - Second Class if score is more than or equal to 75%
#   - Average if student has not failed
#   - Failed if score is less than or equal to 35 %

# Make sure your code uses the same principles as in the template codes of earlier exercises

def main():
    
    eng = int(input("Enter English marks: ",))
    sci = int(input("Enter Science marks: ",))
    math = int(input("Enter Mathematicks marks: ",))
    eng_per = eng / 80
    sci_per = sci / 90
    math_per = math / 100

    total_percentage = ((eng_per+sci_per+math_per) / 3) * 100
    print("total_percentage:", total_percentage)

    if total_percentage >= 90:
        print("First Class")
    elif total_percentage >= 75:
        print("Second Class")
    elif total_percentage > 35:
        print("Average")
    else:
        print("Fail")
        
main()
     
    
