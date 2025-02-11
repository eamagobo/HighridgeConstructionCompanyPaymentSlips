from unicodedata import category
age = 47

sex = "Male", "Female"
employees = ['Emp1', 'Emp2', 'Emp3', 'Emp4','Emp5', 'Emp6', 'Emp7', 'Emp8', 'Emp9', 'Emp10','Emp11', 'Emp12', 'Emp13', 'Emp14', 'Emp15', 'Emp16', 'Emp17', 'Emp18', 'Emp19', 'Emp20', 'Emp21', 'Emp22', 'Emp23', 'Emp24', 'Emp25', 'Emp26', 'Emp27', 'Emp28', 'Emp29','Emp30', 'Emp31', 'Emp32', 'Emp33', 'Emp34', 'Emp35','Emp36', 'Emp37', 'Emp38', 'Emp39', 'Emp40', 'Emp41', 'Emp42', 'Emp43', 'Emp44', 'Emp45', 'Emp46', 'Emp47', 'Emp48', 'Emp49', 'Emp50','Emp51', 'Emp52', 'Emp53', 'Emp54','Emp55', 'Emp56', 'Emp57', 'Emp58', 'Emp59', 'Emp60','Emp61', 'Emp62', 'Emp63', 'Emp64', 'Emp65', 'Emp66', 'Emp67', 'Emp68', 'Emp69', 'Emp70', 'Emp71', 'Emp72', 'Emp73', 'Emp74', 'Emp75', 'Emp76', 'Emp77', 'Emp78', 'Emp79','Emp80', 'Emp81', 'Emp82', 'Emp83', 'Emp84', 'Emp85','Emp86', 'Emp87', 'Emp88', 'Emp89', 'Emp90', 'Emp91', 'Emp92', 'Emp93', 'Emp94', 'Emp95', 'Emp96', 'Emp97', 'Emp98', 'Emp99', 'Emp100', 'Emp101', 'Emp102', 'Emp103', 'Emp104', 'Emp105', 'Emp106', 'Emp107', 'Emp108', 'Emp109', 'Emp110', 'Emp111', 'Emp112', 'Emp113', 'Emp114','Emp115', 'Emp116', 'Emp117', 'Emp118', 'Emp119', 'Emp120','Emp121', 'Emp122', 'Emp123', 'Emp124', 'Emp125', 'Emp126', 'Emp127', 'Emp128', 'Emp129', 'Emp130', 'Emp131', 'Emp132', 'Emp133', 'Emp134', 'Emp135', 'Emp136', 'Emp137', 'Emp138', 'Emp139','Emp140', 'Emp141', 'Emp142', 'Emp143', 'Emp144', 'Emp145','Emp146', 'Emp147', 'Emp148', 'Emp149', 'Emp150', 'Emp151', 'Emp152', 'Emp153', 'Emp154', 'Emp155', 'Emp156', 'Emp157', 'Emp158', 'Emp159', 'Emp160', 'Emp161', 'Emp162', 'Emp163', 'Emp164','Emp165', 'Emp166', 'Emp167', 'Emp168', 'Emp169', 'Emp170','Emp171', 'Emp172', 'Emp173', 'Emp174', 'Emp175', 'Emp176', 'Emp177', 'Emp178', 'Emp179', 'Emp180', 'Emp181', 'Emp182', 'Emp183', 'Emp184', 'Emp185', 'Emp186', 'Emp187', 'Emp188', 'Emp189','Emp190', 'Emp191', 'Emp192', 'Emp193', 'Emp194', 'Emp195','Emp196', 'Emp197', 'Emp198', 'Emp199', 'Emp200', 'Emp201', 'Emp202', 'Emp203', 'Emp204', 'Emp205', 'Emp206', 'Emp207', 'Emp208', 'Emp209', 'Emp210', 'Emp211', 'Emp212', 'Emp213', 'Emp214','Emp215', 'Emp216', 'Emp217', 'Emp218', 'Emp219', 'Emp220','Emp221', 'Emp222', 'Emp223', 'Emp224', 'Emp225', 'Emp226', 'Emp227', 'Emp228', 'Emp229', 'Emp230', 'Emp231', 'Emp232', 'Emp233', 'Emp234', 'Emp235', 'Emp236', 'Emp237', 'Emp238', 'Emp239','Emp240', 'Emp241', 'Emp242', 'Emp243', 'Emp244', 'Emp245','Emp246', 'Emp247', 'Emp248', 'Emp249', 'Emp250', 'Emp251', 'Emp252', 'Emp253', 'Emp254', 'Emp255', 'Emp256', 'Emp257', 'Emp258', 'Emp259', 'Emp260', 'Emp261', 'Emp262', 'Emp263', 'Emp264','Emp265', 'Emp266', 'Emp267', 'Emp268', 'Emp269', 'Emp270','Emp271', 'Emp272', 'Emp273', 'Emp274', 'Emp275', 'Emp276', 'Emp277', 'Emp278', 'Emp279', 'Emp280', 'Emp281', 'Emp282', 'Emp283', 'Emp284', 'Emp285', 'Emp286', 'Emp287', 'Emp288', 'Emp289','Emp290', 'Emp291', 'Emp292', 'Emp293', 'Emp294', 'Emp295','Emp296', 'Emp297', 'Emp298', 'Emp299', 'Emp300', 'Emp301', 'Emp302', 'Emp303', 'Emp304', 'Emp305','Emp306', 'Emp307', 'Emp308', 'Emp309', 'Emp310', 'Emp311', 'Emp312', 'Emp313', 'Emp314', 'Emp315','Emp316', 'Emp317', 'Emp318', 'Emp319', 'Emp320', 'Emp321','Emp322', 'Emp323', 'Emp324', 'Emp325', 'Emp326', 'Emp327', 'Emp328', 'Emp329', 'Emp330', 'Emp331','Emp322', 'Emp333', 'Emp334', 'Emp335', 'Emp336', 'Emp337', 'Emp338', 'Emp339', 'Emp340', 'Emp341', 'Emp342', 'Emp343', 'Emp344', 'Emp345', 'Emp346', 'Emp347','Emp348', 'Emp349', 'Emp350', 'Emp351', 'Emp352', 'Emp353','Emp354', 'Emp355', 'Emp356', 'Emp357', 'Emp358', 'Emp359', 'Emp360', 'Emp361', 'Emp362', 'Emp363','Emp364', 'Emp365', 'Emp366', 'Emp367', 'Emp368', 'Emp369', 'Emp370', 'Emp371', 'Emp372', 'Emp373','Emp374', 'Emp375', 'Emp376', 'Emp377', 'Emp378', 'Emp379','Emp380', 'Emp381', 'Emp382','Emp383', 'Emp384','Emp385', 'Emp386','Emp387', 'Emp388','Emp389','Emp390', 'Emp391', 'Emp392', 'Emp393', 'Emp394', 'Emp395', 'Emp396', 'Emp397', 'Emp398', 'Emp399', 'Emp400' ]
print(employees)
detailed_list =[]
for employee in employees:
    salary = 1000
    job = 'category'
    emp = {
        'employee_name':employee,
        'employee_age':age,
        'employee_gender':sex,
        'job_category':category,
        'employee_salary': salary,
    }
    detailed_list.append(emp)
