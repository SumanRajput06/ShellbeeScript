import sys

memory = {}

def interpret_line(line):
    line = line.strip()

    if line.startswith("be "):
        var_name, value = line[3:].split("=", 1)
        memory[var_name.strip()] = eval(value.strip())

    elif line.startswith("Display(") and line.endswith(")"):
        inner = line[8:-1].strip()

        if inner in memory:
            print(memory[inner])
        else:
            print(eval(inner))

    elif line == "version()":
        print("ShellbeeScript v2.0.0")

    elif line.startswith("#") or line == "":
        pass

    else:
        print(f"Shellbee Error: {line}")


def run_shellbee_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            interpret_line(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shellbee_interpreter.py <file.shellbee>")
    else:
        run_shellbee_file(sys.argv[1])
