get_greeting = input("Greeting: ").strip().lower()
if get_greeting.startswith("hello"):
    print("$0")
elif get_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
