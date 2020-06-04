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
  * name - Folder's name
  * path - Path to folder

You can don't enter parameters, in that case name will be 'New Folder' and folder's path will be your current path
```python
f1 = fb.Folder()

print(f1.name)
# Output: 'New Folder'

print(f1.path)
# Output: '*Your current absolute path*'
```

To add new object in folder, use script below
```python
# You can use any object (list, dict, string, int and etc.)
f1.add([1, 2, 3, 4])

# You can even add another folder
f2 = Folder(name='Sub Folder')
f1.add(f2)
```
To remove object from folder use:
```python
f1.remove([1, 2, 3, 4])
```
To create your folder on the driver with inner subfolders and text files use:
```python
# Build function will create on your driver folder and will fill it with subfolders and files
f1.build()
```
If you want to delete folder from the driver, you can use script below
```python
# This function will delete folder from your driver
f1.delete()
```

### Ways to grow
1. Generate Site Project (index.html, assets folder, css folder and etc.)