import math
from colorama import init, Fore, Back, Style

# Main program
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.YELLOW + Style.BRIGHT + "🔢 NUMERICAL METHODS FOR NONLINEAR EQUATIONS 🔢".center(70))
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "SECANT METHOD")

def make_function(expression_string):
    """Convert a string expression into a callable f(x)."""
    def function(x_value):
        return eval(expression_string, {"x": x_value, "math": math,
                               "sin": math.sin, "cos": math.cos,
                               "tan": math.tan, "exp": math.exp,
                               "log": math.log, "sqrt": math.sqrt,
                               "pi": math.pi, "e": math.e})
    return function

def secant(function, first_guess, second_guess, tolerance=0.0000001, max_iterations=100):
    """
    Secant Method
    -------------
    Approximates the derivative using two points.
    x_{n+1} = ( x_n * x_{n-1} + 2 ) / ( x_n + x_{n-1} )
    """
    print(f"\n{'Iteration':>5}  {'Current x':>16}  {'f(Current x)':>16}  {'Error':>14}")
    print("─" * 60)

    iteration_history = [first_guess, second_guess]
    
    for iteration_number in range(1, max_iterations + 1):
        function_at_first = function(first_guess)
        function_at_second = function(second_guess)

        next_guess = second_guess - function_at_second * (second_guess - first_guess) / (function_at_second - function_at_first)
        current_error = abs(next_guess - second_guess)
        iteration_history.append(next_guess)

        print(f"{iteration_number:>5}  {second_guess:>5.4f}  {function_at_second:>5.4f}  {current_error:>5.7f}")

        if current_error < tolerance and abs(function(next_guess)) < tolerance:
            print(f"\n✔  Converged after {iteration_number} iterations.")
            return next_guess, iteration_number, iteration_history

        first_guess = second_guess
        second_guess = next_guess

    print(f"\n⚠  Did not converge in {max_iterations} iterations.")
    return second_guess, max_iterations, iteration_history

print('')
# secant(make_function("x**2 - 2"), first_guess=0.5, second_guess=1.0) 
print("final approximated root :", secant(make_function(input("Enter the function expression: "+ Fore.MAGENTA + Style.BRIGHT)), float(input("Enter the first guess: " + Fore.MAGENTA + Style.BRIGHT)), float(input("Enter the second guess: " + Fore.MAGENTA + Style.BRIGHT)))[0])