import os

def code_file_name(instance, filename):
    print(instance.id)
    filename = "%s.py" % (instance.id)
    return os.path.join('code', filename)