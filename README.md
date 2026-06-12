# 🐚 ShellbeeScript

> A beginner-friendly programming language designed for learning, scripting, and rapid prototyping.

![Version](https://img.shields.io/badge/version-v1.0-gold)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/built%20with-Python-green)

---

## Overview

ShellbeeScript is a custom programming language built from scratch using Python. It combines simple syntax with scripting capabilities, making it ideal for beginners who want to understand how programming languages work.

Created by **Suman Rajput**.

---

## Features

* Easy variable declarations using `be`
* Output using `Display()`
* User input using `form()`
* Conditional logic with `Test {}` and `otherwise {}`
* Repetition using `Rep-for()`
* Shell-style command execution with `shell {}`

---

## Hello World

```shellbee
Display("Hello, World!")
```

Output:

```text
Hello, World!
```

---

## Project Structure

```text
ShellbeeScript/
├── docs/
├── examples/
├── src/
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

## Example

```shellbee
be name = form("Enter your name: ")

Test(name == "Bee")
{
    Display("Welcome back!")
}
otherwise
{
    Display("Hello " + name)
}
```

---

## Roadmap

### Version 1.1

* Comments
* Better error handling
* Improved interpreter

### Version 2.0

* Functions
* Lists
* Modules
* Package support

---

## Creator

Suman Rajput

GitHub: github.com/SumanRajput06

---

## License

MIT License
