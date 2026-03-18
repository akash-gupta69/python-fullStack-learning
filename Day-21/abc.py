from werkzeug.security import generate_password_hash, check_password_hash

hash_pass = generate_password_hash("password123") 
print(hash_pass)

hash_pass_0 = generate_password_hash("password12")

check = check_password_hash(hash_pass,hash_pass_0)      # every time you run you get different hash values so both the passwords not same 
print(check)            # password123 -> Random SALT -> hash this is how the hashing done


# from werkzeug.security import generate_password_hash, check_password_hash

# # During Registration (store this in DB)
# stored_hash = generate_password_hash("password123")

# # During Login (user enters password)
# entered_password = "password123"

# check = check_password_hash(stored_hash, entered_password)
# print(check)