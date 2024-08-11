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