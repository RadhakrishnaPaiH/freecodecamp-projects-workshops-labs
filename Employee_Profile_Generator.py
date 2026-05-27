#Employee's First and Last name stored in variable
first_name = 'John'
last_name = 'Doe'

#Concatenate First and Last to represent as a Full name
full_name = first_name + ' ' + last_name

#Store address in variable address
address = '123 Main Street'

#concat additional address string to previous address
address += ', Apartment 4B'

employee_age = 28

#Displays provided info in the format[John Doe is 28 years old]
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5

#Displays provided info in the format[Experience: 5 years]
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analyst'

salary = 75000

#Displays provided info in the format[Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000]
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

#Employee code
employee_code = 'DEV-2026-JD-001'

#Takes first 3 character from Employee code[Represents Department]
department = employee_code[0:3]
print(department)

#Takes character between position 4-8 in Employee code[Represents Year]
year_code = employee_code[4:8]
print(year_code)

#Takes character between position 9-11 in Employee code[Represents starting alphabet in name]
initials = employee_code[9:11]
print(initials)

#Takes last 3 digits from Employee code[001]
last_three=employee_code[-3:]
print(last_three)