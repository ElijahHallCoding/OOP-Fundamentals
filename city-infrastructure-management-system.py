# Task 1: Vehicle Registration System

# Vehicle class with attributes for registration number, type, and owner
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")

# Instances of Vehicle and updating the owner

# Vehicle instances
vehicle1 = Vehicle("ABC123", "Car", "Elijah Hall")
vehicle2 = Vehicle("XYZ789", "Truck", "Anthony Milton")

# Print the initial owner details
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Update owner of vehicle1
vehicle1.update_owner("Craig Lewis")

# Update owner of vehicle2
vehicle2.update_owner("Bob Williams")

# Updated owner details
print(f"Updated Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Updated Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Task 2: Event Management System Enhancement

# Event class with attributes for name and date
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize the participant count to 0

    # Step 2: Implement a method to add a participant
    def add_participant(self):
        self.participant_count += 1
        print(f"Added a participant. Total participants: {self.participant_count}")

    # Step 3: Implement a method to get the current participant count
    def get_participant_count(self):
        return self.participant_count

# Event instance and managing participants

# Creating an event instance
event1 = Event("City Marathon", "2024-09-15")

# Print participant count
print(f"Event: {event1.name} on {event1.date} has {event1.get_participant_count()} participants.")

# Add participants
event1.add_participant()
event1.add_participant()

# Print the updated participant count
print(f"Updated Event: {event1.name} on {event1.date} now has {event1.get_participant_count()} participants.")

