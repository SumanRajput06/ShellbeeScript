# ShellbeeScript Interpreter

import sys

# Define a simple memory to store variables
memory = {}

def interpret_line(line):
    line = line.strip()

    # Variable declaration: be name = "Suman"
    if line.startswith("be "):
        var_name, value = line[3:].split("=", 1)
        var_name = var_name.strip()
        value = eval(value.strip())  # Use eval to convert "3" to int, etc.
        memory[var_name] = value

# Version command
elif line == "version()":
    print("ShellbeeScript v2.0.0")
    print("Created by Suman Rajput")
elif line.startswith("#") or line == "":
    pass
else:
    print("Shellbee Error")
    print(f"Unknown command: {line}")

def run_shellbee_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            interpret_line(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shellbee_interpreter.py <file.shellbee>")
    else:
        run_shellbee_file(sys.argv[1])
