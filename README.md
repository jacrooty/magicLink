# Magic Link Authentication System
## Overview
This system provides a magic link-based authentication solution using Flask and Vue.js. It allows users to log in without remembering a password, improving the user experience and reducing password-related issues.
Features
Email-based magic link authentication
* Passwordless login
* User data storage in a database
* Secure token generation and verification
* Vue.js frontend for a seamless user experience
* Flask backend for server-side logic and database integration
## Getting Started
Clone the repository: git clone https://github.com/your-username/magic-link-auth.git
Install dependencies: pip install -r requirements.txt (Flask) and npm install (Vue.js)
Set up your database: configure the SQLALCHEMY_DATABASE_URI variable in app.py
Run the Flask server: flask run
Run the Vue.js frontend: npm run serve
## Usage
Users enter their email address on the login page.
The system generates a magic link and sends it to the user's email address.
Users click on the magic link to log in.
The system verifies the token and logs the user in.
### Security Considerations
* Tokens are generated using the secrets library and are stored securely in the database.
* Tokens are verified on each login attempt to prevent token reuse.
* User data is stored securely in the database using best practices.
## Contributing
Contributions are welcome! Please submit pull requests or open issues on GitHub.
License
This project is licensed under the MIT License. See LICENSE for details.
Acknowledgments
This project was inspired by the magic link authentication pattern and built using Flask and Vue.js.
