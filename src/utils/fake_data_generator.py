# src/utils/fake_data_generator.py
from faker import Faker
fake = Faker()

def generate_fake_users(count: int = 5):
    count = max(1, int(count or 5))
    out = []
    for _ in range(count):
        out.append({
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address().replace("\n", ", ")
        })
    return out
