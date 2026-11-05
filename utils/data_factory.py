from faker import Faker
fake = Faker()

def invalid_email(): return f"unknown_{fake.uuid4()}@example.invalid"
