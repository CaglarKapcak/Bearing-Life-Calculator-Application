from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QGroupBox,
    QTextEdit, QMessageBox, QSplitter, QFrame, QSpinBox,
    QScrollArea
)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QDoubleValidator, QIntValidator, QColor, QPalette, QLinearGradient, QBrush
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from calculations import BearingCalculator
from database import BearingDatabase

class ModernButton(QPushButton):
    """Modern stil buton sınıfı"""
    def __init__(self, text, color="#2196F3", parent=None):
        super().__init__(text, parent)
        self.color = color
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial;
            }}
            QPushButton:hover {{
                background-color: {self.darken_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.darken_color(color, 0.2)};
            }}
        """)
    
    def darken_color(self, color, factor=0.1):
        """Rengi koyulaştır"""
        if color.startswith('#'):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            r = max(0, int(r * (1 - factor)))
            g = max(0, int(g * (1 - factor)))
            b = max(0, int(b * (1 - factor)))
            return f"#{r:02x}{g:02x}{b:02x}"
        return color

class ModernGroupBox(QGroupBox):
    """Modern stil grup kutusu"""
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                background-color: rgba(255, 255, 255, 0.95);
                border: 2px solid #e0e0e0;
                border-radius: 12px;
                margin-top: 12px;
                padding-top: 10px;
                font-weight: bold;
                font-size: 13px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px 0 8px;
                color: #1976D2;
            }
        """)

