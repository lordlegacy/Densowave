# M-Pesa STK Push Webapp

This is a Flask-based web application that allows users to send M-Pesa STK (SIM Tool Kit) push requests. Users can sign up, log in, register their businesses, and initiate STK push requests for both Paybill and Buy Goods and Services transactions.

## Features

- User Authentication (Signup and Login)
- JWT-based session management
- Business Registration
- M-Pesa STK Push initiation
- Support for Paybill and Buy Goods and Services transactions

## Tech Stack

- Backend: Python with Flask
- Frontend: HTML, CSS, JavaScript (jQuery)
- Database: SQLAlchemy (ORM)
- Authentication: JWT (JSON Web Tokens)
- API: M-Pesa API integration

## Project Structure

```
/
├── __pycache__/
├── src/
│   ├── dashboard.html
│   ├── login.html
│   ├── signup.html
│   └── styles.css
├── __init__.py
├── config.py
├── extensions.py
├── models.py
├── OAuth.py
├── qr.py
├── routes.py
└── stk_push.py
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/lordlegacy/Densowave.git
   cd densowave
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   CONSUMER_KEY=your_mpesa_consumer_key
   CONSUMER_SECRET=your_mpesa_consumer_secret
   PASSKEY=your_mpesa_passkey
   ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   python app.py
   ```

7. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Sign up for a new account or log in if you already have one.
2. Once logged in, you'll be directed to the dashboard.
3. Register your business by providing the required details.
4. Initiate an M-Pesa STK push by filling out the transaction form.

## API Endpoints

- `/auth/register` - User registration
- `/auth/login` - User login
- `/auth/refresh` - Refresh JWT token
- `/business/register` - Register a new business
- `/business/view` - View registered business information
- `/business/update` - Update business information
- `/stk_push/stk` - Initiate M-Pesa STK push

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [M-Pesa API](https://developer.safaricom.co.ke/)

