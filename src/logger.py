import threading
from src.logger_output_adapter import LoggerOutputAdapter
from src.console_adapter import ConsoleAdapter

class Logger:
    _instance = None
    _lock = threading.Lock()

    class LogLevel:
        FATAL = 'FATAL'
        ERROR = 'ERROR'
        WARN = 'WARN'
        INFO = 'INFO'
        DEBUG = 'DEBUG'
        TRACE = 'TRACE'

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._log_level = self.LogLevel.INFO
        self._adapter = ConsoleAdapter()

    def set_log_level(self, log_level):
        self._log_level = log_level

    def set_adapter(self, adapter: LoggerOutputAdapter):
        self._adapter = adapter

    def log(self, message, level):
        if level == self._log_level:
            self._adapter.write(message, level)