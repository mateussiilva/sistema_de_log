from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout,QHBoxLayout,QGridLayout
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
        
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        layout = QGridLayout()
        
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('green'),0,1)
        layout.addWidget(Color('blue'),1,0)
        
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
            
    
        
        
if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    janela.show()
    app.exec()