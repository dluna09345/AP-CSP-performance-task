#The goal of the program is to take in a series 
#of grades from the user and return their GPA based on the grades
#Ask the user for their date of graduation

import datetime
from typing import List

MARKING_PERIOD_COUNT=4
def get_fsjs():
    today = datetime.date.today()
    year = (today.strftime("%Y"))
    print("This GPA calcutaor will calculate your GPA (assuming that all classes are weighed the same) on a 5.0 scale")
    Class = int(input("What year will you graduate highschool?"))

    fsjs = ""
    if Class == (int(year)+3):
        fsjs = 1
    elif Class == (int(year)+2):
        fsjs = 2
    elif Class == (int(year)+1):
        fsjs = 3
    elif Class == (int(year)):
        fsjs = 4
        
    if Class > (int(year) + 3):
        print("You are too young to have a GPA.")
    elif Class < (int(year)):
        print("You are no longer a highschool student.")
    else:
        return fsjs

def current_mp():
    valid_marking_periods=[]
    for i in range(1,MARKING_PERIOD_COUNT+1):
        valid_marking_periods.append("MP"+str(i))
    current_marking_period=input_valid_value("What is your last marking period completed this year?",valid_marking_periods)
    return current_marking_period

def get_mps_single_year(year, mp):
    mps = []
    for i in range(1, mp+1):
        mps.append(year + "_"+ str(i)) 
    return mps  

def get_mps(year, mp):
    mps = []
    prefix = year
    if year == 2:
        mps = get_mps_single_year("y1", MARKING_PERIOD_COUNT)
    if year == 3:
        mps = get_mps_single_year("y1", MARKING_PERIOD_COUNT)
        mps = mps + get_mps_single_year("y2", MARKING_PERIOD_COUNT)
    if year == 4:
        mps = get_mps_single_year("y1", MARKING_PERIOD_COUNT)
        mps = mps + get_mps_single_year("y2", MARKING_PERIOD_COUNT)
        mps = mps + get_mps_single_year("y3", MARKING_PERIOD_COUNT)
    mpnumber=int(mp[-1])
    mps = mps + get_mps_single_year("y"+str(year), mpnumber)
    
    return mps



def input_valid_value(question:str, allowed_values:List[str]):
    valid_value = False
    allowed_values_str=""
    allowed_values_str=""
    for index, allowed_value in enumerate(allowed_values):
        if index==0:
            allowed_values_str=allowed_value
        else:
            allowed_values_str=allowed_values_str+","+allowed_value
    while valid_value == False:
        value = input(question + " Value must be any of the following: " + allowed_values_str + ":")
        if value in allowed_values:
            valid_value = True
        else:
            print("Value must be one of these values:" + allowed_values_str)
    return value
        

def get_classes(year):
    print(f'Please list out your classes below for year {year}:')
    classes = []
    exit = False
    while exit == False:
        Class = input("Enter class name: ")
        classes.append(Class)
        again = input_valid_value("Would you like add another class?(y/n)", ["y", "n"])
        if again == "n":
            exit = True
    return classes

def get_grades_for_mp(classes, mp):
    count=1
    dict = {}
    for _class in classes:
        grade = int(input(f'Enter {_class} grade for year {mp[1]} MP{mp[-1]} here:'))
        grade = (grade/100)*5
        dict[str(_class)]=grade
    count = count+1
    return dict

def calculate_gpa(all_grades):
    sum_of_all_grades = 0
    grade_count = 0
    for mp in all_grades.values():
        sum_of_all_grades = sum_of_all_grades+sum(mp.values())
        grade_count = grade_count+len(mp.values())
    gpa = sum_of_all_grades/grade_count
    return gpa

    
def main():
    fsjs = get_fsjs()
    mp = current_mp()
    mp_list = get_mps(fsjs, mp)
    classes = {}
    for i in range(1, fsjs+1):
        year = str(i)
        classes[year] = get_classes(year)

    mp_grades = {}

    for mp in mp_list:
        year=mp[1]
        classes_for_year=classes[year]
        mp_grades[mp]=get_grades_for_mp(classes_for_year, mp)

    print(f'Your estimated GPA is {str(calculate_gpa(mp_grades))}.')



    # mp_gpas = []
    # for i in range(mp):
    #     dict = get_grades_for_mp(classes, mp)
    #     mpgpa = get_gpa_for_mp(dict)
    #     mp_gpas.append(mpgpa)
    

    # if fsjs != "freshman":
    #     prev_gpa = float(input("What was your gpa last year?"))
    #     if fsjs == "sophomore":
    #         final_gpa = (prev_gpa+yearly_gpa)/2
    #     elif fsjs == "junior":
    #         final_gpa = (prev_gpa*2)+(yearly_gpa)/3
    #     elif fsjs == "senior":
    #         final_gpa = (prev_gpa*3)+(yearly_gpa)/4
    # else:
    #     final_gpa = yearly_gpa
    # print(final_gpa)


if __name__ == "__main__":
    main()
 
        

    
    




