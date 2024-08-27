# Age Verification Program

This project is a simple Python script designed to verify the age of a user and determine if they are allowed entry based on age restrictions. The program uses basic input handling and error management to ensure that only users aged 18 or older are allowed.

## Features

- Prompts the user to enter their age.
- Checks if the entered age meets the minimum age requirement of 18.
- Raises a `ValueError` with a custom message if the age is below 18.
- Displays a message to inform the user whether they are allowed to enter based on their age.

## How It Works

1. **User Input**: The script asks the user to input their age.
2. **Age Verification**: 
   - If the user's age is 18 or above, the program allows entry and prints "Allowed to enter."
   - If the user's age is below 18, the program raises a `ValueError` with the message "18+ Adults only" and prints the error message.

## Code Explanation

```python
def positive_num(num):
    if num < 18:
        raise ValueError("18+ Adults only")
    else:
        return num

num = int(input("Enter your age: "))

try:
    positive_num(num)
    print('Allowed to enter')
except ValueError as e:
    print(e)
```

### Functions

- **`positive_num(num)`**: 
  - Takes an integer `num` (age) as input.
  - Raises a `ValueError` if the age is less than 18.
  - Returns the age if the age is 18 or older.

### Error Handling

- The script uses a `try-except` block to handle exceptions.
- If a `ValueError` is raised, the program catches it and prints the error message, preventing the program from crashing.

## How to Run

1. Make sure you have Python installed on your system.
2. Clone or download the repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using Python:

   ```bash
   python main.py
   ```

5. Enter your age when prompted.

## Example Usage

```bash
$ python age_verification.py
Enter your age: 17
18+ Adults only

$ python age_verification.py
Enter your age: 20
Allowed to enter
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.