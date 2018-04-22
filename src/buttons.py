from PyQt5 import QtWidgets as Qw, QtCore as Qc, QtGui as Qg
import sys

class Button1(Qw.QPushButton):

    def __init__(self, text = None, parent = None, size = (100, 30)):
        super().__init__(text = text, parent = parent)
        self.setSizePolicy(Qw.QSizePolicy.Ignored, Qw.QSizePolicy.Ignored)
        self.setFixedSize(*size)
        self.setFocusPolicy(Qc.Qt.NoFocus)
        self.setCursor(Qc.Qt.PointingHandCursor)
        self.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    border: 1px solid #c81414;
                    border-radius: 8px;
                    color: #c81414;
                    font-size: 14px;
                    font-family: "Noto Sans CJK Kr Medium";
                }
                QPushButton:hover:!pressed{
                    background-color: #c81414;
                    border: 1px solid  #c81414;
                    color: #ffffff;
                }
        """)

class Button2(Qw.QPushButton):
    def __init__(self, text = None, parent = None, size=(100, 30)):
        super().__init__(text = text, parent = parent)
        self.setSizePolicy(Qw.QSizePolicy.Ignored, Qw.QSizePolicy.Ignored)
        self.setFixedSize(*size)
        self.setFocusPolicy(Qc.Qt.NoFocus)
        self.setCursor(Qc.Qt.PointingHandCursor)
        self.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    border: none;
                    color: rgba(0,0,0,0.87);
                    font-size: 14px;
                    font-family: "Noto Sans CJK Kr Medium";
                }
                QPushButton:hover:!pressed{
                    color: #c81414;
                }
                QPushButton:pressed{
                    color: rgba(0,0,0,0.87);
                }
        """)

def main():
    app = Qw.QApplication(sys.argv)

    widget = Qw.QWidget()
    widget.resize(300, 600)
    widget.setStyleSheet('QWidget{background-color:white}')
    hlayout = Qw.QVBoxLayout()
    widget.setLayout(hlayout)
    hlayout.setAlignment(Qc.Qt.AlignHCenter)
    btn1 = Button1('버튼1')
    btn2 = Button2('버튼2')
    hlayout.addWidget(btn1)
    hlayout.addWidget(btn2)
    widget.show()
    app.exec()

if __name__ == '__main__':
    main()