import sys

if len(sys.argv) != 2  :
    print("Usage: parser.py <filename>")
    exit(1)

with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        if line.find("Total:") == 0:
            line = ""
        if line.find("Fraud calls detected:") == 0:
            line = "\n" + line
        sys.stdout.write(line)
    infile.close()
exit(0)