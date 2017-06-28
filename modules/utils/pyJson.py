'''
pyJson.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.0
@date: 19/06/17
@status: WRK
'''

import json
import os
import os.path


class pyJson(object):
    """docstring for pyJson."""

    def __init__(self, path):
        self.path = path

    def get(self, file, key=None):
        path_to_file = self.path + '/' + file
        with open(path_to_file, 'r') as tmpj:
            data_str = tmpj.read()

        if key is None:
            return json.loads(data_str)  # return all the json
        else:
            return json.loads(data_str)[key]

    def set(self, args, path=None):
        if path is None:
            with open(self.path, 'w') as f:
                json.dump(args, f)
        else:
            with open(path, 'w') as f:
                f.write(json.dump(args, f))

    def copy(self, path=None, ext='copy'):
        if path is None:
            with open(self.path, 'r') as f:
                json_data = json.load(f)

                ext = '.' + ext

                newPath = self.path + ext
        else:
            with open(path, 'r') as f:
                json_data = json.load(f)

                ext = '.' + ext

                newPath = self.path + ext

        if os.path.isfile(newPath):
            newPath = newPath + ext

        with open(newPath, 'w') as f:
            f.write(json.dumps(json_data))

        return newPath


    def edit(self, key, new_val):
        with open(self.path, 'r') as f:
            json_data = json.load(f)
            json_data[key] = new_val

        new_path = self.copy('tmp')

        with open(new_path, 'w') as f:  # temporary json with new changes
            f.write(json.dumps(json_data))

        os.remove(self.path)
        # rename the temporary file onto the original file
        os.rename(new_path, self.path)

    def append(self, key, args):
        with open(self.path, 'r') as f:
            json_data = json.load(f)
            json_elements = json_data[key]

        json_elements.append(args)

        self.edit(key, json_elements)

    def remove(self, key, arg):
        data = self.read()

        i = -1
        for element in data[key]:
            i += 1
            if arg in element.values():
                del data[key][i]
                break

        self.edit(key, data[key])


'''
test

# edit
jay = pyJson('../../data/data.json')
jay.edit('description', 'description test')
print jay.read('description')

# read a specific element
print jay.read('links')[0]['url']

# write
jay = pyJson('./test.json')
jay.write({'one':1, 'two':2})

# add
new_link = {'title':'test', 'url':'test.com'}
jay.add('links', new_link)

# remove
jay = pyJson('../../data/data.json')
jay.remove('links', 'test')
'''
