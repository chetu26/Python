import pickle
import csv

def create_hospitals_list():
    num_hospitals = int(input("Enter the number of hospitals: "))
    hospitals = []

    for i in range(num_hospitals):
        print(f"\nHospital {i+1}")
        name = input("Enter the hospital name: ")
        location = input("Enter the hospital location: ")
        capacity = int(input("Enter the hospital capacity: "))

        hospital = {
            "name": name,
            "location": location,
            "capacity": capacity
        }

        hospitals.append(hospital)

    return hospitals

def save_to_pickle(hospitals, filename):
    with open(filename, 'wb') as file:
        pickle.dump(hospitals, file)
    print("Data saved to pickle successfully!")

def load_from_pickle(filename):
    with open(filename, 'rb') as file:
        hospitals = pickle.load(file)
    return hospitals

def save_to_csv(hospitals, filename):
    fieldnames = ['Name', 'Location', 'Capacity']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(hospitals)

    print("Data saved to CSV successfully!")

# Step 1: Create hospitals list
hospitals_list = create_hospitals_list()

# Step 2: Save to pickle
pickle_filename = "hospitals.pickle"
save_to_pickle(hospitals_list, pickle_filename)

# Step 3: Load from pickle
loaded_hospitals = load_from_pickle(pickle_filename)

# Step 4: Save to CSV
csv_filename = "hospitals.csv"
save_to_csv(loaded_hospitals, csv_filename)
