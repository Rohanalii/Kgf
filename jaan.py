os.system("git pull")
try:
    __import__("jaan").Xyz()
except Exception as e:
    exit(str(e))
