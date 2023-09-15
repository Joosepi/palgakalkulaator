def main():
    # Ask user for employee name
    employee_name = input('Enter employee\'s name: ')

    # Ask user for number of hours worked
    hours_worked = float(input('Enter amount of hours worked: '))

    # Ask user for employee's pay rate
    pay_rate = float(input('Enter the employee\'s pay rate: '))
    overtime_pay_rate = pay_rate * 1.5

    # Calculate regular and overtime pay based on actual hours worked
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0.0
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * overtime_pay_rate

    # Calculate bruto pay and deductions for neto pay
    total_bruto_pay = regular_pay + overtime_pay

    # You can change the tax rate and other deductions as needed
    tax_rate = 0.20  # Example tax rate (you can adjust this)
    total_deductions = total_bruto_pay * tax_rate
    total_neto_pay = total_bruto_pay - total_deductions

    # Display employee details, bruto pay, and neto pay
    print('+' + '-'*90 + '+')
    print('|{:<40} {:<14}|'.format('Employee name:', employee_name))
    print('|{:<40} {:<14}|'.format('Hours Worked:', '{:.2f}'.format(hours_worked)))
    print('|{:<40} {:<14}|'.format('Pay Rate:', '{:.2f}'.format(pay_rate)))
    print('|{:<40} {:<14}|'.format('Regular Hours:', '{:.2f}'.format(regular_hours)))
    print('|{:<40} {:<14}|'.format('Overtime Hours:', '{:.2f}'.format(overtime_hours)))
    print('|{:<40} {:<14}|'.format('Regular Hour Pay:', '${:.2f}'.format(regular_pay)))
    print('|{:<40} {:<14}|'.format('Overtime Pay:', '${:.2f}'.format(overtime_pay)))
    print('|{:<40} {:<14}|'.format('Bruto Pay:', '${:.2f}'.format(total_bruto_pay)))
    print('|{:<40} {:<14}|'.format('Deductions:', '${:.2f}'.format(total_deductions)))
    print('|{:<40} {:<14}|'.format('Neto Pay:', '${:.2f}'.format(total_neto_pay)))
    print('+' + '-'*90 + '+')

# Program start
main()
