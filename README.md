# RANDOM PASSWORD GENERATOR USING PYTHON

### 1. Introduction

The Random Password Generator is a Python project that creates strong and random passwords. It allows users to choose the password length and select lowercase letters, uppercase letters, numbers, and special characters.

### 2. Objective

The main objective is to generate secure passwords easily and reduce the use of weak or predictable passwords.

### 3. Technologies Used

* **Language:** Python
* **Modules:** `secrets`, `string`, `math`
* **File:** `passwords.txt`

### 4. Working

The program first asks the user for the password length and character types. It generates at least one character from each selected category and fills the remaining positions randomly. The characters are then shuffled to create the final password.

The program also calculates an approximate entropy value and classifies the password as **Weak, Medium, Strong, or Very Strong**.

### 5. Main Features

* Custom password length (4–128 characters)
* Lowercase and uppercase letters
* Numbers and special characters
* Multiple password generation
* Password strength checking
* Save passwords to a text file
* Input validation

### 6. Advantages

The project is simple, fast, easy to use, and does not require external libraries. It uses Python's `secrets` module, which is suitable for generating security-related random values.

### 7. Limitations

The program uses a command-line interface and saves passwords as plain text when the user chooses the save option. The strength calculation is only an approximate estimate.

### 8. Future Scope

A graphical interface, clipboard copy option, better password analysis, and secure password-manager integration can be added in the future.

### 9. Conclusion

This project demonstrates how Python can be used to create a practical password-generation tool. It helped in understanding functions, loops, conditional statements, input validation, file handling, random generation, and basic password-strength calculation.
