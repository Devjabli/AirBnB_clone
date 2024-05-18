# AirBnB Clone Project

## Welcome to the AirBnB clone project v1

![](pics/65f4a1dd9c51265f49d0.png)

## Descreption
### => The first step is to write a command interpreter to manage your AirBnB objects. This is crucial as it forms the foundation for building your first full web application: the AirBnB clone v1.

![](pics/815046647d23428a14ca.png)

### Goals
- **Parent Class (BaseModel)**: Handle initialization, serialization, and deserialization of future instances.
- **Serialization/Deserialization Flow**: Instance ↔ Dictionary ↔ JSON string ↔ file.
- **Classes Creation**: User, State, City, Place, etc., inheriting from BaseModel.
- **Storage Engine**: Implement the first abstracted storage engine (File storage).
- **Unit Tests**: Validate all classes and storage engine.

## Command Interpreter
Similar to a shell but specific to our project. It allows you to:

- **Create**: New objects (e.g., User, Place).
- **Retrieve**: Objects from a file, database, etc.
- **Operate**: Count, compute stats, etc.
- **Update**: Object attributes.
- **Destroy**: Objects.

## Resources
- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [cmd module in depth](https://pymotw.com/2/cmd/)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime module](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [cmd module wiki page](https://wiki.python.org/moin/CmdModule)

## Learning Objectives
By the end of this project, you should be able to:

- Create a Python package.
- Create a command interpreter using the `cmd` module.
- Understand unit testing and implement it in large projects.
- Serialize and deserialize a class.
- Write and read a JSON file.
- Manage datetime.
- Understand UUID.
- Use `*args` and `**kwargs`.
- Handle named arguments in a function.

## Requirements

### Python Scripts
- Editors: `vi`, `vim`, `emacs`.
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- Files should end with a new line.
- First line: `#!/usr/bin/python3`.
- Mandatory `README.md` at project root.
- Follow `pycodestyle` (version 2.8.*).
- Files must be executable.
- File length tested with `wc`.
- Modules should have documentation.
- Classes should have documentation.
- Functions should have documentation.

### Python Unit Tests
- Editors: `vi`, `vim`, `emacs`.
- Files should end with a new line.
- Test files should be inside a `tests` folder.
- Use the `unittest` module.
- Test files: `.py` extension, start with `test_`.
- Test organization should mirror the project structure.
- Run tests with `python3 -m unittest discover tests` or `python3 -m unittest tests/test_models/test_base_model.py`.
- Modules, classes, and functions should have documentation.
- Collaborate on test cases to cover all edge cases.


## Execution
Your shell should work in both interactive and non-interactive modes.

### Interactive Mode
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### All tests should pass in non-interactive mode:
```
$ echo "python3 -m unittest discover tests" | bash
```
