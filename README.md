# **Codebase Flattener**  

*Effortlessly declutter your project by flattening nested `.py` files into a single folder.*

## **Overview**

Do you often find yourself digging through multiple nested directories to find Python files?  
**Codebase Flattener** is here to simplify your life! This lightweight CLI tool scans through your source directory (and all its subdirectories), collects all `.py` files (excluding `__init__.py`), and copies them into a single destination directory — all while automatically renaming conflicting files. 

It's perfect for organizing large codebases, consolidating scripts, or preparing for migration or backup.

---

## **Features**
- **Flattens Nested Directories**: Gathers all `.py` files into a single folder, no matter how deeply nested they are.
- **Excludes `__init__.py`**: Avoids copying module definition files (`__init__.py`).
- **Handles File Name Conflicts**: Renames files with duplicate names to ensure no overwriting.
- **Clean Destination Directory**: Automatically clears the destination folder before copying.
- **Command-Line Simplicity**: Provides an easy-to-use CLI interface.
- **Directory Path Preservation**: Option to prefix files with their original directory structure.

---

## **Installation**

Install the package from source:

```bash
pip install git+https://github.com/josephchay/codebase-flattener.git
```

## **Command-Line Arguments**

| Argument         | Required | Default | Description                                             |
|------------------|----------|---------|---------------------------------------------------------|
| `--src`          | Yes      | -       | Source directory containing the Python files to flatten |
| `--dest`         | Yes      | -       | Destination directory where files will be copied        |
| `--include-init` | No       | `False` | Include `__init__.py` files in the flattening process   |

## **Usage Examples**

Here are various scenarios and how to use the tool:

| Scenario           | Command                                                      | Description                                                               |
|--------------------|--------------------------------------------------------------|---------------------------------------------------------------------------|
| Basic Flattening   | `codebase-flattener --src src --dest flat`                   | Flattens all `.py` files (except `__init__.py`) into the 'flat' directory |
| Include Init Files | `codebase-flattener --src src --dest flat --include-init`    | Includes `__init__.py` files in the flattening process                    |
| Relative Paths     | `codebase-flattener --src ../project/src --dest ./flat`      | Works with relative paths                                                 |
| Absolute Paths     | `codebase-flattener --src /path/to/src --dest /path/to/dest` | Works with absolute paths                                                 |

### **Example Directory Transformations**

**Example 1: Basic Flattening**
```
Before:                             After:
src/                               flat/
├── module1/                       ├── script1.py
│   ├── script1.py                 ├── helper.py
│   ├── __init__.py               └── script2.py
│   └── utils/
│       └── helper.py
└── module2/
    └── script2.py

Command: codebase-flattener --src src --dest flat
```

**Example 2: With Directory Prefixes**
```
Before:                             After:
src/                               flat/
├── auth/                          ├── auth__login.py
│   ├── login.py                   ├── auth__utils__validator.py
│   └── utils/                     ├── models__user.py
│       └── validator.py           └── models__data__schema.py
└── models/
    ├── user.py
    └── data/
        └── schema.py

Command: codebase-flattener --src src --dest flat
```

**Example 3: Including Init Files**
```
Before:                             After:
src/                               flat/
├── core/                          ├── core____init__.py
│   ├── __init__.py               ├── core__main.py
│   ├── main.py                   ├── plugins____init__.py
│   └── plugins/                  └── plugins__extra.py
│       ├── __init__.py
│       └── extra.py

Command: codebase-flattener --src src --dest flat --include-init
```

## **How It Works**
1. **Directory Traversal**: Recursively scans through the source directory using `os.walk()`.
2. **File Filtering**: Selects `.py` files, skipping `__init__.py` (unless `--include-init` is used).
3. **Conflict Resolution**: Renames files if conflicts are detected in the destination folder.
4. **Copy Operation**: Uses `shutil.copy2()` to preserve metadata while copying files.
5. **Clean Destination**: Ensures the destination folder is emptied before starting.

## **Why Use Codebase Flattener?**
* Save time navigating large, deeply nested projects.
* Quickly consolidate files for migration, sharing, or debugging.
* Eliminate clutter while maintaining file integrity.
* Fully automated with zero manual intervention required.

## **Development**
Clone the Repository:

```bash
git clone https://github.com/josephchay/codebase-flattener.git
cd flatten-directory
```

Install Locally:

```bash
pip install .
```

Run Tests:
To test functionality during development, you can run:

```bash
python -m src.main --src <source_dir> --dest <dest_dir>
```

## **Contributing**
Contributions are welcome! If you'd like to report a bug, suggest a feature, or submit a PR:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Description of changes"`).
4. Push your branch and open a PR.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **Support**
Need help? Have a question? Feel free to reach out:
* **Email**: josephemmanuelchay@gmail.com
* **GitHub Issues**: [Issues](https://github.com/josephchay/codebase-flattener/issues)

Make your life easier and your projects cleaner — flatten your directories today!
