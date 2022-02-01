
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 10                                |
# April 8, 2021                                   |
# Michael Belmear                                 |
# -------------------------------------------------

def read_file(file_name):
    file = open(file_name, 'r')
    line_0 = file.readline()
    school = []
    people = []
    for line in file:
        line = line.strip('\n')
        val = line.split(",")
        school.append(val[1])
        people.append(float(val[0]))
    college_names = np.array((school))
    college_enrollments = np.array((people))
    return(college_names, college_enrollments)

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    fig = plt.figure(figsize = (7, 5))
    fig.canvas.set_window_title('MSU Enrollments')
    plt.bar(college_names, college_enrollments, color = ['gold','blue'], width = 0.8)
    plt.yticks(np.arange(1000, 6000, 1000))
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.title("Fall 2020")
    plt.show()
# -------------------------------------------------

main("fall-2020.csv")

