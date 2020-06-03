# Overview
Here I'll post ideas that can grow in projects

# Projects
## Folder Builder
Folder builder is a script that generates tree of folders and inner files

### How to use
Folder builder is a very simple script.
At first you need to create a new instance of Folder class.
```python
f1 = fb.Folder(name='Test folder', path='./')
```
There are 2 parameters:
    +name - Folder's name
    +path - Path to folder

You can don't enter parameters, in that case name will be 'New Folder' and folder's path will be your current path
```python
f1 = fb.Folder()

print(f1.name)
# Output: 'New Folder'

print(f1.path)
# Output: '*Your current absolute path*'
```

### Ways to grow
1. Generate Site Project (index.html, assets folder, css folder and etc.)