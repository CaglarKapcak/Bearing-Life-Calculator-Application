import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ui import MainWindow

def main():
    # Yüksek DPI desteği
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    
    # Uygulama genel stil
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()