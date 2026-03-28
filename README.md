# Bearing Life Calculator - Professional Engineering Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![PySide6](https://img.shields.io/badge/PySide6-6.6%2B-green.svg)](https://pypi.org/project/PySide6/)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

A professional desktop application for bearing life calculation and selection according to ISO 281 standards. This engineering tool provides accurate life predictions, reliability adjustments, and intelligent bearing recommendations.

![Bearing Life Calculator Screenshot](screenshots/main_window.png)

## 📋 Table of Contents
- [Features](#-features)
- [Technical Specifications](#-technical-specifications)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Calculation Methodology](#-calculation-methodology)
- [Project Structure](#-project-structure)
- [Database Schema](#-database-schema)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

### Core Functionality
- **ISO 281 Standard Calculations**: L10 life calculation with exponent p=3 for ball bearings and p=10/3 for roller bearings
- **Reliability Adjustment**: Support for multiple reliability levels (90%, 95%, 96%, 97%, 98%, 99%) with corresponding a₁ factors
- **Operating Conditions**: Adjustments for shock loads and lubrication conditions
- **Visual Analytics**: Real-time load-life relationship graphs using Matplotlib
- **Intelligent Recommendations**: Automatic bearing selection based on calculated requirements

### User Interface
- **Modern Design**: Clean, professional interface with intuitive layout
- **Color-Coded Inputs**: Visual categorization of different parameter types
- **Real-time Validation**: Input validation with user-friendly error messages
- **Interactive Graphs**: Dynamic load-life curves with current operating point highlighting
- **Comprehensive Results**: Detailed calculation outputs with formatted results

### Technical Features
- **SQLite Database**: Built-in bearing database with expandable library
- **Modular Architecture**: Separated concerns for calculations, database, and UI
- **High DPI Support**: Optimized for modern high-resolution displays
- **Cross-Platform**: Runs on Windows, Linux, and macOS

## 🔧 Technical Specifications

### Technology Stack
## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| 🐍 Python | 3.8+ | Core programming language for application logic |
| 🎨 PySide6 | 6.6.0+ | Modern GUI framework with Qt6 bindings |
| 📊 NumPy | 1.24.0+ | High-performance numerical computations |
| 🔬 SciPy | 1.10.0+ | Scientific and engineering calculations |
| 📈 Matplotlib | 3.7.0+ | Real-time data visualization and plotting |
| 🗄️ SQLite3 | Built-in | Embedded database for bearing library |

### Additional Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| pytest | ≥ 7.0 | Unit testing framework |
| black | ≥ 23.0 | Code formatter |
| flake8 | ≥ 6.0 | Code linting |


### System Requirements
- **OS**: Windows 10/11, Linux (Ubuntu 20.04+), macOS 11+
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 200MB
- **Display**: 1280x720 minimum resolution

## 📦 Installation

### Method 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/bearing-life-calculator.git
cd bearing-life-calculator

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```
### Method 2: Using setup.py

 # Install the package
python setup.py install

# Run the application
bearing-calculator

### Dependencies (requirements.txt)
PySide6>=6.6.0
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0

📖 Usage Guide
Step-by-Step Tutorial
# 1. Input Parameters
Enter the following values in the left panel:

Parameter	Description	Example
Bearing Type	Select between ball and roller bearings	Ball Bearing
Dynamic Load (C)	Bearing's dynamic load capacity (N)	12500 N
Equivalent Load (P)	Actual load on bearing (N)	5000 N
RPM	Rotational speed	1500 RPM
Reliability	Desired reliability level	95%
Shock Load	Operating shock conditions	Medium Shock
Lubrication	Lubrication quality	Good

# 2. Calculate Life
Click the "HESAPLA" (Calculate) button to perform calculations. The results will appear in the right panel with:
Basic L10 life (million revolutions)
L10h life (hours)
Adjusted life with reliability factor
Final life with operating conditions

# 3. View Graph
The bottom panel displays a load-life relationship graph showing:
How life changes with load variations
Current operating point marked in red
Logarithmic scale for large life ranges

# 4. Get Recommendations
Click "RULMAN ÖNER" (Recommend Bearing) to get intelligent bearing suggestions based on:

Required dynamic load capacity (C > 1.2 × P)
Selected bearing type
Available database entries
Input Validation
The application validates all inputs:
No empty fields allowed
Positive numeric values only
RPM > 0
Appropriate value ranges


### 🧮 Calculation Methodology
Basic Life Calculation (L10)

For Ball Bearings:     L10 = (C/P)³
For Roller Bearings:   L10 = (C/P)^(10/3)

Where:
- L10 = Basic rating life (million revolutions)
- C = Dynamic load capacity (N)
- P = Equivalent dynamic load (N)

# Life in Hours (L10h)
L10h = (10⁶ / (60 × RPM)) × (C/P)^p
# Reliability Adjustment (Lna)

Lna = a₁ × L10h

# Reliability Factors (a₁):
- 90%: a₁ = 1.00
- 95%: a₁ = 0.62
- 96%: a₁ = 0.53
- 97%: a₁ = 0.44
- 98%: a₁ = 0.33
- 99%: a₁ = 0.21

# Operating Condition Factors
Condition	Factor
Normal Shock	1.0
Light Shock	1.2
Medium Shock	1.5
Heavy Shock	2.0
Good Lubrication	1.0
Average Lubrication	0.8
Poor Lubrication	0.6

 # Final Adjusted Life
Ladjusted = Lna / (Shock Factor × Lubrication Factor)


