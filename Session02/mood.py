print("Hello world! I'm Mr. Moody")
from random import randrange
n = randrange(1, 31)
if n < 30:
    print("""┈┈┈╭━━━━━╮┈┈┈┈┈
┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈
┈┈┈┃┊┊╭━╮┻╮┈┈┈┈
┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈
┈┈╭┻┊┊╰━┻━╮┈┈┈┈
┈┈╰┳┊╭━━━┳╯┈┈┈┈
┈┈┈┃┊┃╰━━┫┈HOMER
┈┈┈┈┈┈┏━┓┈┈┈┈┈┈ """)

elif n < 60:
    print("Ok, it's fine")
else:
    print("let's rock!!!")