class MainWindow(QMainWindow):
    """Ana pencere - Modern tasarım"""
    
    def __init__(self):
        super().__init__()
        self.calculator = BearingCalculator()
        self.database = BearingDatabase()
        self.init_ui()
        self.setup_styles()
        
    def setup_styles(self):
        """Ana pencere stilleri - Düzeltilmiş renkler"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f5f7fa, stop:1 #e9ecef);
            }
            QLabel {
                color: #2c3e50;
                font-size: 12px;
                font-weight: 500;
                font-family: 'Segoe UI', Arial;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #dcdde1;
                border-radius: 8px;
                background-color: white;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                background-color: #ffffff;
            }
            QComboBox {
                padding: 8px;
                border: 2px solid #dcdde1;
                border-radius: 8px;
                background-color: white;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
                color: #2c3e50;
            }
            QComboBox:hover {
                border-color: #2196F3;
            }
            QComboBox:focus {
                border-color: #2196F3;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #2196F3;
                margin-right: 5px;
            }
            /* ComboBox açılır liste stilleri - OKUNABİLİRLİK DÜZELTİLDİ */
            QComboBox QAbstractItemView {
                background-color: white;
                border: 2px solid #2196F3;
                border-radius: 6px;
                padding: 5px;
                selection-background-color: #2196F3;
                selection-color: white;
                outline: none;
                color: #2c3e50;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px 12px;
                margin: 2px;
                border-radius: 4px;
                color: #2c3e50;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #2196F3;
                color: white;
            }
            QTextEdit {
                border: 2px solid #dcdde1;
                border-radius: 8px;
                background-color: white;
                font-family: 'Courier New', monospace;
                font-size: 11px;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #2196F3;
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
    def init_ui(self):
        """Kullanıcı arayüzünü oluşturur"""
        self.setWindowTitle("🎯 Rulman Ömrü ve Seçim Hesaplayıcısı - Professional Edition")
        self.setGeometry(100, 100, 1400, 900)
        
        # Ana widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Başlık
        title_label = QLabel("🔧 RULMAN ANALİZ VE SEÇİM ARACI")
        title_label.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title_label.setStyleSheet("""
            color: #1976D2;
            padding: 15px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(25, 118, 210, 0.1), stop:1 rgba(25, 118, 210, 0.05));
            border-radius: 12px;
            margin-bottom: 10px;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Ana splitter
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.setHandleWidth(2)
        main_splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #bdc3c7;
                width: 2px;
            }
        """)
        
        # Paneller
        left_panel = self.create_input_panel()
        main_splitter.addWidget(left_panel)
        
        middle_panel = self.create_middle_panel()
        main_splitter.addWidget(middle_panel)
        
        right_panel = self.create_results_panel()
        main_splitter.addWidget(right_panel)
        
        main_splitter.setSizes([400, 250, 450])
        
        top_layout = QHBoxLayout()
        top_layout.addWidget(main_splitter)
        
        bottom_panel = self.create_graph_panel()
        
        main_layout.addLayout(top_layout, 2)
        main_layout.addWidget(bottom_panel, 1)
        
    def create_input_panel(self):
        """Sol panel - giriş parametreleri"""
        panel = ModernGroupBox("📊 GİRİŞ PARAMETRELERİ")
        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Rulman tipi
        tip_label = QLabel("🔄 Rulman Tipi:")
        tip_label.setStyleSheet("color: #E67E22; font-weight: bold; font-size: 12px;")
        layout.addWidget(tip_label, 0, 0)
        self.bearing_type = QComboBox()
        self.bearing_type.addItems(["⚪ Ball Bearing (Bilyalı)", "🔴 Roller Bearing (Makaralı)"])
        self.bearing_type.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #FFB74D;
            }
            QComboBox:hover {
                border-color: #E67E22;
            }
        """)
        layout.addWidget(self.bearing_type, 0, 1)
        
        # Dinamik yük
        dyn_label = QLabel("💪 Dinamik Yük (C) [N]:")
        dyn_label.setStyleSheet("color: #27AE60; font-weight: bold;")
        layout.addWidget(dyn_label, 1, 0)
        self.dynamic_load = QLineEdit()
        self.dynamic_load.setValidator(QDoubleValidator(0, 1e6, 2))
        self.dynamic_load.setPlaceholderText("Örn: 12500 N")
        self.dynamic_load.setStyleSheet("background-color: #F1F8E9;")
        layout.addWidget(self.dynamic_load, 1, 1)
        
        # Eşdeğer yük
        eq_label = QLabel("⚖️ Eşdeğer Yük (P) [N]:")
        eq_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
        layout.addWidget(eq_label, 2, 0)
        self.equivalent_load = QLineEdit()
        self.equivalent_load.setValidator(QDoubleValidator(0, 1e6, 2))
        self.equivalent_load.setPlaceholderText("Örn: 5000 N")
        self.equivalent_load.setStyleSheet("background-color: #FFEBEE;")
        layout.addWidget(self.equivalent_load, 2, 1)
        
        # Devir sayısı
        rpm_label = QLabel("🔄 Devir Sayısı (RPM):")
        rpm_label.setStyleSheet("color: #3498DB; font-weight: bold;")
        layout.addWidget(rpm_label, 3, 0)
        self.rpm = QLineEdit()
        self.rpm.setValidator(QIntValidator(1, 100000))
        self.rpm.setPlaceholderText("Örn: 1500 RPM")
        self.rpm.setStyleSheet("background-color: #E3F2FD;")
        layout.addWidget(self.rpm, 3, 1)
        
        # Güvenilirlik - DÜZELTİLDİ: Açılır liste net görünüyor
        rel_label = QLabel("🎯 Güvenilirlik Oranı:")
        rel_label.setStyleSheet("color: #9B59B6; font-weight: bold;")
        layout.addWidget(rel_label, 4, 0)
        self.reliability = QComboBox()
        self.reliability.addItems(["90% (Standart)", "95% (Yüksek)", "96%", "97%", "98%", "99% (Çok Yüksek)"])
        self.reliability.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #9B59B6;
                color: #2c3e50;
            }
            QComboBox:hover {
                border-color: #8E44AD;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        layout.addWidget(self.reliability, 4, 1)
        
        # Şok yük - DÜZELTİLDİ
        shock_label = QLabel("💥 Şok Yük Durumu:")
        shock_label.setStyleSheet("color: #F39C12; font-weight: bold;")
        layout.addWidget(shock_label, 5, 0)
        self.shock_load = QComboBox()
        self.shock_load.addItems(["✅ Normal (1.0)", "⚠️ Hafif Şok (1.2)", "⚡ Orta Şok (1.5)", "💢 Ağır Şok (2.0)"])
        self.shock_load.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #F39C12;
                color: #2c3e50;
            }
            QComboBox:hover {
                border-color: #E67E22;
            }
        """)
        layout.addWidget(self.shock_load, 5, 1)
        
        # Yağlama - DÜZELTİLDİ
        lub_label = QLabel("🛢️ Yağlama Durumu:")
        lub_label.setStyleSheet("color: #16A085; font-weight: bold;")
        layout.addWidget(lub_label, 6, 0)
        self.lubrication = QComboBox()
        self.lubrication.addItems(["✨ İyi (1.0)", "👍 Orta (0.8)", "👎 Kötü (0.6)"])
        self.lubrication.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #16A085;
                color: #2c3e50;
            }
            QComboBox:hover {
                border-color: #138D72;
            }
        """)
        layout.addWidget(self.lubrication, 6, 1)
        
        # Bilgi kartı
        info_card = QFrame()
        info_card.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #E8F0FE, stop:1 #F0E8FE);
                border-radius: 10px;
                padding: 10px;
                margin-top: 10px;
            }
        """)
        info_layout = QVBoxLayout(info_card)
        info_text = QLabel(
            "📌 HESAPLAMA BİLGİLERİ\n\n"
            "• Bilyalı rulmanlar için p = 3\n"
            "• Makaralı rulmanlar için p = 10/3\n"
            "• Tüm yük değerleri Newton (N) cinsindendir\n"
            "• L10 ömrü ISO 281 standardına göre hesaplanır"
        )
        info_text.setStyleSheet("color: #2c3e50; font-size: 10px;")
        info_text.setWordWrap(True)
        info_layout.addWidget(info_text)
        layout.addWidget(info_card, 7, 0, 1, 2)
        
        layout.setRowStretch(8, 1)
        panel.setLayout(layout)
        
        scroll = QScrollArea()
        scroll.setWidget(panel)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        return scroll
    
    def create_middle_panel(self):
        """Orta panel - butonlar"""
        panel = ModernGroupBox("⚡ İŞLEMLER")
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 30, 20, 30)
        
        self.calc_button = ModernButton("🚀 HESAPLA", "#27AE60")
        self.calc_button.setMinimumHeight(60)
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)
        
        self.recommend_button = ModernButton("💡 RULMAN ÖNER", "#E67E22")
        self.recommend_button.setMinimumHeight(60)
        self.recommend_button.clicked.connect(self.recommend_bearing)
        layout.addWidget(self.recommend_button)
        
        self.clear_button = ModernButton("🗑️ TEMİZLE", "#95A5A6")
        self.clear_button.setMinimumHeight(50)
        self.clear_button.clicked.connect(self.clear_inputs)
        layout.addWidget(self.clear_button)
        
        info_button = ModernButton("ℹ️ YARDIM", "#3498DB")
        info_button.setMinimumHeight(50)
        info_button.clicked.connect(self.show_help)
        layout.addWidget(info_button)
        
        layout.addStretch()
        
        tip_card = QFrame()
        tip_card.setStyleSheet("""
            QFrame {
                background: #FFF9C4;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        tip_layout = QVBoxLayout(tip_card)
        tip_label = QLabel("💡 İpucu:")
        tip_label.setStyleSheet("font-weight: bold; color: #F39C12;")
        tip_layout.addWidget(tip_label)
        tip_text = QLabel("Önce 'Hesapla' butonu ile ömrü hesaplayın,\nardından 'Rulman Öner' ile uygun rulmanı seçin.")
        tip_text.setWordWrap(True)
        tip_text.setStyleSheet("color: #7f8c8d; font-size: 11px;")
        tip_layout.addWidget(tip_text)
        layout.addWidget(tip_card)
        
        panel.setLayout(layout)
        return panel
    
    def create_results_panel(self):
        """Sağ panel - sonuçlar"""
        panel = ModernGroupBox("📈 HESAPLAMA SONUÇLARI")
        layout = QVBoxLayout()
        
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setFont(QFont("Consolas", 10))
        self.results_text.setStyleSheet("""
            QTextEdit {
                background-color: #2C3E50;
                color: #ECF0F1;
                border: 2px solid #34495E;
                border-radius: 8px;
                font-family: 'Consolas', 'Courier New', monospace;
            }
        """)
        layout.addWidget(self.results_text)
        
        panel.setLayout(layout)
        return panel
    
    def create_graph_panel(self):
        """Alt panel - grafik"""
        panel = ModernGroupBox("📊 YÜK - ÖMÜR ANALİZ GRAFİĞİ")
        layout = QVBoxLayout()
        
        self.figure = Figure(figsize=(10, 4), facecolor='#f8f9fa')
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#ffffff')
        self.canvas = FigureCanvas(self.figure)
        
        self.ax.grid(True, alpha=0.3, linestyle='--')
        self.ax.set_xlabel('Eşdeğer Yük (P) [N]', fontsize=10, fontweight='bold')
        self.ax.set_ylabel('Ömür (L10h) [saat]', fontsize=10, fontweight='bold')
        self.ax.set_title('Yük - Ömür İlişkisi', fontsize=12, fontweight='bold', color='#1976D2')
        
        layout.addWidget(self.canvas)
        panel.setLayout(layout)
        
        return panel
    
    def show_help(self):
        """Yardım penceresi"""
        help_text = """
        <h2>📖 Rulman Hesaplayıcı Kullanım Kılavuzu</h2>
        
        <h3>🎯 Amaç:</h3>
        <p>Bu uygulama, mühendislik hesaplamaları için rulman ömrünü ISO 281 standardına göre hesaplar ve uygun rulman seçimi yapar.</p>
        
        <h3>📝 Giriş Parametreleri:</h3>
        <ul>
        <li><b>Rulman Tipi:</b> Bilyalı veya makaralı rulman seçimi</li>
        <li><b>Dinamik Yük (C):</b> Rulmanın dinamik yük kapasitesi (Newton)</li>
        <li><b>Eşdeğer Yük (P):</b> Rulmana etki eden eşdeğer yük (Newton)</li>
        <li><b>Devir Sayısı:</b> Rulmanın dönme hızı (RPM)</li>
        <li><b>Güvenilirlik:</b> İstenen güvenilirlik seviyesi (%)</li>
        <li><b>Şok Yük:</b> Çalışma koşullarındaki şok etkisi</li>
        <li><b>Yağlama:</b> Yağlama kalitesi</li>
        </ul>
        
        <h3>🔢 Hesaplama Formülleri:</h3>
        <ul>
        <li>L10 = (C/P)^p (milyon devir)</li>
        <li>L10h = (10^6 / (60 × RPM)) × (C/P)^p (saat)</li>
        <li>Ball bearing için p = 3</li>
        <li>Roller bearing için p = 10/3</li>
        </ul>
        
        <h3>💡 İpuçları:</h3>
        <ul>
        <li>Yük değerleri pozitif olmalıdır</li>
        <li>RPM değeri 0'dan büyük olmalıdır</li>
        <li>Hesaplama sonrası 'Rulman Öner' butonu aktif olur</li>
        <li>Grafik, yük-ömür ilişkisini görselleştirir</li>
        </ul>
        
        <p><b>📞 Destek:</b> Teknik sorularınız için mühendislik birimi ile iletişime geçiniz.</p>
        """
        
        msg = QMessageBox(self)
        msg.setWindowTitle("Yardım - Rulman Hesaplayıcı")
        msg.setTextFormat(Qt.RichText)
        msg.setText(help_text)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
                min-width: 500px;
            }
            QLabel {
                color: #2c3e50;
            }
        """)
        msg.exec()
    
    def validate_inputs(self):
        """Giriş değerlerini doğrular"""
        try:
            if not self.dynamic_load.text():
                QMessageBox.warning(self, "⚠️ Uyarı", "Dinamik yük değerini giriniz!")
                return False
            if not self.equivalent_load.text():
                QMessageBox.warning(self, "⚠️ Uyarı", "Eşdeğer yük değerini giriniz!")
                return False
            if not self.rpm.text():
                QMessageBox.warning(self, "⚠️ Uyarı", "Devir sayısını giriniz!")
                return False
            
            c = float(self.dynamic_load.text())
            p = float(self.equivalent_load.text())
            rpm = int(self.rpm.text())
            
            if c <= 0:
                QMessageBox.warning(self, "⚠️ Uyarı", "Dinamik yük pozitif bir değer olmalıdır!")
                return False
            if p <= 0:
                QMessageBox.warning(self, "⚠️ Uyarı", "Eşdeğer yük pozitif bir değer olmalıdır!")
                return False
            if rpm <= 0:
                QMessageBox.warning(self, "⚠️ Uyarı", "Devir sayısı pozitif bir değer olmalıdır!")
                return False
            
            return True
            
        except ValueError:
            QMessageBox.warning(self, "⚠️ Uyarı", "Geçerli sayısal değerler giriniz!")
            return False
    
    def calculate(self):
        """Hesaplama işlemini yapar"""
        if not self.validate_inputs():
            return
        
        try:
            bearing_type_raw = self.bearing_type.currentText()
            bearing_type = "ball" if "Ball" in bearing_type_raw else "roller"
            c = float(self.dynamic_load.text())
            p = float(self.equivalent_load.text())
            rpm = int(self.rpm.text())
            
            rel_text = self.reliability.currentText()
            reliability = int(rel_text.split('%')[0])
            
            shock_text = self.shock_load.currentText()
            if "Normal" in shock_text:
                shock = "normal"
            elif "Hafif" in shock_text:
                shock = "light_shock"
            elif "Orta" in shock_text:
                shock = "medium_shock"
            else:
                shock = "heavy_shock"
            
            lub_text = self.lubrication.currentText()
            if "İyi" in lub_text:
                lubrication = "good"
            elif "Orta" in lub_text:
                lubrication = "average"
            else:
                lubrication = "poor"
            
            l10 = self.calculator.calculate_l10(bearing_type, c, p)
            l10h = self.calculator.convert_to_hours(l10, rpm)
            lna = self.calculator.apply_reliability_factor(l10h, reliability)
            final_life = self.calculator.apply_operating_conditions(lna, shock, lubrication)
            
            results = f"""
