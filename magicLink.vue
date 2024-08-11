Frontend (Vue) Code
Create a Vue component for the login page:
HTML
<template>
  <div>
    <input type="email" v-model="email" placeholder="Email">
    <button @click="sendMagicLink">Send Magic Link</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: ''
    }
  },
  methods: {
    sendMagicLink() {
      axios.post('/magic-link', { email: this.email })
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
Flask Server-Side Code
Create a Flask route to handle the magic link request:
Python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'
mail = Mail(app)

@app.route('/magic-link', methods=['POST'])
def send_magic_link():
    email = request.json['email']
    # Generate a magic link token
    token = secrets.token_urlsafe(16)
    # Store the token in the database
    db = get_db()
    db.execute('INSERT INTO magic_links (email, token) VALUES (?, ?)', (email, token))
    db.commit()
    # Send the magic link email
    msg = Message('Magic Link', sender='your-email@gmail.com', recipients=[email])
    msg.body = f'Click this link to log in: http://example.com/login/{token}'
    mail.send(msg)
    return jsonify({'message': 'Magic link sent'})
Login Route
Create a Flask route to handle the magic link login:
Python
@app.route('/login/<token>', methods=['GET'])
def login(token):
    # Verify the token
    db = get_db()
    cursor = db.execute('SELECT email FROM magic_links WHERE token = ?', (token,))
    email = cursor.fetchone()
    if email:
        # Log the user in
        login_user(email)
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'error': 'Invalid token'}), 401
This is a basic example to get you started. You'll need to modify the code to fit your specific use case and implement additional security measures.