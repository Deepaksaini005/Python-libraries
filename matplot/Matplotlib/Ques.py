# 10 students   ,  5 subjects   marks plot

import matplotlib.pyplot as plt
import numpy as np

students = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']

subjects = ['Math', 'Science', 'English', 'History', 'python']

marks = np.random.randint(40, 100, size=10)
bar_width = 0.15

p = np.arange(len(students))

p1 = [i for i in p]

p2 = [i + bar_width for i in p1]
p3 = [i + bar_width  for i in p2]
p4 = [i + bar_width  for i in p3]
p5 = [i + bar_width  for i in p4]

plt.bar(p1, marks[0], width=bar_width, label='Math', color='red', edgecolor='black')

plt.bar(p2, marks[1], width=bar_width, label='Science', color='blue', edgecolor='black')

plt.bar(p3, marks[2], width=bar_width, label='English', color='green', edgecolor='black')

plt.bar(p4, marks[3], width=bar_width, label='History', color='orange', edgecolor='black')

plt.bar(p5, marks[4], width=bar_width, label='Python', color='purple', edgecolor='black')

plt.xlabel("Students", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.title("Student Marks in Different Subjects", fontsize=14)

plt.grid(axis ='y')
plt.legend()
plt.show()

