import logging


class LoggingSetup:
    """
    This class manages a logging file that catches and records
    important scenarios during tests running.
    """

    (logging.basicConfig
     (filename="../../../orange_hrm_logging_file.log",
      level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:',
      force=True))


