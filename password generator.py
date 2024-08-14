import secrets
import string
l=int(input("enter the length of the password"))

def generate_secure_password(l):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(l))
    return password


secure_password = generate_secure_password(l)
print("Secure password:", secure_password)
