import re, sys
from collections import Counter
def count_errors(text):
    c = Counter()
    for line in text.splitlines():
        if "ERROR" in line: c["ERROR"] += 1
        elif "WARNING" in line or "WARN" in line: c["WARNING"] += 1
        elif "CRITICAL" in line: c["CRITICAL"] += 1
    return dict(c)
def count_file(path):
    return count_errors(open(path, encoding="utf-8", errors="ignore").read())
if __name__ == "__main__":
    print(count_file(sys.argv[1]))
