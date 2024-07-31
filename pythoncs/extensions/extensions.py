get_file_name = input("File name: ").lower().strip()
# front, back = get_file_name.split(".")
if get_file_name.endswith("gif"):
    print(f"image/gif")
elif get_file_name.endswith("jpg") or get_file_name.endswith("jpeg"):
    print(f"image/jpeg")
elif get_file_name.endswith("png"):
    print(f"image/png")
elif get_file_name.endswith("pdf"):
    print(f"application/pdf")
elif get_file_name.endswith("txt"):
    print(f"text/plain")
elif get_file_name.endswith("zip"):
    print(f"application/zip")
else:
    print("application/octet-stream")
