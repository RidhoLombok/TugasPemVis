import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout, QMessageBox
)
# Saya menggunakan AI untuk membuat kode ini dengan mempelajari juga setiap barisnya
# untuk memahami cara kerja
class BiodataForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 350)

        # Input Nama
        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Masukkan Nama")

        # Input NIM
        self.nim_input = QLineEdit()
        self.nim_input.setPlaceholderText("Masukkan NIM")

        # Input Kelas
        self.kelas_input = QLineEdit()
        self.kelas_input.setPlaceholderText("Contoh: TI-2A")

        # ComboBox Jenis Kelamin
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Laki-laki", "Perempuan"])

        # Tombol
        self.show_button = QPushButton("Tampilkan")
        self.reset_button = QPushButton("Reset")

        # Label hasil
        self.result_label = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nama:"))
        layout.addWidget(self.nama_input)
        layout.addWidget(QLabel("NIM:"))
        layout.addWidget(self.nim_input)
        layout.addWidget(QLabel("Kelas:"))
        layout.addWidget(self.kelas_input)
        layout.addWidget(QLabel("Jenis Kelamin:"))
        layout.addWidget(self.gender_combo)
        layout.addWidget(self.show_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(QLabel("Hasil:"))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Event handling
        self.show_button.clicked.connect(self.tampilkan_data)
        self.reset_button.clicked.connect(self.reset_form)

    def tampilkan_data(self):
        nama = self.nama_input.text().strip()
        nim = self.nim_input.text().strip()
        kelas = self.kelas_input.text().strip()
        gender = self.gender_combo.currentText()

        # Validasi
        if not nama or not nim or not kelas or not gender:
            QMessageBox.warning(self, "Validasi Gagal", "Semua field harus diisi!")
            return

        # Tampilkan hasil
        self.result_label.setText(
            f"Nama: {nama}\nNIM: {nim}\nKelas: {kelas}\nJenis Kelamin: {gender}"
        )

    def reset_form(self):
        self.nama_input.clear()
        self.nim_input.clear()
        self.kelas_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BiodataForm()
    window.show()
    sys.exit(app.exec())