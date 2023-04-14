class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        with open(self.filename, 'w') as f:
            pass  # Тут создается файл без записи в него. Запись в методе далее.

    def write_to_file(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)

    def delete_file(self):
        import os
        try:
            os.remove(self.filename)
            print(f"{self.filename} deleted successfully")
        except OSError as e:
            print(f"Error deleting file: {e.filename} - {e.strerror}")

if __name__ == '__main__':
    fm = FileManager('example.txt')
    fm.create_file()
    fm.write_to_file('Hello, world!')
    fm.delete_file()
