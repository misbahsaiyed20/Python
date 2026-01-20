from validation import UserSchema

schema = UserSchema()

user_data = {
    "name": "Misba",
    "email": "misbaemail",
    "age": "twenty"
}

# checking user input using marshmallow
errors = schema.validate(user_data)

if errors:
    print("Input validation failed:", errors)
else:
    print("All inputs are valid")
