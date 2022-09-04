def main():
    loan,interest_rate,num_periods = collect_inputs()
    monthly_rate = interest_rate/100/12
    pmt = monthly_payment(loan,monthly_rate,num_periods)
    total_to_pay = total_mortage(pmt,num_periods)
    interest = total_interest(total_to_pay,loan)
    pmts = payments(pmt, total_to_pay, monthly_rate, num_periods)
    header_inputs = (loan, num_periods, interest, pmt)
    table = make_table(pmts, header_inputs)
    print(table)
    with open('mortgage.txt', 'w') as file:
        file.write(table)

def collect_inputs():
    loan = float(input("How much do you want to borrow?: "))
    interest_rate = float(input("What is interest rate?: "))
    num_periods = int(input('For how many years?: ')) * 12
    print()
    return loan, interest_rate, num_periods

def monthly_payment(loan,monthly_rate,num_periods):
    return round((loan * (monthly_rate * (1 + monthly_rate) ** num_periods) / ((1 + monthly_rate) ** num_periods - 1)))

def total_mortage(monthly_payment,num_periods):
    return monthly_payment * num_periods

def total_interest(mortage, loan):
    return mortage - loan

def payments(pmt, total_to_pay, monthly_rate, num_periods):
    payments = []
    for month in range(1, num_periods + 1):
        month_interest = round(total_to_pay * monthly_rate)
        payments.append((month, month_interest,
                     round(pmt - month_interest),
                     round(total_to_pay)))
    total_to_pay -= pmt
    return payments

def make_table(pmts, header_inputs):
    header = make_header(*header_inputs)
    table = header + pmts
    widths = column_widths(table)
    header_template = '|{:^{w1}}|{:^{w2}}|{:^{w3}}|{:^{w4}}|'
    data_template = '|{:^{w1},}|{:^{w2},}|{:^{w3},}|{:^{w4},}|'
    formatted_table = format_rows(header, header_template, widths, [])
    formatted_table = format_rows(pmts, data_template, widths, formatted_table)
    formatted_table = insert_lines(formatted_table, (1, 3))
    return '\n'.join(formatted_table)

def make_header(loan, num_periods, interest, pmt):
        return [['Loan: %d' % loan, 'Years: %d' % (num_periods / 12),
             'Interest: %d' % interest, 'Monthly Payment: %d' % pmt],
            ['Payment', 'Interest', 'Principal', 'Left to Pay']]

def column_widths(table):
    num_cols = len(table[0])
    col_widths = {}
    for col_num in range(num_cols):
        column = extract_column(col_num, table)
        col_width = len(max(column, key=len)) + 4
        col_widths['w%d' % (col_num + 1)] = col_width
    return col_widths

def extract_column(col_num, table):
    column = []
    for row in table:
        column.append(str(row[col_num]))
    return column

def format_rows(data, template, widths, formatted_table):
    for row in data:
        line = template.format(*row, **widths)
        formatted_table.append(line)
    return formatted_table

def insert_lines(table, row_nums, sign='='):
    width = len(max(table, key=len))
    for row_num in row_nums:
        table.insert(row_num, sign * width)
    return table


main()