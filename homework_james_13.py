# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 4 Lesson 2 Assignment: OOP Fundamentals

import datetime

print("\n    === 1.1 Vehicle Registration System ===\n")

class Vehicle:
    def __init__(self, reg_num, type_, owner):
        self.registration_number = reg_num
        self.type_ = type_
        self.owner = owner

    def update_owner(self, new_owner):
        old_owner = self.owner
        self.owner = new_owner
        print(f"Ownership for {self.type_} {self.registration_number} has changed from {old_owner} to {new_owner}.")

# I cannot vouch for the historical accuracy of this account, but here are some cars and presidents I found on Wikipedia.
# The views and policies of these presidents do not represent those of the programmer.
car_lincoln = Vehicle("111188", "Lincoln Continental", "Gerald Ford")
car_lincoln.update_owner("Jimmy Carter")
car_lincoln.update_owner("Ronald_Reagan")
car_cadillac = Vehicle("040495", "Cadillac Fleetwood", "Ronald Reagan")
car_cadillac.update_owner("George H.W. Bush")



print("\n    === 1.2 Event Management System Enhancement ===\n")
'''
Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of 
participants. Implement a method add_participant that increases the count and a method get_participant_count 
to retrieve the current count.

Code Example: Basic Event class without participant tracking.
'''

class Event:
    def __init__(self, name, date, attendance):
        self.name = name
        self.date = date
        self.attendance = attendance

    def add_participant(self, count=1):
        self.attendance += count

    def get_participant_count(self):
        return self.attendance
    
weekend_event = Event("Scrapbooking Retreat", datetime.datetime(2024, 4, 5), 38)
weekend_event.add_participant()
print(f"{weekend_event.get_participant_count()} people are coming to the {weekend_event.name}!")
weekend_event.add_participant(3)
print(f"{weekend_event.get_participant_count()} people are coming to the {weekend_event.name}!")