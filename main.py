import math

last = 0
deg = True  # True = degrees, False = radians

def run():
    global last, deg
    print("Calc ready. Type 'q' to quit, 'deg'/'rad' to switch")
    
    while True:
        expr = input("> ").strip()
        
        if expr == 'q': 
            break
        elif expr == 'deg':
            deg = True
            print("Using degrees")
            continue
        elif expr == 'rad':
            deg = False 
            print("Using radians")
            continue
        elif expr == 'ans':
            print(last)
            continue
        elif not expr:
            continue
            
        # replace stuff humans actually type
        expr = expr.replace('^', '**')
        expr = expr.replace('√', 'sqrt')
        expr = expr.replace('Ans', str(last))
        expr = expr.replace('ans', str(last))
        
        # trig funcs
        if deg:
            expr = expr.replace('sin(', 'math.sin(math.radians(')
            expr = expr.replace('cos(', 'math.cos(math.radians(')
            expr = expr.replace('tan(', 'math.tan(math.radians(')
        else:
            expr = expr.replace('sin(', 'math.sin(')
            expr = expr.replace('cos(', 'math.cos(')
            expr = expr.replace('tan(', 'math.tan(')
        
        # other funcs
        expr = expr.replace('log(', 'math.log10(')
        expr = expr.replace('ln(', 'math.log(')
        expr = expr.replace('sqrt(', 'math.sqrt(')
        expr = expr.replace('pi', 'math.pi')
        expr = expr.replace('e', 'math.e')
        
        try:
            last = eval(expr)
            print(f"= {int(last) if last == int(last) else last}")
        except ZeroDivisionError:
            print("Can't divide by zero bro")
        except:
            print("That didn't work")

run()