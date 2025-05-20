from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from mi_formulario import Ui_Dialog  # Importa la clase Ui_Dialog
import sys

class MiDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar la señal del botón "Agregar Propietario"
        self.ui.AgregarP.clicked.connect(self.agregar_propietario)

        # Conectar la señal del botón "Agregar Finca"
        self.ui.AgregarP_2.clicked.connect(self.agregar_finca)

    def agregar_propietario(self):
        doc_id = self.ui.DocID.text()
        nombre = self.ui.Nom.text()
        apellido = self.ui.Apellido.text()
        celular = self.ui.Cel.text()
        correo = self.ui.Mail.text()

        if not doc_id or not nombre or not apellido or not celular or not correo:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos del propietario.")
        else:
            # Aquí iría la lógica para guardar la información del propietario
            QMessageBox.information(self, "Éxito", "Propietario agregado exitosamente.")
            self.limpiar_campos_propietario()

    def agregar_finca(self):
        cultivo = self.ui.DocID_2.text()
        registro_castral = self.ui.DocID_4.text()
        municipio = self.ui.DocID_3.text()

        if not cultivo or not registro_castral or not municipio:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos de la finca.")
        else:
            # Aquí iría la lógica para guardar la información de la finca
            QMessageBox.information(self, "Éxito", "Finca agregada exitosamente.")
            self.limpiar_campos_finca()

    def limpiar_campos_propietario(self):
        self.ui.DocID.clear()
        self.ui.Nom.clear()
        self.ui.Apellido.clear()
        self.ui.Cel.clear()
        self.ui.Mail.clear()

    def limpiar_campos_finca(self):
        self.ui.DocID_2.clear()
        self.ui.DocID_4.clear()
        self.ui.DocID_3.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = MiDialogo()
    dialogo.show()
    sys.exit(app.exec_())