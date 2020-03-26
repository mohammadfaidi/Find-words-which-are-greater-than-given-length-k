def string():
    str = input("Enter the sentences seperate between by  ,: ")
    k = int(input("Enter the length:"))
    str2 = []
    text = str.split(",")
    for i in text:
        if len(i) > k:
            str2.append(i)

    return str2


while True:
    print(string())
