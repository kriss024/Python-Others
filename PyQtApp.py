# Signals and slots example.

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

def greeting():
    # Slot function.
    if msg.text():
        msg.setText('')
    else:
        msg.setText('<h1>Hello World!</h1>')

app = QApplication(sys.argv)
app.setStyle('Fusion')

window = QWidget()
window.setWindowTitle('Signals and slots')
window.setWindowIcon(QIcon('data-science.jpg'))
window.resize(320, 200)

layout = QVBoxLayout()

btn = QPushButton('Show')
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel()
layout.addWidget(msg)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())