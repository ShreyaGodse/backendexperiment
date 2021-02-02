from flask import Flask,request

app = Flask(__name__)
@app.route("/")
def home():
  return "Welcome to my app!"

@app.route("/shreya")
def func():
    name = request.args.get("name") if "name" in request.args else ""

    return name

@app.route("/abc")
def abc():
    return "Shreya"

@app.route("/add")
def add():
    n1 = request.args.get("n1") if "n1" in request.args else ""
    n2 = request.args.get("n2") if "n2" in request.args else ""
    return (n1+n2)

@app.route("/validate")
def validate():
    name = request.args.get("name") if "name" in request.args else ""
    if len(name)>0:
        return name
    else:
        return "Name not provided"

@app.route("/square")
def square():
    num = request.args.get("number") if "number" in request.args else ""
    inum = int(num)
    sq = inum**2
    return str(sq)

@app.route("/squareroot")
def squareroot():
    num = request.args.get("number") if "number" in request.args else ""
    inum = int(num)
    sqr = inum**0.5
    return str(sqr)

@app.route("/cube")
def cube():
    num = request.args.get("number") if "number" in request.args else ""
    inum = int(num)
    cube = inum**3
    return str(cube)

@app.route("/cuberoot")
def cuberoot():
    num = request.args.get("number") if "number" in request.args else ""
    inum = int(num)
    cuberoot = inum**(1./3.)
    return str(cuberoot)


@app.route("/calculate")
def calculate():
    num = request.args.get("number") if "number" in request.args else ""
    inum = int(num)
    sq = inum**2
    sqr = inum**0.5
    cube = inum**3
    cuber = inum**(1./3.)
    return {
        "Number ": inum,
        "Square ": sq,
        "Square root ": sqr,
        "Cube ": cube,
        "Cube root: " : cuber
    }





@app.route("/stringlen", methods = ["POST"])
def stringlen():
    request_json = request.get_json()
    string1 = request_json["name"] if "name" in request_json else ""

    return {
        "name": string1,
        "length": len(string1)
    }