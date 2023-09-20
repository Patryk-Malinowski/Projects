# Patryk Malinowski
# Programming Fundamentals Project
# Keep track of jobs for recruitment agency


amount_of_jobs = int(input("How many jobs would you like to add? "))
print()

table = (f"{'ID':5}{'Job Title':16}{'Location':14}{'EXP':6}{'Rate(€)':10}{'Hours':10}{'Earnings(€)'}"
         f"\n{'=' * 72}")

i = 1  # used to initiate loop
ID = 0
yes_or_no = ("y", "n")  # allows user to type anything starting with a 'y' or 'n' for work experience

while i <= amount_of_jobs:
    try:
        print(f"Enter Details of Job {i}")
        title = str(input("Job title: ")).capitalize()
        while title == "":  # ensures the title cannot be left blank
            title = str(input("Job title: ")).capitalize()
        company_name = str(input("Company name: ")).upper()
        while company_name == "":  # ensures the company name cannot be left blank
            company_name = str(input("Company name: ")).upper()
        employment = int(input("Please specify the type of employment\n"
                               "1. Full Time\n"
                               "2. Part Time\n"
                               "===> "))
        while employment < 1 or employment > 2:  # either part-time or full-time employment has to be chosen
            employment = float(input("Please specify the type of employment\n"
                                     "1. Full Time\n"
                                     "2. Part Time\n"
                                     "===> "))
        if employment == 1:
            hours: float = 40
        elif employment == 2:
            hours = float(input("Hours per week: "))
            while hours <= 0 or hours >= 40:  # part-time hours must be greater than 0 and less than 40
                hours = float(input("Hours per week: "))
        experience = str(input("Does this job require experience? (Yes/No) ")).lower()
        while not experience.startswith(yes_or_no):
            experience = str(input("Does this job require experience? (Yes/No) ")).lower()
        rate = float(input("Rate of pay per hour: "))
        while rate <= 0:  # rate of pay must be greater than 0
            rate = float(input("Rate of pay per hour: "))
        print("-" * 72)
        print()
        i += 1
        ID += 1
        earnings = hours * rate
        table += f"\n{ID:<5}{title:16}{company_name:14}{experience:6}{rate:<10.2f}{hours:<10.1f}{earnings:.2f}"
        if employment == 1:
            with open("full-time.txt", "a") as connection:
                job = f"{title},{company_name},{experience},{rate:.2f},{hours:.1f},{earnings:.2f}"
                print(job, file=connection)
        elif employment == 2:
            with open("part-time.txt", "a") as connection:
                job = f"{title},{company_name},{experience},{rate:.2f},{hours:.1f},{earnings:.2f}"
                print(job, file=connection)
    except IOError:
        print("Error! There has been an error with the file you are searching for ")

count_ft = 0
count_pt = 0
lowest_pay = 999999999
highest_pay = -99999999
jobs_total = 0  # counts total amount of jobs in a text file such as full-time.txt or part-time.txt
total_rates = 0  # totals all the rates to later find the average hourly rate
highest_job = ""
highest_company = ""

with open("full-time.txt", "r") as connection:
    for line in connection:
        count_ft += 1
        line = line.split(",")
        pay = float(line[3])
        job = line[0]
        company = line[1]
        total_rates += pay
        jobs_total += 1
        if pay > highest_pay:
            highest_pay = pay
            highest_job = job
            highest_company = company
        if pay < lowest_pay:
            lowest_pay = pay
with open("part-time.txt", "r") as connection:
    for line in connection:
        count_pt += 1
        line = line.split(",")
        pay = float(line[3])
        job = line[0]
        company = line[1]
        total_rates += pay
        jobs_total += 1
        if pay > highest_pay:
            highest_pay = pay
            highest_job = job
            highest_company = company
        elif pay < lowest_pay:
            lowest_pay = pay

print(table)

average_pay = total_rates / jobs_total

print("-" * 72)
print()
print("Summary")
print("=" * 8)
print()
print(f"Full-Time Jobs: {count_ft} - full-time.txt has been updated")
print(f"Part-Time Jobs: {count_pt} - part-time.txt has been updated")
print()
print(f"Hourly pay rate ranges from €{lowest_pay:.2f} to €{highest_pay}")
print()
print(f"Average Hourly Rate: €{average_pay:.2f}")
print()
print(f"Highest Paying Job Details: {highest_job} at {highest_company}")
