
```
# Python Flask Contacts CRUD

This is a CRUD (Create, Read, Update, Delete) application built with Python Flask framework. 
It allows you to store contacts in a database and perform basic operations like viewing, editing, and deleting contacts.

## Features

- Create a new contact by providing the fullname, email, and phone number.
- View a list of all contacts stored in the database.
- Edit the details of an existing contact.
- Delete a contact from the database.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.6 or higher)

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

- Open the `.env` file and configure the environment variables according to your setup:

   . `DATABASE_CONNECTION_URI`: The URI of your MySQL database. Example: `mysql://MYSQL_USER:MYSQL_PASSWORD@MYSQL_HOST/MYSQL_DATABASE`

## Database Setup

1. Create a MySQL database for the project.

2. Update the variables `MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE` in the `.env` file with your MySQL database connection details.

3. Also update the `SECRET_KEY` variable which is also in the `env` file, for security reasons


## Usage

1. Start the Flask development server:

   ```shell
   python3 index.py
   ```

   The server should now be running at `http://localhost:5000`.

2. Open your web browser and navigate to `http://localhost:5000`.

3. You will see the homepage where you can perform different CRUD operations on contacts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an 
issue or submit a pull request. Make sure to follow the existing code style and conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to [Fazt's course: Flask SQLAlchemy CRUD con MySQL](https://www.youtube.com/watch?v=BP3D03CYFHA), 
I learned much more about flask and how to exchange data to databases with Flask SQLAlchemy

## Contact

If you have any questions, feel free to reach out to the project author:

- Name: [Dave Adbeel](https://github.com/DaveAdbeel)
- Email: [davidadbeelgonzalez@gmail.com](mailto:davidadbeelgonzalez@gmail.com)

