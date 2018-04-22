from PyQt5 import QtWidgets as Qw, QtCore as Qc, QtGui as Qg
import sys

class VerticalScrollbar1(Qw.QScrollBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("""
            QScrollBar:vertical {
                background: #ffffff;
                width: 10px;

            }
            QScrollBar::handle:vertical {
                border: 1px;
                border-radius: 8px;
                background: #f0f0f0;
                width: 10px;
            }
        """)

class HorizontalScrollbar1(Qw.QScrollBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("""
            QScrollBar:horizontal {
                background: #ffffff;
                height: 10px;

            }
            QScrollBar::handle:horizontal {
                border: 1px;
                border-radius: 8px;
                background: #f0f0f0;
                height: 10px;
            }
        """)

def main():
    app = Qw.QApplication(sys.argv)

    widget = Qw.QWidget()
    widget.resize(300, 600)
    widget.setStyleSheet('QWidget{background-color:white;color:white;}') #글씨, 배경 하얀색
    hlayout = Qw.QVBoxLayout()
    widget.setLayout(hlayout)
    hlayout.setAlignment(Qc.Qt.AlignHCenter)
    textedit1 = Qw.QPlainTextEdit()
    hs1 = HorizontalScrollbar1()
    vs1 = VerticalScrollbar1()
    textedit1.setHorizontalScrollBar(hs1)
    textedit1.setStyleSheet('QPlainTextEdit{background-color:white;}')
    textedit1.setVerticalScrollBar(vs1)
    textedit1.setLineWrapMode(0)
    textedit1.insertPlainText(('#'*100+'\n')*100)
    textedit1.setFocusPolicy(Qc.Qt.NoFocus)
    hlayout.addWidget(textedit1)
    widget.show()
    app.exec()

if __name__ == '__main__':
    main()