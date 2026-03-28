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
