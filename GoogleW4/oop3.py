class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        return self.current + 1
    def down(self):
        """Makes the elevator go down one floor."""
        return self.current - 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        return floor

elevator = Elevator(-1, 10, 0)