╔══════════════════════════════════════════════════════════════╗
║                    🎯 RULMAN ÖMRÜ HESAP SONUÇLARI            ║
╚══════════════════════════════════════════════════════════════╝

📌 GİRİŞ PARAMETRELERİ
───────────────────────────────────────────────────────────────
  Rulman Tipi          : {bearing_type.upper()}
  Dinamik Yük (C)      : {c:,.0f} N
  Eşdeğer Yük (P)      : {p:,.0f} N
  C/P Oranı            : {c/p:.2f}
  Devir Sayısı         : {rpm:,.0f} RPM

📊 TEMEL ÖMÜR HESABI
───────────────────────────────────────────────────────────────
  • L10 (milyon devir) : {l10:.2f} milyon devir
  • L10h (saat)        : {l10h:,.0f} saat ({self.calculator.get_life_string(l10h)})

🔧 DÜZELTME FAKTÖRLERİ
───────────────────────────────────────────────────────────────
  • Güvenilirlik (%{reliability})  : a₁ = {self.calculator.RELIABILITY_FACTORS[reliability]}
  • Şok Yük Faktörü    : {self.calculator.SHOCK_FACTORS[shock]}
  • Yağlama Faktörü    : {self.calculator.LUBRICATION_FACTORS[lubrication]}

