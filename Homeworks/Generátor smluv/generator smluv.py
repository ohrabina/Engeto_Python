TEMPLATE_PATH = 'C:\Users\hrabi\Documents\Python\Engeto\Homeworks\Generátor smluv\Templates'
CONTRACTS_PATH = 'C:\Users\hrabi\Documents\Python\Engeto\Homeworks\Generátor smluv\Contracts'
EMPLOYEE_DB_PATH = 'C:\Users\hrabi\Documents\Python\Engeto\Homeworks\Generátor smluv\employees.txt'
TEMPLATES = ['salary_change', 'job_change', 'contract_prolongation']

def main():
    #volba šablony
    num = int(input(print_prompt()))
    #databáze
    employees = load_db(EMPLOYEE_DB_PATH)
    #šablona
    template_name = TEMPLATES[num].replace(' ', '_')
    #nahrani šablony
    template = load_template(template_name)
    #generace smlouvy
    for employee_id, employee in employees.items():
        print('Creating contract for %s ....' % (employee_id,))
        write_file(employee, template, template_name)
    # Tisk zaverecne zpravy pro uzivatele
    print('\nContracts have been generated.')

def print_prompt():
    print("Pleases select and option number of action you want to perform:\n")
    for temp in enumerate(TEMPLATES):
        print('{}. {}'.format(*temp))
    return '\n'

def load_db(path):
    with open(path) as employees_file:
        content = employees_file.read()
    return eval(content)

def load_template():
    template_path = '{}/{}.txt'.format(TEMPLATE_PATH,template_name)
    with open(template_path) as template_file:
        template = template_file.read()
    return template

def write_file(employee, template, template_name):
    # Ziskani jmena souboru
    filename = '{}_{}.txt'.format(template_name, employee['full_name'])
    # Ziskani cesty k souboru
    filepath = '{}/{}'.format(CONTRACTS_PATH, filename)
    # Kontextovy manazer
    with open(filepath, 'w') as new_file:
        # Zapis do noveho souboru
        new_file.write(template.format(**employee))

main()