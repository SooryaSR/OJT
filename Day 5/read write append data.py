 #Create a class called FileProcessor with methods to read data from a file, write data to a file, and append data to an existing file.

class FileProcessor:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."

    @staticmethod
    def write_to_file(filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    @staticmethod
    def append_to_file(filename, data):
        with open(filename, 'a') as file:
            file.write(data)

FileProcessor.write_to_file("myfile.txt", "Hello, World!")
print(FileProcessor.read_file("myfile.txt"))

FileProcessor.append_to_file("myfile.txt", "\nThis is a new line.")
print(FileProcessor.read_file("myfile.txt"))
