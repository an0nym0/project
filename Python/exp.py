import traceback


try:
    print("Maybe error")
    raise Exception()
except (Exception, IndexError) as e:
    traceback.format_exc()
except FileNotFoundError:
    print("File not found!")
else:
    print("No error")
finally:
    print("Close file")
    exit()