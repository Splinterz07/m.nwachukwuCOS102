# Define student data
students = [
    ["Evelyn", 17, 5.5, 80], ["Jessica", 16, 6.0, 85], ["Somto", 17, 5.4, 70],
    ["Edith", 18, 5.9, 60], ["Liza", 17, 5.5, 76], ["Madonna", 20, 6.1, 66],
    ["Waje", 19, 6.0, 87], ["Tola", 17, 5.7, 95], ["Aisha", 17, 5.5, 50],
    ["Latifa", 17, 5.5, 49],

    ["Chinedu", 19, 5.7, 74], ["Liam", 16, 5.9, 87], ["Wale", 18, 5.8, 75],
    ["Gbenga", 17, 6.1, 68], ["Abiola", 20, 5.9, 66], ["Kola", 19, 5.5, 78],
    ["Kunle", 16, 6.1, 87], ["George", 18, 5.4, 98], ["Thomas", 17, 5.8, 54],
    ["Wesley", 19, 5.7, 60]
]

# Print table header
print("Name       | Age | Height | Score")
print("--------------------------------")

# Print student data in a table format
for student in students:
    name, age, height, score = student
    print(f"{name} | {age} | {height} | {score}")