#!/usr/bin/python3
"""
  Read stdin line by line and compute metrics
"""

import sys


def parse_log():
  status_codes = [200, 301, 400, 403, 404, 405, 500]

  stdin_log = {"file_size": 0, "code_list": {str(code): 0 for code in status_codes}}

  return stdin_log
  pass

def print_code(log):
  print("File size: {}".format(log["file_size"]))

  sort_code = sorted(log["code_list"])

  for code in sort_code:
    if log["code_list"][code]:
      print(f"{code}: {log['code_list'][code]}")



def parse_stdin_line(line, regex, log):
  match = regex.fullmatch(line)

  if match:
    stat_code, file_size = match.group(1, 2)

    log["file_size"] += int(file_size)

    if stat_code.isdecimal():
      log["code_list"][stat_code] += 1
  return log

def main():
  regex = ""

  log = parse_log()
  line_count = 0

  for line in sys.stdin:
    line = line.strip()

    line_count += 1

    parsed_log = parse_stdin_line(line, regex, log)

    if line_count % 10 == 0:
      print_code(parsed_log)

if __name__ == "__main__":
  main()