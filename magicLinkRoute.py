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