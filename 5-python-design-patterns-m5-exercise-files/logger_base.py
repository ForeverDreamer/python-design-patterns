import datetime
from singleton_base import Singleton


class Logger(Singleton):

    def __init__(self, path):
        if self._log_file is None:
            self._log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s: %s\n' % (now, log_record)
        self._log_file.write(record)

    def close_log(self):
        self._log_file.close()
        self._log_file = None
