# Tasky - Task Management Application

Tasky is a web-based task management application built with Django and Tailwind CSS.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.8 or later
* You have installed pip (Python package manager)
* You have a Windows/Linux/Mac machine

## Setting up Tasky

To set up Tasky, follow these steps:

1. Clone the repository:

2. Create a virtual environment:

 python -m venv env

3. Activate the virtual environment:
- On Windows:
  ```
  .\env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source env/bin/activate
  ```

4. Install the required dependencies:

5. Run database migrations:
python manage.py migrate

6. Create a superuser (admin) account:
python manage.py createsuperuser

## Running Tasky

To run Tasky, follow these steps:

1. Make sure your virtual environment is activated.

2. Start the Django development server:
python manage.py runserver


3. Open a web browser and navigate to `http://127.0.0.1:8000/`

4. To access the admin interface, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## Using Tasky

- Create new tasks by clicking on the "Create Task" button.
- View, edit, and delete tasks using the icons next to each task.
- Use the search bar to find specific tasks.
- Sort tasks by due date, priority, or status using the sorting buttons.

## Contributing to Tasky

To contribute to Tasky, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact me, you can reach me at `nbaronjekeko33@gmail.com`.

