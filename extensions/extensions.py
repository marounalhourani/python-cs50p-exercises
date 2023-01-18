x = input("File Name: ")
if ("." in x):
    dot = x.index(".")
    extension = x[dot + 1: len(x)].strip()
else:
    extension = x

if(extension.lower() == "jpg" or extension =="jpeg"):
    print("image/jpeg")
elif(extension.lower() =="pdf"):
    print("application/pdf")
elif(extension.lower() == "gif"):
    print("image/" + extension)
elif(extension.lower() =="png"):
    print("image/" + extension)
elif(extension.lower() =="txt"):
    print("text/plain")
elif(extension.lower() =="zip"):
    print("application/"+extension)
elif(extension.lower() =="txt.pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")