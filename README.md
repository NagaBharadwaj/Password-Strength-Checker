# Password-Strength-Checker
```markdown
# Password Strength Checker

## Overview
"Password Strength Checker" is a Python-based application that evaluates the strength of passwords based on multiple criteria, including length, character variety, and the presence of common patterns.

## Features
- Evaluates password strength on a scale of weak, moderate, or strong.
- Provides suggestions for improving weak passwords.
- Checks against a list of commonly used passwords.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Password-Strength-Checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Password-Strength-Checker
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter a password to evaluate its strength.

## Technologies Used
- **Python**
- **Regex** for pattern matching.
- **Common password dataset** for enhanced security.

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License.
```

## Sample Python Files

### main.py
```python
from checker.strength_checker import check_password_strength

def main():
    print("Welcome to Password Strength Checker!")
    password = input("Enter a password to check its strength: ")
    strength, suggestions = check_password_strength(password)

    print(f"Password Strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
```

### checker/strength_checker.py
```python
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
```


