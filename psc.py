import re

def check_password_strength(password):
    suggestions = []
    strength = "Weak"

    # Check length
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")

    # Check for character variety
    if not re.search(r"[a-z]", password):
        suggestions.append("Include lowercase letters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include uppercase letters.")
    if not re.search(r"\d", password):
        suggestions.append("Include numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include special characters.")

    # Check common passwords
    with open("checker/common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
    if password in common_passwords:
        suggestions.append("Avoid using common passwords.")

    # Determine strength
    if len(password) >= 8 and len(suggestions) == 0:
        strength = "Strong"
    elif len(password) >= 8 and len(suggestions) <= 2:
        strength = "Moderate"

    return strength, suggestions
