from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

title = "Lider Ahenk Status"
activeMsg = "Lider Ahenk is active."
inactiveMsg = "Lider Ahenk is not active."

def liderAhenkStatus():
    # TODO : get lider ahenk status
    r = random.randint(0, 1)
    if r:
        # service is active
        tray.showMessage(title, activeMsg, icon, 100)
    else:
        # service is inactive
        tray.showMessage(title, inactiveMsg, icon, 100)

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("liderahenk.jpeg")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action = QAction("Status")
action.triggered.connect(liderAhenkStatus)
menu.addAction(action)

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()
