bricks_number = int(input("Enter number of bricks in 3 digits: "))
print()
piglet_a = int(bricks_number / 100)
piglet_b = int((bricks_number % 100) / 10)
piglet_c = int((bricks_number % 100) % 10)

print(f"The first piglet picked up {piglet_a} bricks.")
print(f"The second piglet picked up {piglet_b} bricks.")
print(f"The third piglet picked up {piglet_c} bricks.")

leftover = (piglet_a + piglet_b + piglet_c) %3
print(leftover == 0)
