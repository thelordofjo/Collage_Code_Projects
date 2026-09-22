import math
from colorama import init, Fore, Back, Style

# Main program
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.YELLOW + Style.BRIGHT + "🔢 NUMERICAL METHODS FOR NONLINEAR EQUATIONS 🔢".center(70))
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "BISECTION METHOD")


def make_function(expression_string):
    """Convert a string expression into a callable f(x)."""
    def function(x_value):
        return eval(expression_string, {"x": x_value, "math": math,
                               "sin": math.sin, "cos": math.cos,
                               "tan": math.tan, "exp": math.exp,
                               "log": math.log, "sqrt": math.sqrt,
                               "pi": math.pi, "e": math.e})
    return function

def bisection(function, a, b, tolerance=0.0000001, max_iterations=100):
    """
    Bisection Method
    ----------------
    Finds root by repeatedly halving the interval [a, b].
    Requires f(a) and f(b) to have opposite signs.
    """
    # Check if f(a) and f(b) have opposite signs
    fa = function(a)
    fb = function(b)
    
 
    print(f"\n{'Iteration':^8}  {'a':^14}  {'b':^14}  {'c':^14}  {'f(c)':^14}  {'Error':^12}")
    print("─" * 85)
    
    iteration_history = []
    
    for iteration_number in range(1, max_iterations + 1):
        c = (a + b) / 2
        fc = function(c)
        current_error = (b - a) / 2
        iteration_history.append(c)
        
        print(f"{iteration_number:^8}  {a:^14.7f}  {b:^14.7f}  {c:^14.7f}  {fc:^14.7f}  {current_error:^12.7f}")
        
        if abs(fc) < tolerance or current_error < tolerance:
            print(f"\n✔ Converged after {iteration_number} iterations.")
            return c, iteration_number, iteration_history
        
        # Determine the subinterval for the next iteration 
        # (either [a, c] or [c, b])
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print(f"\n⚠ Did not converge in {max_iterations} iterations.")
    return (a + b) / 2, max_iterations, iteration_history


function_str = input("Enter the function f(x): "+ Fore.MAGENTA + Style.BRIGHT)
a = float(input("Enter the left endpoint a: "+ Fore.MAGENTA + Style.BRIGHT))
b = float(input("Enter the right endpoint b: "+ Fore.MAGENTA + Style.BRIGHT))

f = make_function(function_str)
root, iterations, history = bisection(f, a, b)

if root is not None:
    print(f"\n Final approximated root: {root:.5f}")
    print(f" f(root) = {f(root):.5f}")
    print(f" Converged in {iterations} iterations")