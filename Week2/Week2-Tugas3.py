import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QCheckBox, QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt

class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Login")
        self.resize(400, 250)

        # Input Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Masukkan Username")

        # Input Password (default tersembunyi)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Masukkan Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Checkbox toggle password
        self.show_password_cb = QCheckBox("Tampilkan Password")
        self.show_password_cb.toggled.connect(self.toggle_password)

        # Tombol
        self.login_button = QPushButton("Login")
        self.reset_button = QPushButton("Reset")

        # Label hasil
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.show_password_cb)
        layout.addWidget(self.login_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # Event handling
        self.login_button.clicked.connect(self.validasi_login)
        self.reset_button.clicked.connect(self.reset_form)

    def toggle_password(self, checked):
        """Toggle password visibility"""
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)   # tampilkan
        else:
            self.password_input.setEchoMode(QLineEdit.Password) # sembunyikan

    def validasi_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if username == "admin" and password == "12345":
            self.result_label.setText("Login Berhasil!")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.result_label.setText("Login Gagal!")
            self.result_label.setStyleSheet("color: red;")

    def reset_form(self):
        self.username_input.clear()
        self.password_input.clear()
        self.show_password_cb.setChecked(False)  # otomatis sembunyikan kembali
        self.result_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLogin()
    window.show()
    sys.exit(app.exec())