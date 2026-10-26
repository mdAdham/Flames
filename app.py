from flask import Flask, render_template, request, redirect

from collections import Counter

def calculate_count(name1, name2):
    c1 = Counter("".join(c for c in name1.lower() if c.isalpha()))
    c2 = Counter("".join(c for c in name2.lower() if c.isalpha()))

    diff1 = c1 - c2
    diff2 = c2 - c1

    return sum(diff1.values()) + sum(diff2.values())

def do_flames(count):
    flames = ["Friends", "Lover", "Affection", "Marriage", "Enemies", "Siblings"]

    if count == 0:
        return "You've Made a Error Bro"

    index = 0
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    return flames[0]

app = Flask(__name__)

result = False
resultValue = ""

@app.route("/")
def home():
    return render_template("index.html", result=result, resvalue=resultValue)

@app.route("/send", methods=["POST"])
def sendfunc():
    data = request.form
    names = list(data.values())

    name1, name2 = names
    print(name1)
    print(name2)

    count = calculate_count(name1, name2)
    res = do_flames(count)

    global result, resultValue

    result=True
    resultValue=res
    return redirect("/")

if __name__ == "__main__":
    app.run()

# n1 = input("Enter Name 1: ")
# n2 = input("Enter Name 2: ")

# count = calculate_count(n1, n2)
# print(f"Result -> {do_flames(count)}")

# print(calculate_count())
