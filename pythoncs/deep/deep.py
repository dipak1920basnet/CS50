get_user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
if get_user == "42":
    print("Yes")
elif get_user.lower().startswith("forty") and get_user.lower().endswith("two"):
    print("Yes")
else:
    print("No")
