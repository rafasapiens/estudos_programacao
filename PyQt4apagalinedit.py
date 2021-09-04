import sys, os
from PyQt5 import QtCore, QtGui,  QtWidgets
class Dialog_01(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()

        myQWidget = QtWidgets.QWidget()
        myBoxLayout = QtWidgets.QVBoxLayout()       


        self.myQLineEdit = QtWidgets.QLineEdit('Type text here')
        self.myQLineEdit.textChanged.connect(self.fixText)

        myBoxLayout.addWidget(self.myQLineEdit)        

        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)
        self.setWindowTitle('Dialog 01')

    def fixText(self, arg):
        arg=str(arg)
        if not arg: return

        arg=self.cleanupString(arg)

        if len(arg)<3: result=arg.upper()
        else:     result = arg[0:4].upper()+arg[4:]
        # resultList=list(result)
        # resultList.insert(4, '_')
        # result=''.join(resultList)
        self.myQLineEdit.blockSignals(True)
        self.myQLineEdit.setText(result)
        self.myQLineEdit.blockSignals(False)

    def cleanupString(self, line=None):
        if line==None: return
     #   invalid = invalid=['!','','#','$','%','&','\\','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',',']','^','`','{','|','}','~', ' ']
        for c in invalid: 
            if len(line)>0: line=line.replace(c,'_')
        return line


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog_1 = Dialog_01()
    dialog_1.show()
    dialog_1.resize(480,320)
    sys.exit(app.exec_())
