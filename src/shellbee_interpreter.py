import sys

memory = {}
functions = {}

def interpret_line(line):
line = line.strip()

```
# Variable declaration
if line.startswith("be "):
    var_name, value = line[3:].split("=", 1)
    var_name = var_name.strip()
    value = eval(value.strip())
    memory[var_name] = value

# Display statement
elif line.startswith("Display(") and line.endswith(")"):
    inner = line[8:-1].strip()

    if inner in memory:
        print(memory[inner])
    else:
        print(eval(inner))

# Version command
elif line == "version()":
    print("ShellbeeScript v2.0.0")
    print("Created by Suman Rajput")

# Creator command
elif line == "creator()":
    print("Suman Rajput")

# Comments and blank lines
elif line.startswith("#") or line == "":
    pass

# Function call
elif line.endswith("()"):
    func_name = line.replace("()", "").strip()

    if func_name in functions:
        for cmd in functions[func_name]:
            interpret_line(cmd)
    else:
        print(f"Shellbee Error: Function '{func_name}' not found")

else:
    print(f"Shellbee Error: Unknown command '{line}'")
```

def run_shellbee_file(filepath):

```
print("🐚 ShellbeeScript v2.0")
print("----------------------")

with open(filepath, "r") as file:
    lines = file.readlines()

i = 0

while i < len(lines):

    line = lines[i].strip()

    # Function definition
    if line.startswith("fun "):

        func_name = line[4:].replace("()", "").strip()

        body = []

        i += 1

        while i < len(lines):

            current = lines[i].strip()

            if current == "}":
                break

            if current != "{":
                body.append(current)

            i += 1

        functions[func_name] = body

    else:
        interpret_line(line)

    i += 1
```

if **name** == "**main**":

```
if len(sys.argv) < 2:
    print("Usage: python shellbee_interpreter.py <file.shellbee>")
else:
    run_shellbee_file(sys.argv[1])
```
