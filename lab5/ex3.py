import re
import logging
import sys

def critical_logging(line):
    regex_pattern_critical = r'POSSIBLE BREAK-IN ATTEMPT'
    match_critical = re.search(regex_pattern_critical, line)
    if match_critical:
        logging.critical("Oh very no no: " + line)

def error_logging(line):
    logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
    regex_pattern_error = r'error: \w+'
    match_error = re.search(regex_pattern_error, line)
    if match_error:
        logging.error("Oh no: " + line)
    critical_logging(line)
        

def warn_logging(line):
    logging.basicConfig(level=logging.WARN, stream=sys.stdout)
    regex_pattern_warning = r'Failed password|Unknown user'
    match_warning = re.search(regex_pattern_warning, line)
    if match_warning:
        logging.warning("Something went wrong with: " + line)
    error_logging(line)

def info_logging(line):
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    regex_pattern_info = r'Accepted|Connection closed|Disconnecting'
    match_info = re.search(regex_pattern_info, line)
    if match_info:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        logging.info("Everything is fine with:  " + line)
    warn_logging(line)

def debug_logging(line):
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logging.debug("Size: " + str(len(line.encode('utf-8'))))
    info_logging(line)

def show_log(line, min_level=None):
    if min_level == 'DEBUG':
        debug_logging(line)
    elif min_level == 'INFO':
        info_logging(line)
    elif min_level == 'WARNING':
        warn_logging(line)
    elif min_level == 'ERROR':
        error_logging(line)
    elif min_level == 'CRITICAL':
        critical_logging(line)

    
