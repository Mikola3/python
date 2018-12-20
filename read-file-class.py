class Filereader():
    """ Class for task"""
    def __init__(self, file):
        """Initiate our file"""
        self.file = file

    def read(self):
        """Read file"""
        try:
            return open(self.file, 'r').read()
        except FileNotFoundError:
            return ""


reader = Filereader("dev/scripts/helper.py")
print(reader.read())
