Certainly! Here's an updated README file for the Python Flask Contacts CRUD project, including information about Flask-SQLAlchemy, MySQL, and environment variables:

```
# Python Flask Contacts CRUD

This is a CRUD (Create, Read, Update, Delete) application built with Python Flask framework. It allows you to store contacts in a database and perform basic operations like viewing, editing, and deleting contacts.

## Features

- Create a new contact by providing the name, email, and phone number.
- View a list of all contacts stored in the database.
- Edit the details of an existing contact.
- Delete a contact from the database.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- Flask (version 1.1.2 or higher)
- Flask-SQLAlchemy (version 2.5.0 or higher)
- MySQL (version 5.7 or higher)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/DaveAdbeel/Python_Flask_Contacts_CRUD.git
   ```

2. Change into the project directory:

   ```shell
   cd Python_Flask_Contacts_CRUD
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

1. Rename the `.env.example` file to `.env`.

2. Open the `.env` file and configure the environment variables according to your setup:

   - `DATABASE_URI`: The URI of your MySQL database. Example: `mysql://username:password@hostname/database_name`

## Database Setup

1. Create a MySQL database for the project.

2. Update the `DATABASE_URI` in the `.env` file with your MySQL database connection details.

3. Run the database migrations to create the necessary tables:

   ```shell
   flask db upgrade
   ```

## Usage

1. Start the Flask development server:

   ```shell
   flask run
   ```

   The server should now be running at `http://localhost:5000`.

2. Open your web browser and navigate to `http://localhost:5000`.

3. You will see the homepage where you can perform different CRUD operations on contacts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the existing code style and conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by the need for a simple and straightforward contacts management system using Flask. Special thanks to the Flask community for their excellent documentation and resources.

## Contact

If you have any questions, feel free to reach out to the project author:

- Name: [Dave Adbeel](https://github.com/DaveAdbeel)
- Email: [dave.adbeel@example.com](mailto:dave.adbeel@example.com)

```

Feel free to customize the content and formatting based on your specific project requirements.
