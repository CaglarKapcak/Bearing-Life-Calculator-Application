import sqlite3
import os

class BearingDatabase:
    """Rulman veritabanı yönetimi"""
    
    def __init__(self, db_path="bearings.db"):
        self.db_path = db_path
        self.create_database()
    
    def create_database(self):
        """Veritabanı ve tabloları oluşturur"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bearings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bearing_name TEXT NOT NULL,
                dynamic_load REAL NOT NULL,
                bearing_type TEXT NOT NULL,
                static_load REAL,
                bore_diameter REAL,
                outer_diameter REAL,
                width REAL
            )
        ''')
        
        # Örnek rulman verilerini ekle (eğer yoksa)
        cursor.execute("SELECT COUNT(*) FROM bearings")
        count = cursor.fetchone()[0]
        
        if count == 0:
            self.insert_sample_data()
        
        conn.commit()
        conn.close()
    
    def insert_sample_data(self):
        """Örnek rulman verilerini ekler"""
        sample_bearings = [
            # Rulman adı, dinamik yük (kN), tip, statik yük (kN), iç çap (mm), dış çap (mm), genişlik (mm)
            ("6204", 12.8, "ball", 6.65, 20, 47, 14),
            ("6205", 14.0, "ball", 7.85, 25, 52, 15),
            ("6206", 19.5, "ball", 11.2, 30, 62, 16),
            ("6304", 15.9, "ball", 7.9, 20, 52, 15),
            ("6305", 22.5, "ball", 11.5, 25, 62, 17),
            ("6306", 29.6, "ball", 16.0, 30, 72, 19),
            ("NU205", 27.5, "roller", 24.0, 25, 52, 15),
            ("NU206", 36.5, "roller", 32.0, 30, 62, 16),
            ("NU207", 44.0, "roller", 39.0, 35, 72, 17),
            ("NJ205", 28.0, "roller", 24.5, 25, 52, 15),
            ("NJ206", 37.0, "roller", 33.0, 30, 62, 16),
            ("SKF 6204", 13.5, "ball", 7.0, 20, 47, 14),
            ("SKF 6205", 14.8, "ball", 8.3, 25, 52, 15),
            ("FAG 6206", 20.0, "ball", 11.5, 30, 62, 16),
            ("NSK 6304", 16.5, "ball", 8.2, 20, 52, 15),
            ("NSK 6305", 23.0, "ball", 12.0, 25, 62, 17),
        ]
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for bearing in sample_bearings:
            cursor.execute('''
                INSERT INTO bearings (bearing_name, dynamic_load, bearing_type, static_load, bore_diameter, outer_diameter, width)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', bearing)
        
        conn.commit()
        conn.close()
    
    def get_all_bearings(self):
        """Tüm rulmanları getirir"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT bearing_name, dynamic_load, bearing_type FROM bearings ORDER BY dynamic_load")
        bearings = cursor.fetchall()
        
        conn.close()
        return bearings
    
    def get_bearings_by_type(self, bearing_type):
        """Belirli tipteki rulmanları getirir"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT bearing_name, dynamic_load, bearing_type 
            FROM bearings 
            WHERE bearing_type = ?
            ORDER BY dynamic_load
        ''', (bearing_type,))
        
        bearings = cursor.fetchall()
        conn.close()
        return bearings
    
    def recommend_bearing(self, required_dynamic_load, bearing_type):
        """
        Gerekli dinamik yük kapasitesine göre uygun rulman önerir
        
        Args:
            required_dynamic_load: Gereken minimum dinamik yük kapasitesi (N)
            bearing_type: Rulman tipi ("ball" veya "roller")
        
        Returns:
            Önerilen rulman bilgisi (name, dynamic_load) veya None
        """
        # required_dynamic_load'u kN'ye çevir
        required_dynamic_load_kN = required_dynamic_load / 1000
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT bearing_name, dynamic_load, static_load, bore_diameter, outer_diameter, width
            FROM bearings 
            WHERE bearing_type = ? AND dynamic_load >= ?
            ORDER BY dynamic_load ASC
            LIMIT 1
        ''', (bearing_type, required_dynamic_load_kN))
        
        result = cursor.fetchone()
        conn.close()
        
        return result
    
    def add_bearing(self, name, dynamic_load, bearing_type, static_load=None, bore=None, outer=None, width=None):
        """Yeni rulman ekler"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO bearings (bearing_name, dynamic_load, bearing_type, static_load, bore_diameter, outer_diameter, width)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, dynamic_load, bearing_type, static_load, bore, outer, width))
        
        conn.commit()
        conn.close()