from sqlalchemy_client import SQLAlchemyClient
from table_models.department_table import Department
from table_models.employee_table import Employee


try:
    sqlalchemy_client = SQLAlchemyClient()

    for table_model in [Department, Employee]:
        sqlalchemy_client.create_table(table_model)

    # Додавання департаментів та співробітників до бази даних
    it_department = Department(name='IT')
    hr_department = Department(name='HR')

    sqlalchemy_client.session.add_all([it_department, hr_department])
    sqlalchemy_client.session.commit()

    john = Employee(name='John', department_id=it_department.id)
    sqlalchemy_client.session.add(john)
    sqlalchemy_client.session.commit()




except Exception as e:
    sqlalchemy_client.close_connection()


