import re

def extract_number(text):
    # Use regular expression to extract all digits
    numbers = re.findall(r'\d+', text)
    
    if numbers:
        # Combine the first number on the left and right
        combined = int(numbers[0] + numbers[-1])
        return combined
    return 0

total_sum = 0

try:
    with open('document.txt', 'r') as file:
        # Loop through each line in the file
        for line in file:
            line = line.strip()  # Remove any extra spaces/newlines
            total_sum += extract_number(line)
    
    print(f"The total sum is: {total_sum}")

except FileNotFoundError:
    print("The file 'document.txt' was not found.")
