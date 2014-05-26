#!/usr/bin/env python  
#coding=utf-8  
from PyQt4.QtGui  import *  
from PyQt4.QtCore import *    
class MyDialog(QDialog):  
    def __init__(self, parent=None):  
        super(MyDialog, self).__init__(parent)  
        self.MyTable = QTableWidget(4,3)  
        #self.MyTable.setEditTriggers(QAbstractItemView.CurrentChanged) 
        self.MyTable.setHorizontalHeaderLabels(['姓名','身高','体重'])  
          
        newItem = QTableWidgetItem("松鼠")  
        self.MyTable.setItem(0, 0, newItem)  
          
        newItem = QTableWidgetItem("10cm")  
        self.MyTable.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem("60g")  
        self.MyTable.setItem(0, 2, newItem)   


        self.MyCombo = QComboBox()  
        self.MyCombo.addItem("√")  
        self.MyCombo.addItem("×")           
        self.MyTable.setCellWidget(1,0,self.MyCombo)  


        lv = QListView()  
        itemmode = QStandardItemModel()
        itemmode.appendRow(QStandardItem("a"))
        itemmode.appendRow(QStandardItem("b"))
        lv.setModel(itemmode)
        lv.setFixedSize(200,300)
        self.MyTable.setCellWidget(1,2,lv)  


        lw = QListWidget()  
        lw.addItem("a")
        lw.addItem("b")
        self.MyTable.setCellWidget(2,1,lw)  
        
        layout = QHBoxLayout()  
        layout.addWidget(self.MyTable)  
        self.setLayout(layout)      
          
          
if __name__ == '__main__':  
    import sys  
    app = QApplication(sys.argv)  
    myWindow = MyDialog()  
    myWindow.show()  
    sys.exit(app.exec_())         
