class FileReader:
    def read(self):
        print("Reading data from file...")

class FileWriter:
    def write(self):
        print("Writing data to file...")

class FileManager(FileReader, FileWriter):
    def delete(self):
        print("Deleting file...")

fm = FileManager()

fm.read()
fm.write()
fm.delete()