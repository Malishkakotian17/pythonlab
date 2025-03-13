class RegistrationSystem:
    def __init__(self):
        self.registered_emails = set()

    def register_user(self, email):
        if email in self.registered_emails:
            return f"Error: {email} has already been registered."
        else:
            self.registered_emails.add(email)
            return f"Success: {email} has been registered."

# Example usage
reg_system = RegistrationSystem()
print(reg_system.register_user("user1@example.com"))  # Output: Success: user1@example.com has been registered.
print(reg_system.register_user("user2@example.com"))  # Output: Success: user2@example.com has been registered.
print(reg_system.register_user("user1@example.com"))  # Output: Error: user1@example.com has already been registered.