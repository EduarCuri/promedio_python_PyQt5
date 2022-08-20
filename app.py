import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import calculos as operaciones

class Ejemplo01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ejercicio01.ui",self)
        self.initUi()
    
    def initUi(self):
        self.btnuevo.clicked.connect(self.nuevo)
        self.btcalcular.clicked.connect(self.calcular)
        self.btsalir.clicked.connect(self.salir)

    def nuevo(self, e):
        self.tnombre.setText("")
        self.tnota1.setText("")
        self.tnota2.setText("")
        self.tnota3.setText("")
        self.lblpromedio.setText("")
        self.lblobs.setText("")
        self.tnombre.setFocus()

    def calcular(self, e):
        # strip limpia los espacios en derecha o izquierda y solo deja el contenido
        n1 = float(self.tnota1.text().strip())
        n2 = float(self.tnota2.text().strip())
        n3 = float(self.tnota3.text().strip())
        promedio = operaciones.calcularpromedio(n1, n2, n3)
        self.lblpromedio.setText(str(round(promedio,0)))
        self.lblobs.setText(operaciones.calcularobservacion(promedio))

    def salir(self, e):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana01 = Ejemplo01()
    ventana01.show()
    sys.exit(app.exec_())
