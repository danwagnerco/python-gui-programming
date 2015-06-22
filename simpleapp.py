from PySide.QtCore import *
from PySide.QtGui import *
import sys
import time

app = QApplication(sys.argv)
due = QTime.currentTime()
message = "Alert!"

# >python simpleapp 09:32 Command Options Here
try:
    if len(sys.argv) < 2:
        raise ValueError
    elif len(sys.argv) > 2:
        commands = " ".join(sys.argv[2:])
    else:
        commands = None

    hours, minutes = sys.argv[1].split(":")
    due = QTime(int(hours), int(minutes))

    if not due.isValid():
        raise ValueError

except:
    print("Usage: simpleapp.py HH:MM Optional Message")
    sys.exit(1)

while QTime.currentTime() < due:
    time.sleep(5)

l = "<font color=red size=72> {0} {1}</font>".format(message, commands)
label = QLabel(l)
label.setWindowFlags(Qt.SplashScreen)
label.show()

QTimer.singleShot(10000, app.quit)
app.exec_()

