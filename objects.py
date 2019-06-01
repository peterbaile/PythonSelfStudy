# Dictionaries/ JSON Object
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# cannot use customer.age

# Approach 1:
# the problem with this approach is that an error occurs if the field does not exist
# gender = customer["gender"]  # will report error
age = customer["age"]

# Approach 2:
gender = customer.get("gender")  # will return the None Object that represents the absence of a value
print(gender)
gender = customer.get("gender", "male")  # gender = male, will not change customer
print(gender)
