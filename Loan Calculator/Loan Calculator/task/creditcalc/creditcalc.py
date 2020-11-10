# loan_principal = int(input("Enter the loan principal: "))
#
# print("What do you want to calculate?")
# print('type "m" - for number of monthly payments,')
# calculation_type = input('type "p" - for the monthly payment:')
#
# if calculation_type == 'm':
#     payment_amount = int(input('Enter the monthly payment:'))
#     if payment_amount == loan_principal:
#         print('It will take 1 month to repay the loan')
#     else:
#         if loan_principal % payment_amount != 0:
#             number_of_payments = loan_principal // payment_amount + 1
#         else:
#             number_of_payments = loan_principal // payment_amount
#         print('It will take', number_of_payments, 'months to repay the loan')
#
# elif calculation_type == 'p':
#     number_of_months = int(input('Enter the number of months:'))
#
#     if loan_principal % number_of_months == 0:
#         payment = loan_principal // number_of_months
#         print('Your monthly payment =', payment)
#     else:
#         payment = loan_principal // number_of_months + 1
#         last_payment = loan_principal - (number_of_months - 1) * payment
#         print('Your monthly payment =', payment, 'and the last payment =', str(last_payment) + '.')
#
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

from math import ceil, log
from sys import argv


def incorrect_parameters():
    print("Incorrect parameters")


def differentiate_payment(values_dict):
    nominal_interest = values_dict["interest"] / (12 * 100)
    total_payment = 0
    for month in range(values_dict["periods"]):
        diff_payment = (int(values_dict["principal"] / values_dict["periods"])
                        + nominal_interest * (values_dict["principal"]
                                              - (values_dict["principal"] * ((month + 1) - 1)) / values_dict["periods"]))
        print(f'month {month}: payment is {ceil(diff_payment)}')
        total_payment += ceil(diff_payment)
    print()
    print(f'Overpayment = {ceil(total_payment - values_dict["principal"])}')


def annuity_calculation(values_dict):
    if "principal" in values_dict and "payment" in values_dict and "interest" in values_dict:
        nominal_interest = values_dict["interest"] / (12 * 100)
        num_of_months = log(values_dict["payment"] / (values_dict["payment"]
                                                      - nominal_interest * values_dict["principal"]),
                            1 + nominal_interest)
        num_of_months = ceil(num_of_months)

        if num_of_months < 12:
            print(f'It will take {num_of_months} months to repay this loan!')
        elif num_of_months % 12 == 0:
            print(f'It will take {num_of_months // 12} years to repay this loan!')
        else:
            print(f'It will take {num_of_months // 12} years and {num_of_months % 12} months to repay this loan!')
        print(f'Overpayment = {int(num_of_months * values_dict["payment"] - values_dict["principal"])}')
    elif "principal" in values_dict and "periods" in values_dict and "interest" in values_dict:
        nominal_interest = values_dict["interest"] / (12 * 100)
        annuity_payment = (values_dict["principal"]
                           * (nominal_interest * (1 + nominal_interest) ** values_dict["periods"])
                           / ((1 + nominal_interest) ** values_dict["periods"] - 1))
        print(f'You monthly payment = {ceil(annuity_payment)}!')
        print(f'Overpayment = {int(ceil(annuity_payment) * values_dict["periods"] - values_dict["principal"])}')
    elif "payment" in values_dict and "periods" in values_dict and "interest" in values_dict:
        nominal_interest = values_dict["interest"] / (12 * 100)
        loan_principal = (values_dict["payment"]
                          / ((nominal_interest * (1 + nominal_interest) ** values_dict["periods"])
                             / ((1 + nominal_interest) ** values_dict["periods"] - 1)))
        print(f'Your loan principal = {round(loan_principal)}!')
        print(f'Overpayment = {int(values_dict["payment"] * values_dict["periods"] - round(loan_principal))}')


args = argv
if len(args) != 5:
    incorrect_parameters()
else:
    if args[1] == "--type=diff":
        values = dict()
        for argument in args[2:]:
            if argument[:12] == "--principal=":
                values["principal"] = float(argument[12:])
            elif argument[:11] == "--interest=":
                values["interest"] = float(argument[11:])
            elif argument[:10] == "--periods=":
                values["periods"] = int(argument[10:])
            else:
                incorrect_parameters()
                break
        if len(values) == 3:
            differentiate_payment(values)
        else:
            incorrect_parameters()
    elif args[1] == "--type=annuity":
        values = dict()
        for argument in args[2:]:
            if argument[:12] == "--principal=":
                values["principal"] = float(argument[12:])
            elif argument[:11] == "--interest=":
                values["interest"] = float(argument[11:])
            elif argument[:10] == "--periods=":
                values["periods"] = int(argument[10:])
            elif argument[:10] == "--payment=":
                values["payment"] = int(argument[10:])
            else:
                incorrect_parameters()
                break
        if len(values) == 3:
            annuity_calculation(values)
        else:
            incorrect_parameters()
    else:
        incorrect_parameters()


# print("What do you want to calculate?")
# print('type "n" for number of monthly payments,')
# print('type "a" for annuity monthly payment amount,')
# calculation_type = input('type "p" for loan principal:')
#
# if calculation_type == 'n':
#     principal = float(input('Enter the loan principal:'))
#     monthly_payment = float(input('Enter the monthly payment:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     nominal_interest = loan_interest / (12 * 100)
#     num_of_months = log(monthly_payment / (monthly_payment - nominal_interest * principal),
#                         1 + nominal_interest)
#     num_of_months = ceil(num_of_months)
#
#     if num_of_months < 12:
#         print(f'It will take {num_of_months} months to repay this loan!')
#     elif num_of_months % 12 == 0:
#         print(f'It will take {num_of_months // 12} years to repay this loan!')
#     else:
#         print(f'It will take {num_of_months // 12} years and {num_of_months % 12} months to repay this loan!')
# elif calculation_type == 'a':
#     principal = float(input('Enter the loan principal:'))
#     periods = float(input('Enter the number of periods:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     nominal_interest = loan_interest / (12 * 100)
#     annuity_payment = (principal
#                        * (nominal_interest * (1 + nominal_interest) ** periods)
#                        / ((1 + nominal_interest) ** periods - 1))
#     print(f'You monthly payment = {ceil(annuity_payment)}!')
# elif calculation_type == 'p':
#     annuity_payment = float(input('Enter the annuity payment:'))
#     periods = float(input('Enter the number of periods:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     nominal_interest = loan_interest / (12 * 100)
#     loan_principal = (annuity_payment
#                       / ((nominal_interest * (1 + nominal_interest) ** periods)
#                          / ((1 + nominal_interest) ** periods - 1)))
#     print(f'Your loan principal = {round(loan_principal)}!')
