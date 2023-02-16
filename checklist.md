# Сheck Your Code Against the Following Points

## Code Efficiency

1. You don't need `else` if you have `break` in if-condition.

Good example:

```python
for _ in range(10):
    if condition:
        break
    print("Best practice")
```

Bad example:

```python
for _ in range(10):
    if condition:
        break
    else:
        print("Bad practice")
```

2. Use `os` methods to make your code cross-platform.

Good example:

```python
def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path
```

Bad example:

```python
def create_path(directories: list) -> str:
    path = "/".join(directories)
    return path
```

## Don't Repeat Yourself

Create separate functions in order not to have repeating blocks of code.

## Code Style

1. Use one style of quotes in your code. Double quotes are preferable.
2. Use descriptive and correct variable names.

Good example:

```python
page_number = 1

with open("file.txt", "a") as source_file:
    source_file.write(f"{page_number} line\n")
```

Bad example:

```python
i = 1

with open("file.txt", "a") as f:
    f.write(f"{i} line\n")
```

## Clean Code

1. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.

2. Make sure you've tested your code with different flags and it works correctly.
