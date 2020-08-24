# Bank System

Bank system is a project, that simulates a basic implementation of user panel in bank, without any GUI, just a simple backend code. The goal was to learn how to use objective programming, MySQL and Cryptography libaries in Python.

## Installation

First of all, clone the repository into the desired folder

```bash
git clone https://github.com/hoopdead/bank_system
```

Then install virtualenv, and install all of the libaries included in project

```bash
virtualenv env
```

Third thing is to set a database (MySQL)

```bash
python3 main_server.py
```

Fourth, and last thing, to use client side:

``` bash
python3 main_client.py
```


Make sure, that your MySQL service is running!
The Following code have been tested on Ubuntu 18.07.

## Description of all the classes and functions:

Folder Init:

    database_creator.py:

        Class Creator handles multiple methods - 
            _connection - connects to database
            create_db - create database clients
            create_client_table - create accounts table

    database_checker.py:

        Class CheckerClass inherits from CreatorClass - the only reason for that is _connection method is passed -
            check_if_database_exists - checks, if database exists
            check_if_table_exists - check, if table exists
            check_if_accounts_in_table_exists - check, if there's any account in table

    user.py:

        Class UserClass handles information about user, his action and active choices -
            constructor - takes argument about list of choices, that user CAN and CANNOT choose, and what login_number for bank does user have
            introduction - print some information about program
            display_choices - display choices, that user can make
            check_active_choices - check from INPUT what choices are active right now
            get_account_number - opens connection with database and check, what account number in bank does user have
            update_username - function, that updates class with new username
            get_username - function, that returns username

    transaction.py:

        Class UserTransaction handles all operations allowed for user in bank, including passing money to someone, or check contact list -
            constructor - nothing here 
            check_contact_list - return a list of all persons registered in bank, that function is temporary and made just for simplify the process of passing money for tests :)
            make_transaction - passing money from your pocket, to other user.

    balance.py:
    
        Class UserBalance is created for all operations connected with your account balance, like checking balance, adding it, etc -
            constructor - takes your login number, made for mysql statements
            get_account_balance - get how much money is on your account
            get_account_balance_by_account_number - get how much money there's on account with given account number
            add_account_balance - function made for tests - you can add as much money, as you can

Folder automation:

    create_some_accounts.py:

        Class inherits from Creator, the only reason is that _connection method is passed
        Class AccountCreatorAutomat:
        Class handles multiple methods - 
            create_multiple_accounts - function to fill the accounts table with random data for testing

client.py:

Folder Auth:

    password_encrypt.py:

        AuthenticationPasswordEncrypterClass have information about password encryption and decryption - 
            constructor - take nothing, just set secret_key to zero bytes
            set_secret_key - set secret_key from json file
            password_encode - encoding given password with secret key
            password_decode - decodeing given password with secret key

        login.py:

        UserLoginClass have all function connented with login auth system - 
            constructor - login, and password
            get_password_from_db - get password from database with given username from constructor,
            get_username - returns your username
            login - function just logs you in, with given login and password in constructor

        register.py:

            UserRegisterClass have all function conneted with register auth system - 
                constructor - firstname, surname, password, country, city, street_name, home number
                fetch_login_numbers - check what login numbers are already in db
                fetch_account_numbers - check what acc numbers are already in db
                fetch_credit_card_numbers - check what credit card numbers are in db
                get_login_number - return new login number for new account
                get_account_number - retun new account number for new account
                get_credit_card_number - return credit card number for new acc
                register - register your new account



Folder sockets:

    client.py:

        ClientClass - handles information about socket client -
            send - send message to server - ENCODING - utf-8

    server.py:

        ServerClass - handles information about socket server -
            constructor - takes addr and server information
            handle_client - function for handle client connection
            start - starts the socket server


## License
[MIT](https://choosealicense.com/licenses/mit/)