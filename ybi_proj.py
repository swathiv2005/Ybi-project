import pandas as pd
import random

# Sample train data
train_data = {
    "Train": ["Shatabdi Express", "Rajdhani Express", "Garib Rath", "Duronto Express"],
    "Sleeper Seats": [150, 100, 200, 120],
    "AC Seats": [50, 60, 75, 40],
    "Sleeper Price": [500, 700, 300, 600],
    "AC Price": [1200, 1500, 800, 1000]
}

trains = pd.DataFrame(train_data)

# Function to check seat availability
def check_availability(train, class_type, num_seats):
    if train in trains["Train"].values:
        index = trains[trains["Train"] == train].index[0]
        if class_type == "Sleeper" and trains.loc[index, "Sleeper Seats"] >= num_seats:
            return True
        else:
            return False
        if class_type == "AC" and trains.loc[index, "AC Seats"] >= num_seats:
            return True
        else:
            return False
    else:
        print("Train not found.")
        return False

# Function to book tickets
def book_tickets(train, class_type, num_seats):
    if check_availability(train, class_type, num_seats):
        index = trains[trains["Train"] == train].index[0]
        if class_type == "Sleeper":
            trains.loc[index, "Sleeper Seats"] -= num_seats
            price = trains.loc[index, "Sleeper Price"]
        elif class_type == "AC":
            trains.loc[index, "AC Seats"] -= num_seats
            total_price = trains.loc[index, "AC Price"]
        pnr_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))  # Generate a random PNR
        print(f"Tickets booked successfully!")
        print(f"PNR Number: {pnr_number}")
        print(f"Total Fare: {price * num_seats}")
    else:
        print("Booking failed. Seats not available.")

# Example usage
book_tickets("Rajdhani Express", "Sleeper", 5)
print(trains)
