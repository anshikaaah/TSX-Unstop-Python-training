from flask import Flask, render_template, request, flash, redirect, url_for
import os
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic form validation
        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))
        
        # Validate email format
        try:
            validate_email(email)
        except EmailNotValidError:
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('contact'))
        
        # In a production environment, you would send the email here
        # For now, we'll just show a success message
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 