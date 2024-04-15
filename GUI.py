#Imports, GPIO is for the raspberry Pi Pins, time is for the sleep method and the QT imports are for the GUI
import RPi.GPIO as GPIO
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

#Sets up GUI window Class
class Window(QMainWindow):
    #Initialises Window Object
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(610, 340, 600, 400)
        self.setWindowTitle("GUI Window")
        self.initUi()
        
    
    #Initialises Buttons
    def initUi(self): 
        #First Radio Button
        self.labelRed = QtWidgets.QLabel(self)
        self.labelRed.setText("Red LED")
        self.labelRed.move(50,100)
        self.bRed = QtWidgets.QRadioButton(self)
        self.bRed.move(70, 125)
        self.bRed.toggled.connect(self.pressRed)
    
        #Second Radio Button
        self.labelBlue = QtWidgets.QLabel(self)
        self.labelBlue.setText("Blue LED")
        self.labelBlue.move(250,100)
        self.bBlue = QtWidgets.QRadioButton(self)
        self.bBlue.move(270, 125)
        self.bBlue.toggled.connect(self.pressBlue)
    
        #Third Radio Button
        self.labelGreen = QtWidgets.QLabel(self)
        self.labelGreen.setText("Green LED")
        self.labelGreen.move(450,100)
        self.bGreen = QtWidgets.QRadioButton(self)
        self.bGreen.move(470, 125)
        self.bGreen.toggled.connect(self.pressGreen)
    
        #Exit Button
        self.bExit = QtWidgets.QPushButton(self)
        self.bExit.setText("Push To Exit")
        self.bExit.move(250, 300)
        self.bExit.clicked.connect(self.pressExit)
        
    #Reacts when the red LED button is pressed
    def pressRed(self):
        #Red is GPIO10
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(9, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        
    #Reacts when the blue LED button is pressed
    def pressBlue(self):
        #Blue is GPIO9
        GPIO.output(10, GPIO.LOW)
        GPIO.output(9, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        
    #Reacts when the green LED button is pressed
    def pressGreen(self):
        #Green is GPIO9
        GPIO.output(10, GPIO.LOW)
        GPIO.output(9, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        
    #Reacts when the exit button is pressed
    def pressExit(self):
        GPIO.output(10, GPIO.LOW)
        GPIO.output(9, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.cleanup()
        self.close

#Method to construct a window object
def CreateWindow():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

#Sets up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

#Calls Window Creation Method
CreateWindow()
