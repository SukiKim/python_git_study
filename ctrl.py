# 6.6.2 ctrl.py
class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator =self.view.cb.currentText()
        
        if operator =='+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        
        else:
            return "Calculation Error"
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)
        
    def sum(self, a, b):
        try:
            return a+b
        except:
            return "Calculation Error"
        


        
# # 6.4.4 ctrl.py
# class Control:
#     def __init__(self, view):
#         self.view = view
#         self.connectSignals()
        
#     def calculate(self):
#         pass
        
#     def connectSignals(self):
#         self.view.btn1.clicked.connect(self.calculate)
#         self.view.btn2.clicked.connect(self.view.clearMessage)
        
#     def sum(self, a, b):
#         try:
#             return a+b
#         except:
#             return "Calculation Error"



# # 6.4.1 ctrl.py
# # class Control:
# #     def __init__(self, view):
# #         self.view = view
# #         self.connectSignals()
        
# #     def calculate(self):
# #         pass
        
# #     def connectSignals(self):
# #         self.view.btn1.clicked.connect(self.calculate)
# #         self.view.btn2.clicked.connect(self.view.clearMessage)
        
# #     def sum(self, a, b):
# #        return a+b

# # class Control:
# #     def __init__(self, view):
# #         self.view = view
# #         self.connectSignals()
        
# #     def connectSignals(self):
# #         self.view.btn1.clicked.connect(self.view.activateMessage)
# #         self.view.btn2.clicked.connect(self.view.clearMessage)


# # ch 5.2.1 ctrl.pyversions
# #class Control:
# #    def __init__(self, view):
# #        self.view = view
# #        self.connectSignals()

# #    def connectSignals(self):
# #        self.view.btn1.clicked.connect(self.view.activateMessage)
# #        self.view.btn2.clicked.connect(self.view.clearMessage)
