import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)

# Saya menggunakan AI untuk membuat kode ini dengan mempelajari juga setiap barisnya
# untuk memahami cara kerja dan mengumpulkan tugas dengan cepat

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Konversi Suhu")
        self.resize(400, 300)

        # Input Celsius
        self.celsius_input = QLineEdit()
        self.celsius_input.setPlaceholderText("Masukkan suhu dalam Celsius")

        # Tombol konversi
        self.btn_fahrenheit = QPushButton("Konversi ke Fahrenheit")
        self.btn_kelvin = QPushButton("Konversi ke Kelvin")
        self.btn_reamur = QPushButton("Konversi ke Reamur")

        # Label hasil
        self.result_label = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Input Suhu (Celsius):"))
        layout.addWidget(self.celsius_input)
        layout.addWidget(self.btn_fahrenheit)
        layout.addWidget(self.btn_kelvin)
        layout.addWidget(self.btn_reamur)
        layout.addWidget(QLabel("Hasil:"))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Event handling
        self.btn_fahrenheit.clicked.connect(self.konversi_fahrenheit)
        self.btn_kelvin.clicked.connect(self.konversi_kelvin)
        self.btn_reamur.clicked.connect(self.konversi_reamur)

    def get_celsius(self):
        """Ambil nilai Celsius dari input, validasi angka"""
        try:
            return float(self.celsius_input.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Input Tidak Valid", "Masukkan angka yang benar!")
            return None

    def konversi_fahrenheit(self):
        c = self.get_celsius()
        if c is not None:
            f = (c * 9/5) + 32
            self.result_label.setText(f"{c:.2f} °C = {f:.2f} °F")

    def konversi_kelvin(self):
        c = self.get_celsius()
        if c is not None:
            k = c + 273.15
            self.result_label.setText(f"{c:.2f} °C = {k:.2f} K")

    def konversi_reamur(self):
        c = self.get_celsius()
        if c is not None:
            r = c * 4/5
            self.result_label.setText(f"{c:.2f} °C = {r:.2f} °Re")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())