device_status = "Active"
temperature = 38

if device_status == "Active":
    if temperature > 35:
        print("High Temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")