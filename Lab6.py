import random

class Parent:
    def __init__(self, gene1, gene2):
        self.gene1 = gene1
        self.gene2 = gene2

class Child:
    def __init__(self, parent1, parent2):
        self.gene1 = random.choice([parent1.gene1, parent1.gene2])
        self.gene2 = random.choice([parent2.gene1, parent2.gene2])
        self.eye_color = self.determine_eye_color()

    def determine_eye_color(self):
        if 'brown' in [self.gene1, self.gene2]:
            return 'brown'
        else:
            return 'blue'

# Input genes for parents
p1_gene1 = input("Please enter gene 1 of parent 1: ")
p1_gene2 = input("Please enter gene 2 of parent 1: ")
p2_gene1 = input("Please enter gene 1 of parent 2: ")
p2_gene2 = input("Please enter gene 2 of parent 2: ")


# Create Parent objects
p1 = Parent(p1_gene1, p1_gene2)
p2 = Parent(p2_gene1, p2_gene2)

# Create Child object
c = Child(p1, p2)

# Output genes and eye color
print("Parent 1 genes:", p1.gene1, p1.gene2)
print("Parent 2 genes:", p2.gene1, p2.gene2)
print("Child gene 1:", c.gene1)
print("Child gene 2:", c.gene2)
print("Child eye color:", c.eye_color)
