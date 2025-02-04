from flask import Flask, render_template, request
import re

app = Flask(__name__)

def password_checker(password):
    """
    Checks the strength of a password based on:
      - Minimum length of 8 characters
      - Presence of uppercase letters
      - Presence of lowercase letters
      - Presence of digits
      - Presence of special characters
    Returns a rating ("Weak", "Moderate", "Strong") and a list of feedback messages.
    """
    strength = 0
    messages = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        messages.append("Password must be at least 8 characters long.")

    # Check for uppercase letter
    if re.search("[A-Z]", password):
        strength += 1
    else:
        messages.append("Password must contain at least one uppercase letter.")

    # Check for lowercase letter
    if re.search("[a-z]", password):
        strength += 1
    else:
        messages.append("Password must contain at least one lowercase letter.")

    # Check for digit
    if re.search("[0-9]", password):
        strength += 1
    else:
        messages.append("Password must contain at least one digit.")

    # Check for special character
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        messages.append("Password must contain at least one special character (!@#$%^&*).")

    # Determine the password rating
    if strength <= 2:
        rating = "Weak"
    elif strength in [3, 4]:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, messages

@app.route("/", methods=["GET", "POST"])
def index():
    rating = None
    messages = []
    if request.method == "POST":
        password = request.form.get("password")
        rating, messages = password_checker(password)
    return render_template("index.html", rating=rating, messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
