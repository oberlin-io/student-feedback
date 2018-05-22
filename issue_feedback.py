
#                   _  | | \
#                  / |_|_|  \
#                 _
#                /_|__|_|_|___\
#               /              .
#
#            Rubric and Gradesheet
#                   Printer
#
#             oberlin83@gmail.com
#
#
#
#
#

import re
import csv_list

scores = csv_list.make_list("scores.csv")
rubric = csv_list.make_list("rubric.csv")

for i in range(len(scores)):
	if i == 0:
		continue
	stu_id = scores[i][0]

	feedback = "Writing Task 1 Feedback\nModule: 4 (2016/2017)\nInstructor: John Oberlin\nLevel: 103\nSection: ADN\n"
	feedback += "Student ID: " + stu_id + "\n\n"


	structure = scores[i][1]
	feedback += "Structure: " + structure + "\n"

	for j in range(len(rubric)):
		if j == 0:
			continue

		if structure == "":
			continue
	
		if float(structure) >= float(rubric[j][0]):
			feedback += rubric[j][1] + "\n\n"
			break
	

	content = scores[i][2]
	feedback += "Content: " + content + "\n"

	for j in range(len(rubric)):
		if j == 0:
			continue

		if content == "":
			continue
	
		if float(content) >= float(rubric[j][0]):
			feedback += rubric[j][2] + "\n\n"
			break


	vocabulay = scores[i][3]
	feedback += "Vocabulary: " + vocabulay + "\n"

	for j in range(len(rubric)):
		if j == 0:
			continue

		if vocabulay == "":
			continue
	
		if float(vocabulay) >= float(rubric[j][0]):
			feedback += rubric[j][3] + "\n\n"
			break


	grammar = scores[i][4]
	feedback += "Grammar and Mechanics: " + grammar + "\n"

	for j in range(len(rubric)):
		if j == 0:
			continue

		if grammar == "":
			continue
	
		if float(grammar) >= float(rubric[j][0]):
			feedback += rubric[j][4] + "\n\n"
			break


	cohesion = scores[i][5]
	feedback += "Cohesion: " + cohesion + "\n"

	for j in range(len(rubric)):
		if j == 0:
			continue

		if cohesion == "":
			continue
	
		if float(cohesion) >= float(rubric[j][0]):
			feedback += rubric[j][5] + "\n\n"
			break


	total = scores[i][6]
	feedback += "Total: " + total + " from 5 points.\n"



	file_n = stu_id + ".txt"

	with open(file_n,"w") as f:
		f.write(feedback)

raw_input("Press enter to close.")