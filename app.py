from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(number: int) -> int: 
    if (isinstance(number, int) == True): 
        if (number < 0): 
            return -1; 
        else: 
            if(number ==  0 or number == 1): 
                return 1; 
            else: 
                factorialResult: int = 1; 
                for i in range(2, (number + 1)): 
                    factorialResult *=  i; 
                return factorialResult; 
    else: 
        raise TypeError("Not A Integer Argument."); 

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        user_input = request.form.get("number")
        try:
            number = int(user_input)
            if number < 0:
                error = "Factorial Is Not Defined For Negative Number."
            else:
                result = factorial(number)
        except ValueError:
            error = "Not A Valid Input, Please Enter A Valid Number."
        except TypeError as e:
            error = str(e)
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run()
