#Takes user input (name, job title, company), uses f-strings for formatting, and adds \n\n for readability.
print ("Create a quick job application message!")

name = input ("Enter your name: ")
job_tittle = input ("Enter the job tittle: ")
company = input ("Enter the company or place: ")

message = f"\nDear Hiring Manager,\n\nI am interested in applying for the {job_tittle} the position at {company}, Please consider my application. I look forward to the opportunity to discuss further. \n\nBest regards,\n{name}"

print(message)