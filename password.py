import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password. Consider strengthening it.", feedback
    else:
        return "Weak password. Try to improve it.", feedback

password = input("Enter your password: ")

strength_message, suggestions = assess_password_strength(password)

print(f"Password Strength: {strength_message}")
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

