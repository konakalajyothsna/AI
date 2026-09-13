message = input("Write your issue:") #The money went out twice| "Money was deducted twice from my card" | "I cannot login to my account"|

if "refund" in message.lower():
    print("Billing issue")
elif "login" in message.lower():
    print("Login issue")
else:
    print("General issue")

