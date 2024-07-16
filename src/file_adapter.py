from .logger_output_adapter import LoggerOutputAdapter

class FileLoggerAdapter(LoggerOutputAdapter):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, message):
        with open(self.file_path, "a") as file:
            file.write(message + "\n")