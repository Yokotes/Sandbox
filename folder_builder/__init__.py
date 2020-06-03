import os
import shutil

class Folder():
    '''Folder class that can contain objects'''

    # Init new instance of class
    def __init__(self, name='New folder', path=os.path.curdir):
        '''
        Parameters:
            name - name of new folder
            path - path to new folder

        Create new instance of Folder class.
        '''
        self.name = name
        self.path = os.path.abspath(path)
        self.__objects = []
    
    # Rewrite __str__
    def __str__(self):
        '''Return folder path and name as a string'''
        return self.path + "\\" + self.name

    # Rewrite __iter__
    def __iter__(self):
        '''Return iterator'''
        self.next = 0
        return self

    # Rewrit __next__
    def __next__(self):
        '''Return objects that contained in a folder'''
        try:
            current = self.__objects[self.next]
            self.next += 1
            return current
        except IndexError:
            raise StopIteration

    # Change path for the subfolder
    def __change_path_subfolders(self, parent):
        '''
        Parameters:
            parent - folder that contains target subfolder

        Change paths to subfolders
        '''
        if (self == parent): 
            return
        self.path = '{}\\{}'.format(parent.path, parent.name)
        for obj in self.__objects:
            if (type(obj) is Folder):
                obj.path = '{}\\{}'.format(self.path, self.name)
                obj.__change_path_subfolders(obj)
            else: continue

    # Add object to the folder
    def add(self, obj):
        '''
        Parameters:
            obj - any object
        
        Add new object in the folder
        '''
        if (type(obj) is Folder): 
            obj.__change_path_subfolders(self)
        self.__objects.append(obj)
    
    # Remove objects from the folder
    def remove(self, obj):
        '''
        Parameters:
            obj - any object
        
        Remove object from the folder
        '''
        if (obj in self.__objects):
             self.__objects.remove(obj)
        else:
            raise ValueError("Object doesn't exist in the folder")
    
    # Build a folder and inner objects
    def build(self):
        '''
        Build a new folder on the driver and fill it with inner objects as txt

        NOTE: If folder already exist will raise an exception
        '''
        try:
            folder_path = '{}\\{}'.format(self.path, self.name)
            os.makedirs(folder_path)
            for obj in self.__objects:
                if (type(obj) is not Folder):
                    with open(folder_path + '\\{}.txt'.format(str(obj)), 'w') as file:
                        file.write(str(obj))
                else:
                    obj.build()
            print('Folder has been created')
        except FileExistsError as error:
            print(error)

    # Delete the folder from the driver
    def delete(self):
        '''
        Delete the folder from the driver if it exist
        '''
        folder_path = '{}\\{}'.format(self.path, self.name)
        if (os.path.exists(folder_path)):
            shutil.rmtree(folder_path)
            print('Folder has been deleted')
        else:
            raise FileExistsError("Folder doesn't exist")