✨ DÜZELTİLMİŞ ÖMÜR
───────────────────────────────────────────────────────────────
  • Lna (saat)         : {final_life:,.0f} saat
  • Okunabilir         : {self.calculator.get_life_string(final_life)}

╔══════════════════════════════════════════════════════════════╗
║  ✅ Hesaplama başarıyla tamamlandı!                          ║
╚══════════════════════════════════════════════════════════════╝
            """
            
            self.results_text.setText(results)
            self.update_graph(bearing_type, c, rpm)
            
        except Exception as e:
            QMessageBox.critical(self, "❌ Hata", f"Hesaplama sırasında hata oluştu:\n{str(e)}")
    
    def update_graph(self, bearing_type, dynamic_load, rpm):
        """Yük-ömür grafiğini günceller"""
        try:
            current_load = float(self.equivalent_load.text())
            load_range = np.linspace(max(10, current_load * 0.1), current_load * 2, 100)
            
            loads, lives = self.calculator.calculate_life_vs_load(
                bearing_type, dynamic_load, rpm, load_range
            )
            
            self.ax.clear()
            
            self.ax.plot(loads, lives, color='#2196F3', linewidth=3, 
                        label='Ömür (L10h)', marker='', linestyle='-')
            self.ax.fill_between(loads, lives, alpha=0.3, color='#2196F3')
            
            current_l10 = self.calculator.calculate_l10(bearing_type, dynamic_load, current_load)
            current_l10h = self.calculator.convert_to_hours(current_l10, rpm)
            self.ax.plot(current_load, current_l10h, 'ro', markersize=10, 
                        markerfacecolor='#E74C3C', markeredgecolor='white', 
                        markeredgewidth=2, label='Çalışma Noktası')
            
            self.ax.set_xlabel('Eşdeğer Yük (P) [N]', fontsize=11, fontweight='bold', color='#2c3e50')
            self.ax.set_ylabel('Ömür (L10h) [saat]', fontsize=11, fontweight='bold', color='#2c3e50')
            self.ax.set_title('Yük - Ömür İlişkisi', fontsize=13, fontweight='bold', color='#1976D2')
            self.ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
            self.ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
            
            if len(lives) > 0 and max(lives) > min(lives) * 100:
                self.ax.set_yscale('log')
                self.ax.set_ylabel('Ömür (L10h) [saat] (Logaritmik Ölçek)', 
                                  fontsize=11, fontweight='bold')
            
            self.ax.set_facecolor('#fafafa')
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['right'].set_visible(False)
            self.ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            
            self.canvas.draw()
            
        except Exception as e:
            print(f"Grafik güncelleme hatası: {e}")
    
    def recommend_bearing(self):
        """Rulman önerisi yapar"""
        try:
            if not self.equivalent_load.text():
                QMessageBox.warning(self, "⚠️ Uyarı", "Rulman önerisi için önce eşdeğer yükü giriniz!")
                return
            
            p = float(self.equivalent_load.text())
            bearing_type_raw = self.bearing_type.currentText()
            bearing_type = "ball" if "Ball" in bearing_type_raw else "roller"
            
            required_c = p * 1.2
            
            recommended = self.database.recommend_bearing(required_c, bearing_type)
            
            if recommended:
                name, dynamic_load, static_load, bore, outer, width = recommended
                message = f"""
