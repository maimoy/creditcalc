loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

print('Enter the loan principal:')
loan_principal = int(input())
print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment')
calculate_type = input()
if calculate_type == "m":
    print("Enter the monthly payment:")
    global monthly_payment
    monthly_payment = int(input())
    months = (-(-loan_principal // monthly_payment))
    last_payment = loan_principal - (months -1) * monthly_payment
    message_with_last_payment = f' and the last payment = {last_payment}'
    if months > 1 :
        message = f"It will take {months} months to repay loan"
    elif months == 1:
        message = f"It will take {months} month to repay loan"
    if last_payment != monthly_payment:
        print(message + message_with_last_payment)
    else:
        print(message)
elif calculate_type == "p":
    print("Enter the number of months:")
    requested_months = int(input())
    monthly_payment = (loan_principal // requested_months)
    last_payment = loan_principal - (requested_months -1) * monthly_payment
    message_with_last_payment = f' and the last payment = {last_payment}'
    message = f"Your monthly payment = {monthly_payment}"
    diff = last_payment - monthly_payment
    if diff > 0:
        diff_in_months = round(-(-diff // requested_months))
        monthly_payment = monthly_payment+diff_in_months
        last_payment = loan_principal - (requested_months-1) * monthly_payment
        message_with_last_payment = f' and the last payment = {last_payment}'
        message = f"Your monthly payment = {monthly_payment}"
        print(message + message_with_last_payment)
    else:
        print(message)
