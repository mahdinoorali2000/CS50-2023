extensions = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg": "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}
x = input("File name: ").strip().lower()
if x.count(".") > 1:
    x = x.replace(".","", (x.count(".") - 1))

if x.partition(".")[2] in extensions:
    print(extensions[x.partition(".")[2]])
else:
    print("application/octet-stream")
