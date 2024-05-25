# 6.4.1 ctl.py
class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        pass
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)

# class Control:
#     def __init__(self, view):
#         self.view = view
#         self.connectSignals()
        
#     def connectSignals(self):
#         self.view.btn1.clicked.connect(self.view.activateMessage)
#         self.view.btn2.clicked.connect(self.view.clearMessage)


# ch 5.2.1 ctrl.pyversions
#class Control:
#    def __init__(self, view):
#        self.view = view
#        self.connectSignals()

#    def connectSignals(self):
#        self.view.btn1.clicked.connect(self.view.activateMessage)
#        self.view.btn2.clicked.connect(self.view.clearMessage)
