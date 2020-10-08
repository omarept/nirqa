class Piglet:
    """Represents a piglet that can say their name."""
    years = 2
    name = "Mike"
    def speak(self):
        """Outputs a message including the name of the Piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18

a = Piglet()
b = Piglet()

print(a.speak())
print(b.pig_years())