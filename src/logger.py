import os
import sys

class Logger:
    _instance = None

    LOG_LEVELS = {"FATAL": 1, "ERROR": 2, "WARN": 3, "INFO": 4, "DEBUG": 5, "TRACE": 6}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, level="INFO", adapter=None):
        self.level = level
        self.adapter = adapter

    def log(self, message, level):
        if self.LOG_LEVELS[level] <= self.LOG_LEVELS[self.level] and self.adapter:
            self.adapter.write(f"[{level}] {message}")

    def set_adapter(self, adapter: LoggerOutputAdapter):
        self.adapter = adapter