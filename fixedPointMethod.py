import math
from colorama import init, Fore, Back, Style

# Main program
print(Fore.GREEN + Style.BRIGHT + "=" * 70)
print(Fore.YELLOW + Style.BRIGHT + "🔢 NUMERICAL METHODS FOR NONLINEAR EQUATIONS 🔢".center(70))
print(Fore.GREEN + Style.BRIGHT + "=" * 70)

def make_function(expression_string):
    """Convert a string expression into a callable f(x)."""
    def function(x_value):
        return eval(expression_string, {"x": x_value, "math": math,
                               "sin": math.sin, "cos": math.cos,
                               "tan": math.tan, "exp": math.exp,
                               "log": math.log, "sqrt": math.sqrt,
                               "pi": math.pi, "e": math.e})
    return function

def numerical_derivative(g, x, h=1e-6):
    """Approximate derivative using central difference"""
    return (g(x + h) - g(x - h)) / (2 * h)

def convergence_test(g, x0):
    """Check |g'(x0)| < 1"""
    g_prime = numerical_derivative(g, x0)
    print(f"\n🔍 Convergence Test:")
    print(f"g'(x0) ≈ {g_prime:.6f}")
    print(f"|g'(x0)| = {abs(g_prime):.6f}")
    
    if abs(g_prime) < 1:
        print(Fore.GREEN + "✔ Likely to converge (|g'(x0)| < 1)\n")
        return True
    else:
        print(Fore.RED + "⚠ May NOT converge (|g'(x0)| ≥ 1)\n")
        return False

def fixed_point(g, initial_guess, tolerance=0.0000001, max_iterations=100):
    print(f"\n{'Iteration':>5}  {'Current x':>16}  {'g(x)':>16}  {'Error':>14}")
    print("─" * 60)
    
    iteration_history = [initial_guess]
    x_current = initial_guess
    
    for iteration_number in range(1, max_iterations + 1):
        x_next = g(x_current)
        current_error = abs(x_next - x_current)
        iteration_history.append(x_next)
        
        print(f"{iteration_number:>5}  {x_current:>16.7f}  {x_next:>16.7f}  {current_error:>14.7f}")
        
        if current_error < tolerance:
            print(f"\n✔ Converged after {iteration_number} iterations.")
            return x_next, iteration_number, iteration_history
        
        x_current = x_next
    
    print(f"\n⚠ Did not converge in {max_iterations} iterations.")
    return x_current, max_iterations, iteration_history

# Main program
print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
print("FIXED POINT ITERATION METHOD")
print("=" * 60)
print("Solves x = g(x)")
print("You need to rearrange your equation f(x) = 0 into x = g(x)")
print("Examples: For x² - 2 = 0, use g(x) = √(x+2) or g(x) = (x + 2/x)/2")

g_str = input("\nEnter the fixed point function g(x): " + Fore.MAGENTA + Style.BRIGHT)
initial_guess = float(input("Enter the initial guess: " + Fore.MAGENTA + Style.BRIGHT))

g = make_function(g_str)

# 🔴 Convergence test BEFORE iterations
converges = convergence_test(g, initial_guess)

if converges:
    root, iterations, history = fixed_point(g, initial_guess)

    print(f"\n🎯 Final approximated root: {root:.10f}")
    print(f" Check: g(root) = {g(root):.10f}")
    print(f" Should be close to root: {root:.10f}")
    print(f" Converged in {iterations} iterations")
else:
    print("❌ Try a different g(x) or initial guess.")