from flask import Flask, request

app = Flask(__name__)

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

@app.route("/")
def home():
    result = ""
    a = request.args.get("a")
    b = request.args.get("b")
    op = request.args.get("op")

    if a and b and op:
        a = float(a)
        b = float(b)

        if op == "add": result = add(a,b)
        elif op == "sub": result = subtract(a,b)
        elif op == "mul": result = multiply(a,b)
        elif op == "div": result = divide(a,b)

    return f"""
    <html>
    <head>
    <title>Calculator</title>
    <style>
        body {{ font-family: Arial; text-align:center; margin-top:50px; }}
        .box {{ display:inline-block; padding:20px; border:1px solid #333; border-radius:10px; }}
        input, select {{ padding:8px; margin:5px; }}
        button {{ padding:10px 20px; }}
    </style>
    </head>

    <body>
        <div class="box">
        <h2>GUI Calculator</h2>
        <form>
            <input name="a" placeholder="Enter number A" required>
            <input name="b" placeholder="Enter number B" required><br>

            <select name="op">
                <option value="add">Add</option>
                <option value="sub">Subtract</option>
                <option value="mul">Multiply</option>
                <option value="div">Divide</option>
            </select>

            <button type="submit">Calculate</button>
        </form>

        <h3>Result: {result}</h3>
        </div>
    </body>
    </html>
    """

