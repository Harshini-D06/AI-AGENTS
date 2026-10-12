# ==============================
# TRAVEL AGENT MEMORY
# ==============================

class TravelMemory:

    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        """Store information in memory."""
        self.memory[key] = value

    def get(self, key):
        """Retrieve information from memory."""
        return self.memory.get(key)

    def show_memory(self):
        """Display stored information."""

        print("\n🧠 AGENT MEMORY")
        print("-" * 40)

        if not self.memory:
            print("Memory is empty.")
            return

        for key, value in self.memory.items():
            print(f"{key}: {value}")