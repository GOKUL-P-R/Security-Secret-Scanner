import re

# Define patterns for sensitive data
patterns = {
    'API_KEY': r'AIza[0-9A-Za-z-_]{35}',
    'AWS_KEY': r'AKIA[0-9A-Z]{16}'
}

def scan_text(text):
    for name, pattern in patterns.items():
        if re.search(pattern, text):
            print(f"Alert: Found {name}!")

# Example: scan a string
test_code = "my_api_key = 'AIzaSyD-xYz1234567890123456789012345678'"
scan_text(test_code)
