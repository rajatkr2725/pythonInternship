def calculate_grade(marks_list):
    """Calculates average marks and assigns a corresponding letter grade."""
    if not marks_list:
        return 0, "No marks provided"
    
    total = sum(marks_list)
    average = total / len(marks_list)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return average, grade

# Example Usage
student_marks = [85, 92, 78, 90, 88]
avg, final_grade = calculate_grade(student_marks)
print(f"Average Marks: {avg:.2f} | Final Grade: {final_grade}")