amount = 60000
location_match = "No"
transactions = 1

fraud = False

if amount > 50000 and location_match.lower() == "no":
    fraud = True


elif transactions > 3:
    fraud = True

# Output
if fraud:
    print("Fraud Detected")
else:
    print("Transaction Safe")
