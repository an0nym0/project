# import traceback
# errors = open("error.txt", "r+")
#
# try:
#     f2 = open("file2.txt", "r")
    # for pos in range(-1, 1):
    #     f.write("row %s\n" % pos)

    # f2.close()
    # f = open("file2.txt", "r")
    # for line in f.readlines():
    #     print(line)

# except Exception as e:
    # f = open("error.txt", "r+")
    #     f.write("error is: %s" % e)
    # f.close()
    # errors.write(traceback.format_exc())

# errors.write("END\n")
# errors.close()

f = open("error.txt", "r")
for line in f.readlines():
    print(line)
f.close()