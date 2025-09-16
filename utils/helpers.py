def validate_email(email):
    return "@" in email and "." in email.split("@")[1]

def format_name(name):
    return name.title().strip()

def calculate_fine(days_late):
    return days_late * 2 