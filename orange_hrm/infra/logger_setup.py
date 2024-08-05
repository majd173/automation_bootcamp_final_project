import logging


class LoggingSetup:
    # This class manages a logging file that catches and records
    # important scenarios during tests running.
    (logging.basicConfig
     (filename=r"C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm_logging_file.log",
      level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:',
      force=True))


