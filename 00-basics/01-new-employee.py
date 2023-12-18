from prefect import flow, task

@task
def employee_registration():
    print("Employee getting registered")

@task
def update_payroll():
    print("Payroll updated")

@task
def issue_id_card():
    print("Printed id card and distributed")

@task
def employee_onboarding():
    print("Onboarded, training and documentation provided. ")


@flow()
def new_employee():
    employee_registration()
    update_payroll()
    issue_id_card()
    employee_onboarding()

new_employee()