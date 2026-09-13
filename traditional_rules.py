message = input("Write your issue:")

if "refund" in message.lower():
    print("Billing issue")
elif "login" in message.lower():
    print("Login issue")
else:
    print("General issue")

