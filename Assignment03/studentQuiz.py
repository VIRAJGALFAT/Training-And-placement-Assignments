# Student registration with quiz and score logging

import random
import datetime

students = {}
current_user = None

quiz = [
  {"id": 1, "domain": "DSA", "question": "Given an array of integers, find the maximum subarray sum using Kadane's Algorithm.", "difficulty": "Medium", "topic": "Arrays", "answer": "kadane"},
  {"id": 2, "domain": "DSA", "question": "Implement a function to check whether a given linked list has a cycle.", "difficulty": "Medium", "topic": "Linked List", "answer": "fast slow pointer"},
  {"id": 3, "domain": "DSA", "question": "Write a program to reverse a binary tree.", "difficulty": "Medium", "topic": "Binary Tree", "answer": "recursion"},
  {"id": 4, "domain": "DSA", "question": "Find the nth Fibonacci number using Dynamic Programming.", "difficulty": "Easy", "topic": "Dynamic Programming", "answer": "dp"},
  {"id": 5, "domain": "DSA", "question": "Implement a stack using two queues.", "difficulty": "Hard", "topic": "Stacks and Queues", "answer": "queue"},
  {"id": 6, "domain": "SQL", "question": "Write a SQL query to find employees who earn more than the average salary.", "difficulty": "Medium", "topic": "Aggregate Functions", "answer": "avg"},
  {"id": 7, "domain": "SQL", "question": "Write a query to fetch the second-highest salary from the Employee table.", "difficulty": "Medium", "topic": "Subqueries", "answer": "limit offset"},
  {"id": 8, "domain": "SQL", "question": "Find the total number of customers who placed more than 3 orders in the last month.", "difficulty": "Hard", "topic": "Joins and Group By", "answer": "group by"},
  {"id": 9, "domain": "SQL", "question": "Display the department name and number of employees in each department.", "difficulty": "Easy", "topic": "GROUP BY", "answer": "group by"},
  {"id": 10, "domain": "SQL", "question": "Write a query to find duplicate email addresses in a Users table.", "difficulty": "Easy", "topic": "Aggregation and HAVING", "answer": "having"},
  {"id": 11, "domain": "Python", "question": "Write a Python function to check if a string is a palindrome.", "difficulty": "Easy", "topic": "Strings", "answer": "reverse"},
  {"id": 12, "domain": "Python", "question": "Write a Python program to find all unique elements in a list without using set().", "difficulty": "Medium", "topic": "Lists", "answer": "dict"},
  {"id": 13, "domain": "Python", "question": "Explain and demonstrate the difference between shallow copy and deep copy in Python.", "difficulty": "Medium", "topic": "Objects and Memory", "answer": "copy module"},
  {"id": 14, "domain": "Python", "question": "Write a Python program to implement a simple class named BankAccount with deposit and withdraw methods.", "difficulty": "Medium", "topic": "OOP", "answer": "class"},
  {"id": 15, "domain": "Python", "question": "Write a Python one-liner to flatten a list of lists.", "difficulty": "Hard", "topic": "List Comprehension", "answer": "list comprehension"}
]


def register():
    print("\n----- STUDENT REGISTRATION ----")
    username = input("Enter your username: ")
    if username in students:
        print("*** Username already exists! Choose another one. ***")
        return
    password = input("Enter your Password: ")
    name = input("Enter your name: ")
    roll_no = input("Enter your roll number: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    dob = input("Enter your date of birth: ")
    gender = input("Enter your gender: ")
    address = input("Enter your address: ")
    course = input("Enter your course (B.Tech/M.Tech): ")
    year = input("Enter your academic year: ")

    students[username] = {
        "password": password,
        "name": name,
        "roll_no": roll_no,
        "email": email,
        "phone": phone,
        "dob": dob,
        "gender": gender,
        "address": address,
        "course": course,
        "year": year
    }
    print("** Registration done successfully! **")


def login():
    global current_user
    print("\n--- LOGIN PAGE ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in students and students[username]["password"] == password:
        current_user = username
        print("=" * 60)
        print(f"Welcome {students[username]['name']}!\n")
    else:
        print("** Wrong username or password! **")


def show_profile():
    if current_user:
        print("\n--- PROFILE DETAILS ---")
        for key, value in students[current_user].items():
            if key != "password":
                print(f"{key.capitalize()}: {value}")
        print("=" * 60)
    else:
        print("Please login first!")


def update_profile():
    if current_user:
        print("--- UPDATE PROFILE ---")
        print("Fields you can update:")
        for key in students[current_user].keys():
            if key != "password":
                print(f"- {key}")
        field = input("Enter the field you want to update: ").lower()
        if field in students[current_user] and field != "password":
            new_value = input(f"Enter new value for {field}: ")
            students[current_user][field] = new_value
            print("=" * 60)
            print("Profile updated successfully!\n")
        else:
            print("Invalid field name!\n")
    else:
        print("Please login first!\n")


def logout():
    global current_user
    if current_user:
        print("=" * 60)
        print(f"{students[current_user]['name']} is logged out.")
        current_user = None
    else:
        print("No user is logged in.")


def quiz_section():
    if not current_user:
        print("You must login first to access the quiz section!\n")
        return

    print("\n=== QUIZ SECTION ===")
    total_marks = 0
    questions = random.sample(quiz, 5)  # randomly pick 5 questions

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. ({q['domain']}) {q['question']}")
        print(f"Difficulty: {q['difficulty']} | Topic: {q['topic']}")
        ans = input("Your answer: ").strip().lower()

        if ans in q["answer"].lower():
            print("✔ Correct!")
            total_marks += 1
        else:
            print(f"✘ Wrong! Correct hint: {q['answer']}")

    print("\nQuiz Completed!")
    print(f"Your Score: {total_marks}/5")

    now = datetime.datetime.now()
    with open("quiz_results.txt", "a") as f:
        f.write(f"User: {current_user}, Score: {total_marks}/5, Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

    print("Your result has been saved!\n")


def main():
    while True:
        print("\n=== Student Registration System ===")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Take Quiz (Login Required)")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            quiz_section()
        elif choice == "6":
            logout()
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
             
