### Time Tracking Tool for university project

## to install all requirements run:

```
python3 -m venv venv

python3 -m pip install -r requirements.txt
```

## to create all users for your database

1. Run

```
python3 manage.py runserver
```

once to create a database.

2. Quit the process and run:

```
python3 manage.py shell

from app import db
from app.models import User, Role

employee_role = Role(name = 'employee')
supervisor_role = Role(name = 'supervisor')
hr_role = Role(name = 'hr')

user_test_1 = User(email = 'employee@gmail.com', password = 'password', full_name = 'Max Mustermann', role=employee_role)
user_test_2 = User(email = 'chef@gmail.com', password = 'password', full_name = 'John Doe', role=supervisor_role)
user_test_3 = User(email = 'hr@gmail.com', password = 'password', full_name = 'Anita John', role=hr_role)

db.session.add_all([employee_role, supervisor_role, hr_role, user_test_1, user_test_2,user_test_3])
db.session.commit()
```

3. After that you can quit the shell by running

```
quit()
```
