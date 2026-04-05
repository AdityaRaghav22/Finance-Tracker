from app import create_app
import random

app = create_app()

# print("DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])

def print_sample_data_auth_register():
    strings = ["admin", "viewer", "analyst"]
    for i in range(10):
        username = "test"
        password = "test" + str(i+199999)
        email = "test" + str(i) + "@gmail.com"
        role = random.choice(strings)         
        print(f"""("username": "{username}", "password": "{password}", "email": "{email}", "role": "{role}")""")

# print_sample_data_auth_register()

def print_sample_data_auth_login():
    for i in range(10):
        username = "test"
        password = "test" + str(i+199999)
        email = "test" + str(i) + "@gmail.com"
        print(f"""("username": "{username}", "password": "{password}", "email": "{email}")""")

print_sample_data_auth_login()

def print_sample_data_frecord_create():
    for i in range(10):
        user_id = i
        amount = random.randint(1000, 10000)
        type = random.choice(["income", "expense"])
        category = random.choice(["salary", "food", "rent", "transportation", "entertainment", "other"])
        date = "01-" + str(i+1) + "-2026"
        description = "test" + str(i+1)
        print(f"""("user_id": {user_id}, "amount": {amount}, "type": "{type}", "category": "{category}", "date": "{date}", "description": "{description}")""")

print_sample_data_frecord_create()

# print(app.url_map)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