for x in detailed_list:
    print(x)

employees = [
    {'name': 'Elisha', 'salary': 16000, 'gender': 'Male'},
    {'name': 'Agnes', 'salary': 18000, 'gender': 'Female'},
    {'name': 'Boniphace', 'salary': 12000, 'gender': 'Female'},
    {'name': 'Erick', 'salary': 20000, 'gender': 'Male'},
    {'name': 'Jennifer', 'salary': 22000, 'gender': 'Female'},
]
for employee in employees:
    salary = employee['salary']
    gender = employee['gender']
    if 10000 < salary < 20000:
        employee['level'] = 'A1'
    if 7500 < salary < 30000 and gender == 'Female':
        employee['level'] = 'A5-F'
for emp in employees:
    print(emp)


employees = [
    {"name": 'Elisha', 'salary': 16000, 'gender': 'Male'},
    {"name": 'Agnes', 'salary': 18000, "gender": 'Female'},
    {"name": 'Boniphace', 'salary': 12000, 'gender': 'Male'},
    {"name": 'Erick', 'salary': 20000, 'gender': 'Male'},
    {"name": 'Jennifer', 'salary': 25000, 'gender': 'Female'},
    {"name": 'TypoError', 'salary': 'incorrect bank account', "gender": 'Not specified'},
]

for employee in employees:
    try:
        salary = int(employee["salary"])
        gender = employee.get("gender", "").capitalize()

        if 10000 < salary < 20000:
            employee["level"] = "A1"

        if 7500 < salary < 30000 and gender == "Female":
            employee["level"] = "A5-F"

    except ValueError:
        print(f"Error: Invalid salary value for {employee['name']}. Skipping this employee.")
        employee["level"] = "Error"
    except KeyError as e:
        print(f"Error: Missing key {e} in employee record. Skipping this employee.")
        employee["level"] = "Error"
    except Exception as e:
        print(f"Unexpected error for {employee['name']}: {e}")
        employee["level"] = "Error"

for emp in employees:
    print(emp)
