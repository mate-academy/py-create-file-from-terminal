# Create file from terminal

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Create an app `create_file.py` that takes directory path, file name, file
content from the terminal and creates file. There should be flags `-d` or `-f`:

- If only `-d` flag passed, means all items after this flag are parts of the
path.

`python create_file.py -d dir1 dir2` - creates directory `dir1/dir2` inside
current directory.
- If only `-f` flag passed, means first item is the file name.

`python create_file.py -f file.txt`

After pressing `Enter` it creates file `file.txt` and then terminal should
ask you to input content lines until you input "stop": 
```python
Enter content line: Line1 content
Enter content line: Line2 content
Enter content line: Line3 content
Enter content line: stop
```
This creates file `file.txt` inside current directory with content:
```python
2022-02-01 14:41:10
1 Line1 content
2 Line2 content
3 Line3 content
```
App should add current timestamp at the top and number lines. If `file.txt`
already exists it should add content below:

`python create_file.py -f file.txt`
```python
Enter content line: Another line1 content
Enter content line: Another line2 content
Enter content line: Another line3 content
Enter content line: stop
```

```python
2022-02-01 14:41:10
1 Line1 content
2 Line2 content
3 Line3 content

2022-02-01 14:46:01
1 Another line1 content
2 Another line2 content
3 Another line3 content
```


- If both `-d` and `-f` flags passed, app creates directory and
file with content inside this directory.

`python create_file.py -d dir1 dir2 -f file.txt` 
```python
Enter content line: Line1 content
Enter content line: Line2 content
Enter content line: Line3 content
Enter content line: stop
```
Creates directory `dir1/dir2` inside current directory and 
creates file `file.txt`
inside that directory with content:

`dir1/dir2/file.txt: `
```python
2022-02-01 14:46:01
1 Line1 content
2 Line2 content
3 Line3 content
```
It would be relevant to use:
- `sys.argv` to read arguments from the terminal
- `os.makedirs` to create directories
- `.strftime()` method for `datetime.now()` to make timestamp
more beautiful.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
