import math
import argparse

def calculate_monthly(p:int, i:float, num_of_periods:int, month:int):
    interest = (i / 100) / 12
    d = (p / num_of_periods) + (interest * (p - (p * (month - 1)) / num_of_periods))
    return math.ceil(d)


parser = argparse.ArgumentParser(description="this is a description of loan_calculator")

parser.add_argument('--type', choices=['annuity', 'diff'], help='You neded to vhoose type as annuity or diff')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest', help='Incorrect parameters')
parser.add_argument('--payment')
args = parser.parse_args()
if args.interest is None:
    args.type = 'Error'

if args.type == 'diff':
    if args.principal is not None:
        principal = float(args.principal)

    if args.periods is not None:
        periods = int(args.periods)

    if args.interest is not None:
        global interest
        interest = float(args.interest)

    if args.payment is not None:
        payment = int(args.payment)
    sum_of_payments = 0
    # print("type={} principal={} periods={} interest={} payment={}".format(args.type, principal,periods, interest, payment))
    for i in range(1, periods+1):
        current_payment:int = calculate_monthly(principal, interest, periods, i)
        print("Month "+str(i)+" "+str(current_payment))
        sum_of_payments += current_payment

    print()
    print("Overpayment = {}".format(int(sum_of_payments - principal)))

elif args.type == 'annuity':
    if args.principal is not None:
        principal = int(args.principal)
    else:
        calculate_type = 'p'

    if args.periods is not None:
        periods = int(args.periods)
    else:
        calculate_type = 'n'

    if args.interest is not None:
        interest = float(args.interest)
    else:
        calculate_type = 'error'

    if args.payment is not None:
        payment = int(args.payment)
    else:
        calculate_type = 'a'

    # print('What do you want to calculate?')
    # print('type "n" for number of monthly payments,')
    # print('type "a" for annuity monthly payment amount,')
    # print('type "p" for loan principal:')

    # calculate_type = input()
    if calculate_type == "n":
        # print('Enter the loan principal:')
        global loan_principal
        loan_principal = int(principal)
        # print("Enter the monthly payment:")
        global monthly_payment
        monthly_payment = int(payment) # int(input())
        global loan_interest
        # print('Enter the loan interest:')
        loan_interest = float(args.interest)
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
        print("Overpayment = {}".format((number_of_months * math.ceil(monthly_payment)) - loan_principal))
    elif calculate_type == "a":
        #print('Enter the loan principal:')
        # global loan_principal
        loan_principal = principal # int(input())
        # print("Enter the number of periods:")
        # global periods
        # periods =  int(input())
        # global loan_interest
        # print('Enter the loan interest:')
        loan_interest = float(interest) # float(input())
        nominal_interest = (loan_interest/100) / 12
        annuity_payment = loan_principal * ((nominal_interest * math.pow((1+nominal_interest), periods)) / (pow((1+nominal_interest), periods)-1))
        print("Your monthly payment = "+str((math.ceil(annuity_payment)))+"!")
        print("Overpayment = {}".format((periods * math.ceil(annuity_payment))-loan_principal))
    elif calculate_type == "p":
        # print("Enter the annuity payment:")
        annuity_payment = int(payment)
        # print("Enter the number of periods:")

        # periods = int(input())
        # print('Enter the loan interest:')
        # loan_interest = float(input())
        loan_interest = float(interest)
        nominal_interest = (loan_interest / 100) / 12
        loan_principal = annuity_payment / ((nominal_interest*math.pow((nominal_interest + 1), periods)) / (math.pow((1+nominal_interest), periods) - 1))

        print("Your loan principal = "+str(math.floor(loan_principal)) +"!")
        print("Overpayment = {}".format(math.ceil((periods * math.ceil(annuity_payment)) - loan_principal)))
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')


'''    
    if args.principal is not None:
        principal = int(args.principal)

    if args.periods is not None:
        periods = int(args.periods)

    if args.interest is not None:
        interest = int(args.interest)

    if args.payment is not None:
        payment = int(args.payment)

    print("principal={} periods={} interest={} payment={}".format(principal, periods, interest, payment))
'''

