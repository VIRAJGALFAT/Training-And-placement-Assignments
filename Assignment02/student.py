#Student registration

students ={}
current_user = None

def register():
    print("\n-----STUDENT REGISTRATION----")
    username = input("Enter your username: ")
    if username in students:
        print("***This is username is present! choose other one**")
        return
    password = input("Enter your Password: ")
    name = input("Enter your name: ")
    roll_no = input("Enter your roll_no:")
    email = input("Enter your email: ")
    phone = input("Enter your phone Number: ")
    Dob = input("Enter yout DoB: ")
    Gender = input("Enter your Gender: ")
    address = input("Enter your address")
    course = input("Enter your course -b.tech/M.tech: ")
    year = input("Enter your academic: ")

    students[username] = {
    
        "password": password,
        "name": name,
        "roll_no": roll_no,
        "email": email,
        "phone": phone,
        "dob": Dob,
        "gender": Gender,
        "address": address,
        "course": course,
        "year": year

    }
    print("**Registration done**")

def login():
    global current_user
    print("\n ---LOGIN PAGE---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in students and students[username]["password"] == password:
        current_user = username
        print("="*60)
        print(f"Welcome {students[username]['name']}!\n")
    else:
        print("**wrong username or password**")
    
def show_profile():
    if current_user:
        print("\n---PROFILE-DETAILS---")
        for key,value in students[current_user].items():
            if key != "password":
                print(f"{key.capitalize()}:{value}")
            print()
            print("="*60)
    else:
        print("Please login first!")

def update_profile():
    if current_user:
        print("---UPDATE-PROFILE---")
        print("\n--- UPDATE PROFILE ---")
        print("Fields you can update:")
        for key in students[current_user].keys():
            if key != "password":
                print(f"- {key}")

        field = input("Enter the field you want to update: ").lower()
        if field in students[current_user] and field != "password":
            new_value = input(f"Enter new value for {field}: ")
            students[current_user][field] = new_value
            print("="*60)
            print("Profile updated successfully!\n")
        else:
            print("Invalid field name!\n")
    else:
        print("Please login first!\n")
    

def logout():
    global current_user
    if current_user:
        print("="*60)
        print(f"{students[current_user]['name']} is logged out")
        current_user = None
    else:
        print("No user is logged in")
    
def main():
    while True:
        print("=== Student Registration System ===")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Exit")
        
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
            logout()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print(" Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()

