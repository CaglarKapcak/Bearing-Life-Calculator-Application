import numpy as np
import math

class BearingCalculator:
    """Rulman hesaplamaları için ana sınıf"""
    
    # Güvenilirlik faktörleri (a1)
    RELIABILITY_FACTORS = {
        90: 1.0,
        95: 0.62,
        96: 0.53,
        97: 0.44,
        98: 0.33,
        99: 0.21
    }
    
    # Şok yük faktörleri
    SHOCK_FACTORS = {
        "normal": 1.0,
        "light_shock": 1.2,
        "medium_shock": 1.5,
        "heavy_shock": 2.0
    }
    
    # Yağlama faktörleri
    LUBRICATION_FACTORS = {
        "good": 1.0,
        "average": 0.8,
        "poor": 0.6
    }
    
    @staticmethod
    def calculate_l10(bearing_type, dynamic_load, equivalent_load):
        """
        Temel L10 ömrünü hesaplar (milyon devir)
        
        Args:
            bearing_type: "ball" veya "roller"
            dynamic_load: Dinamik yük kapasitesi (N)
            equivalent_load: Eşdeğer yük (N)
        
        Returns:
            L10 ömrü (milyon devir)
        """
        if equivalent_load <= 0:
            return 0
        
        p = 3 if bearing_type == "ball" else 10/3
        ratio = dynamic_load / equivalent_load
        
        return ratio ** p
    
    @staticmethod
    def convert_to_hours(l10, rpm):
        """
        L10 ömrünü saat cinsine çevirir
        
        Args:
            l10: Milyon devir cinsinden ömür
            rpm: Devir sayısı
        
        Returns:
            L10h (saat)
        """
        if rpm <= 0:
            return 0
        
        return (l10 * 1e6) / (60 * rpm)
    
    @staticmethod
    def apply_reliability_factor(l10, reliability_percent):
        """
        Güvenilirlik faktörünü uygular
        
        Args:
            l10: Temel ömür (saat)
            reliability_percent: Güvenilirlik yüzdesi
        
        Returns:
            Düzeltilmiş ömür (saat)
        """
        a1 = BearingCalculator.RELIABILITY_FACTORS.get(reliability_percent, 1.0)
        return l10 * a1
    
    @staticmethod
    def apply_operating_conditions(l10, shock_type, lubrication_type):
        """
        Çalışma koşullarına göre düzeltme faktörlerini uygular
        
        Args:
            l10: Mevcut ömür (saat)
            shock_type: Şok yük tipi
            lubrication_type: Yağlama durumu
        
        Returns:
            Düzeltilmiş ömür (saat)
        """
        shock_factor = BearingCalculator.SHOCK_FACTORS.get(shock_type, 1.0)
        lubrication_factor = BearingCalculator.LUBRICATION_FACTORS.get(lubrication_type, 1.0)
        
        # Çalışma koşulları ömrü azaltır
        total_factor = shock_factor * lubrication_factor
        
        return l10 / total_factor
    
    @staticmethod
    def calculate_life_vs_load(bearing_type, dynamic_load, rpm, load_range):
        """
        Farklı yük değerlerine göre ömür hesaplar (grafik için)
        
        Args:
            bearing_type: "ball" veya "roller"
            dynamic_load: Dinamik yük kapasitesi (N)
            rpm: Devir sayısı
            load_range: Yük aralığı (list)
        
        Returns:
            Yük ve ömür değerleri listeleri
        """
        loads = []
        lives = []
        
        for load in load_range:
            if load > 0:
                l10 = BearingCalculator.calculate_l10(bearing_type, dynamic_load, load)
                l10h = BearingCalculator.convert_to_hours(l10, rpm)
                loads.append(load)
                lives.append(l10h)
        
        return loads, lives
    
    @staticmethod
    def get_life_string(life_hours):
        """
        Ömür değerini okunabilir formata çevirir
        """
        if life_hours < 0:
            return "Geçersiz"
        elif life_hours < 1000:
            return f"{life_hours:.0f} saat"
        elif life_hours < 1e6:
            return f"{life_hours/1000:.1f} bin saat"
        else:
            return f"{life_hours/1e6:.2f} milyon saat"