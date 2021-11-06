import math


print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
calculate_type = input()
if calculate_type == "n":
    print('Enter the loan principal:')
    global loan_principal
    loan_principal = int(input())
    print("Enter the monthly payment:")
    global monthly_payment
    monthly_payment = int(input())
    global loan_interest
    print('Enter the loan interest:')
    loan_interest = float(input())
    global nominal_interest
    nominal_interest = (loan_interest / 100) / 12
    global number_of_months
    number_of_months = math.ceil(math.log( (monthly_payment / (monthly_payment - (nominal_interest * loan_principal))), 1+nominal_interest))
    years = number_of_months // 12
    rest_months = number_of_months % 12
    # print(number_of_months)
    global final_message
    if years > 0:
        final_message = ""
        if years == 1:
            final_message = str(years) + " year"
        elif years > 1:
            final_message = str(years) + " years"
    elif years == 0:
        final_message = ""
    if rest_months > 0:
        if rest_months == 1:
            final_message += (" and " + str(rest_months)+" month")
        elif rest_months > 1:
            final_message += (" and " + str(rest_months) + " months")
    final_message += " to repay this loan!"
    print(final_message)
elif calculate_type == "a":
    print('Enter the loan principal:')
    # global loan_principal
    loan_principal = int(input())
    print("Enter the number of periods:")
    global periods
    periods = int(input())
    # global loan_interest
    print('Enter the loan interest:')
    loan_interest = float(input())
    nominal_interest = (loan_interest/100) / 12
    annuity_payment = loan_principal * ((nominal_interest * math.pow((1+nominal_interest), periods)) / (pow((1+nominal_interest), periods)-1))
    print("Your monthly payment = "+str((math.ceil(annuity_payment)))+"!")
elif calculate_type == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")

    periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    nominal_interest = (loan_interest / 100) / 12
    loan_principal = annuity_payment / ((nominal_interest*math.pow((nominal_interest + 1), periods)) / (math.pow((1+nominal_interest), periods) - 1))

    print("Your loan principal = "+str(math.floor(loan_principal)) +"!")
