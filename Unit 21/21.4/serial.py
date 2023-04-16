"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start):
        """Initialize the Serial Number Generator"""
        self.start = self.next = start

    def __repr__(self):
        """Representation method"""
        return f"<SerialGenerator: Start = {self.start}, Next = {self.next}>"
    
    def reset(self):
        """Resets the current number to original one"""
        self.next = self.start
    
    def generate(self):
        """Returns the number increased by one"""
        self.next += 1
        return self.next - 1
