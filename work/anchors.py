with open("../HTML-Grundlagen.html", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:

    if "<h2>" in line and "</h2>" in line:
        print(line)
