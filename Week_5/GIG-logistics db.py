import pandas as pd
import random

names = [
    "Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Evans", "Ethan Wright",
    "Fiona Brown", "George Clark", "Hannah Lewis", "Ian Walker", "Jane Hall",
    "Kevin Allen", "Laura Young", "Michael King", "Nina Scott", "Oscar Adams",
    "Paula Mitchell", "Quincy Turner", "Rachel Cooper", "Steve Morgan", "Tina Reed",
    "Uma Gray", "Victor Bell", "Wendy Green", "Xander White", "Yara Hill",
    "Zack Ward", "Aaron Brooks", "Bella Flores", "Caleb Hayes", "Daisy Price",
    "Elijah Foster", "Faith Simmons", "Gavin Peterson", "Hailey Coleman", "Isaac Perry",
    "Jasmine Hughes", "Kyle Ross", "Lily Patterson", "Mason Griffin", "Natalie Powell"
]

departments = ["Logistics", "HR", "Finance", "IT", "Operations", "Customer Support"]

# Generate 40 entries
data = {
    "Name": names[:40],
    "Department": [random.choice(departments) for _ in range(40)]
}

df = pd.DataFrame(data)
df.to_csv("GIG-logistics.csv", index=False)

print("✅ 'GIG-logistics.csv' has been generated with 40 employees.")