╔══════════════════════════════════════════════════════════════╗
║                    🎯 RULMAN ÖNERİSİ                         ║
╚══════════════════════════════════════════════════════════════╝

📌 ÖNERİLEN RULMAN
───────────────────────────────────────────────────────────────
  Rulman Kodu        : {name}
  Rulman Tipi        : {bearing_type.upper()}
  Dinamik Yük (C)    : {dynamic_load:.1f} kN ({dynamic_load*1000:.0f} N)
  Statik Yük (C₀)    : {static_load:.1f} kN

📐 TEKNİK ÖZELLİKLER
───────────────────────────────────────────────────────────────
  İç Çap (d)         : {bore:.1f} mm
  Dış Çap (D)        : {outer:.1f} mm
  Genişlik (B)       : {width:.1f} mm

⚙️ UYGUNLUK ANALİZİ
───────────────────────────────────────────────────────────────
  Gereken Min. Yük   : {required_c:.0f} N
  Güvenlik Faktörü   : {dynamic_load*1000/required_c:.2f}
  C/P Oranı          : {(dynamic_load*1000)/p:.2f}

╔══════════════════════════════════════════════════════════════╗
║  ✅ {name} rulmanı uygulamanız için idealdir!                ║
╚══════════════════════════════════════════════════════════════╝
                """
                
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("✅ Rulman Önerisi")
                msg_box.setText(message)
                msg_box.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        min-width: 500px;
                    }
                    QLabel {
                        color: #2c3e50;
                        font-family: 'Consolas', monospace;
                    }
                """)
                msg_box.exec()
            else:
                QMessageBox.warning(self, "⚠️ Uyarı", 
                    f"Seçilen kriterlere uygun rulman bulunamadı.\n"
                    f"Gereken minimum dinamik yük: {required_c:.0f} N\n\n"
                    f"💡 Öneri: Daha yüksek kapasiteli rulmanlar için veritabanını genişletin.")
                
        except Exception as e:
            QMessageBox.critical(self, "❌ Hata", f"Öneri sırasında hata oluştu:\n{str(e)}")
    
    def clear_inputs(self):
        """Giriş alanlarını temizler"""
        self.dynamic_load.clear()
        self.equivalent_load.clear()
        self.rpm.clear()
        self.results_text.clear()
        
        self.ax.clear()
        self.ax.set_xlabel('Eşdeğer Yük (P) [N]', fontsize=10, fontweight='bold')
        self.ax.set_ylabel('Ömür (L10h) [saat]', fontsize=10, fontweight='bold')
        self.ax.set_title('Yük - Ömür Grafiği', fontsize=12, fontweight='bold')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_facecolor('#f8f9fa')
        self.canvas.draw()
        
        QMessageBox.information(self, "✨ Temizlendi", "Tüm alanlar temizlendi. Yeni hesaplama yapabilirsiniz.")