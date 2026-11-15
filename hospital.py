def add_patient(patients):
    name = input("Name: ")
    if not name.strip():
        print("Name cannot be empty.")
        return
    
    try:
        age = int(input("Age: "))
        if age < 0 or age > 120:
            print("Invalid age. Enter a number between 0 and 120. Patient not added.")
            return
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120. Patient not added.")
        return
        
    disease = input("Disease: ")
    doctor = input("Doctor: ")
    
    # Patient IDs start from P101 and increase by 1
    pid = f"P10{len(patients) + 1}"
    patients[pid] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }
    print(f"Patient added. ID: {pid} | {name} | {age} | {disease} | {doctor}")

def view_all(patients):
    if not patients:
        print("No patient records found.")
        return
    for pid, p in patients.items():
        print(f"ID: {pid} | {p['Name']} | {p['Age']} | {p['Disease']} | {p['Doctor']}")

def search_patient(patients):
    pid = input("Enter Patient ID: ").strip()
    if pid in patients:
        p = patients[pid]
        print(f"ID: {pid} | {p['Name']} | {p['Age']} | {p['Disease']} | {p['Doctor']}")
    else:
        print("No patient records found.")

def update_patient(patients):
    pid = input("Enter Patient ID: ").strip()
    if pid in patients:
        new_disease = input("Enter new disease: ")
        patients[pid]['Disease'] = new_disease
        print(f"(a) Patient {pid} updated. Disease: {new_disease}")
    else:
        print("No patient records found.")

def delete_patient(patients):
    pid = input("Enter Patient ID: ").strip()
    if pid in patients:
        del patients[pid]
        print(f"(b) Patient {pid} deleted. Total patients: {len(patients)}")
    else:
        print("No patient records found.")

def main():
    patients = {} 
    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1. Menu option 1 (Add)")
        print("2. Menu option 2 (View all)")
        print("3. Menu option 3 (Search by ID)")
        print("4. Menu option 4 (Update)")
        print("5. Menu option 5 (Delete)")
        print("6. Exit")
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            view_all(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            update_patient(patients)
        elif choice == '5':
            delete_patient(patients)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()