#question11
class Student:

    # Constructor
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for marks
    def get_marks(self):
        return self.__marks

    # Setter for marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

    # Display method
    def display(self):
        print("Student Name:", self.__name)
        print("Student Marks:", self.__marks)


# Creating an object
s1 = Student("Ishika", 90)

# Display original details
print("Original Details:")
s1.display()

# Updating details using setters
s1.set_name("Ishika Singh")
s1.set_marks(95)

# Display updated details
print("\nUpdated Details:")
s1.display()

#12

try:

    # Open the file in read mode
    with open("students.txt", "r") as file:

        content = file.read()

        # Count lines
        lines = content.splitlines()

        # Count words
        words = content.split()

        print("File Content:")
        print(content)

        print("Total Lines:", len(lines))
        print("Total Words:", len(words))

except FileNotFoundError:
    print("Error: students.txt file not found!")

except Exception as e:
    print("An error occurred:", e)

