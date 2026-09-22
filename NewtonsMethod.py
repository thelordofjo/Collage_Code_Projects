import math
from colorama import init, Fore, Back, Style

# Main program
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.YELLOW + Style.BRIGHT + "🔢 NUMERICAL METHODS FOR NONLINEAR EQUATIONS 🔢".center(70))
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "NEWTON'S METHOD")

def make_function(expression_string):
    """Convert a string expression into a callable f(x)."""
    def function(x_value):
        return eval(expression_string, {"x": x_value, "math": math,
                               "sin": math.sin, "cos": math.cos,
                               "tan": math.tan, "exp": math.exp,
                               "log": math.log, "sqrt": math.sqrt,
                               "pi": math.pi, "e": math.e})
    return function

def make_derivative(function, h=1e-6):
    """Create derivative function using finite differences."""
    def derivative(x):
        return (function(x + h) - function(x - h)) / (2 * h)
    return derivative

def newton(function, derivative, initial_guess, tolerance=0.0000001, max_iterations=100):
    """
    Newton-Raphson Method
    --------------------
    x_{n+1} = x_n - f(x_n) / f'(x_n)
    """
    print(f"\n{'Iteration':>5}  {'Current x':>16}  {'f(x)':>16}  {'f\'(x)':>16}  {'Error':>14}")
    print("─" * 75)
    
    iteration_history = [initial_guess]
    x_current = initial_guess
    
    for iteration_number in range(1, max_iterations + 1):
        f_current = function(x_current)
        f_prime_current = derivative(x_current)
        
        if abs(f_prime_current) < 1e-12:
            print(f"⚠ Derivative too small at x = {x_current:.7f}")
            return x_current, iteration_number, iteration_history
        
        x_next = x_current - f_current / f_prime_current
        current_error = abs(x_next - x_current)
        iteration_history.append(x_next)
        
        print(f"{iteration_number:>5}  {x_current:>16.7f}  {f_current:>16.7f}  {f_prime_current:>16.7f}  {current_error:>14.7f}")
        
        if current_error < tolerance and abs(f_current) < tolerance:
            print(f"\n✔ Converged after {iteration_number} iterations.")
            return x_next, iteration_number, iteration_history
        
        x_current = x_next
    
    print(f"\n⚠ Did not converge in {max_iterations} iterations.")
    return x_current, max_iterations, iteration_history


function_str = input("Enter the function f(x): "+ Fore.MAGENTA + Style.BRIGHT)
initial_guess = float(input("Enter the initial guess: " + Fore.MAGENTA + Style.BRIGHT))

f = make_function(function_str)
f_prime = make_derivative(f)

root, iterations, history = newton(f, f_prime, initial_guess)

print(f"\n Final approximated root: {root:.5f}")
print(f" f(root) = {f(root):.5f}")
print(f" Converged in {iterations} iterations")