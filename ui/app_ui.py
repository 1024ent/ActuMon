# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTabWidget::pane {
                border: 1px solid #c0c0c0;
                background-color: white;
                border-radius: 5px;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #f0f0f0, stop: 1 #d0d0d0);
                border: 1px solid #c0c0c0;
                border-bottom-color: #c0c0c0;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                min-width: 120px;
                padding: 8px 16px;
                margin-right: 2px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #ffffff, stop: 1 #e6e6e6);
                border-bottom-color: #ffffff;
                color: #2196F3;
            }
            QTabBar::tab:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #ffffff, stop: 1 #f0f0f0);
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 8px;
                margin-top: 15px;
                padding-top: 10px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                background-color: #fafafa;
            }
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #4CAF50, stop: 1 #45a049);
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
                min-height: 25px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #5CBF60, stop: 1 #4CAF50);
            }
            QPushButton:pressed {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #45a049, stop: 1 #3d8b40);
            }
            QDial {
                background-color: #e8e8e8;
                border: 2px solid #cccccc;
                border-radius: 25px;
            }
            QTextBrowser, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 4px;
                background-color: white;
            }
            QLabel {
                color: #333333;
                font-weight: 500;
            }
        """)
        
        # Central widget with main layout
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout for central widget
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Create the tab widget
        self.vibration = QtWidgets.QTabWidget(self.centralwidget)
        self.vibration.setObjectName("vibration")
        self.vibration.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Add tab widget to main layout
        main_layout.addWidget(self.vibration)
        
        # Create tabs
        self.create_control_tab()
        self.create_temperature_tab()
        self.create_current_tab()
        self.create_vibration_tab()
        
        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Create menu bar and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Set up UI text
        self.retranslateUi(MainWindow)
        self.vibration.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_motor_group(self, parent, motor_num, motor_type="Motor"):
        """Create a standardized motor control group"""
        group = QtWidgets.QGroupBox(parent)
        group.setObjectName(f"motor_{motor_num}")
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Main layout for the group
        group_layout = QtWidgets.QHBoxLayout(group)
        group_layout.setContentsMargins(15, 20, 15, 15)
        group_layout.setSpacing(15)
        
        # Left side - Controls
        control_widget = QtWidgets.QWidget()
        control_layout = QtWidgets.QVBoxLayout(control_widget)
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.setSpacing(10)
        
        # Enable button
        enable_btn = QtWidgets.QPushButton("ENABLE")
        enable_btn.setObjectName(f"motor_enable{motor_num}")
        enable_btn.setMaximumWidth(120)
        control_layout.addWidget(enable_btn)
        
        # Status section
        status_layout = QtWidgets.QHBoxLayout()
        status_label = QtWidgets.QLabel("Status:")
        status_label.setObjectName(f"motor_status{motor_num}")
        status_display = QtWidgets.QTextBrowser()
        status_display.setObjectName(f"motor_status_display{motor_num}")
        status_display.setMaximumHeight(40)
        status_layout.addWidget(status_label)
        status_layout.addWidget(status_display)
        control_layout.addLayout(status_layout)
        
        # Speed input section
        speed_input_layout = QtWidgets.QVBoxLayout()
        speed_label = QtWidgets.QLabel("Set Speed:")
        speed_label.setObjectName(f"set_speed{motor_num}")
        speed_input = QtWidgets.QTextEdit()
        speed_input.setObjectName(f"speed_input{motor_num}")
        speed_input.setMaximumHeight(40)
        speed_input_layout.addWidget(speed_label)
        speed_input_layout.addWidget(speed_input)
        control_layout.addLayout(speed_input_layout)
        
        # Speed knob and current speed
        knob_layout = QtWidgets.QHBoxLayout()
        speed_knob = QtWidgets.QDial()
        speed_knob.setObjectName(f"speed_knob{motor_num}")
        speed_knob.setMaximumSize(QtCore.QSize(60, 60))
        speed_knob.setMinimumSize(QtCore.QSize(60, 60))
        
        current_speed_widget = QtWidgets.QWidget()
        current_speed_layout = QtWidgets.QVBoxLayout(current_speed_widget)
        current_speed_layout.setContentsMargins(0, 0, 0, 0)
        current_speed_label = QtWidgets.QLabel("Current Speed:")
        current_speed_label.setObjectName(f"motor_speed{motor_num}")
        current_speed_display = QtWidgets.QTextBrowser()
        current_speed_display.setObjectName(f"motor_speed_display{motor_num}")
        current_speed_display.setMaximumHeight(40)
        current_speed_layout.addWidget(current_speed_label)
        current_speed_layout.addWidget(current_speed_display)
        
        knob_layout.addWidget(speed_knob)
        knob_layout.addWidget(current_speed_widget)
        control_layout.addLayout(knob_layout)
        
        control_layout.addStretch()
        group_layout.addWidget(control_widget, 1)
        
        # Right side - Monitoring plot
        plot_widget = QtWidgets.QWidget()
        plot_widget.setObjectName(f"motor_speed_plot{motor_num}")
        plot_widget.setAutoFillBackground(True)
        plot_widget.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 4px;")
        plot_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        plot_layout = QtWidgets.QVBoxLayout(plot_widget)
        plot_layout.setContentsMargins(10, 10, 10, 10)
        plot_label = QtWidgets.QLabel("Speed Monitoring")
        plot_label.setObjectName(f"speed_mon{motor_num}")
        plot_label.setAlignment(Qt.AlignCenter)
        plot_label.setStyleSheet("font-weight: bold; color: #666;")
        plot_layout.addWidget(plot_label)
        plot_layout.addStretch()
        
        group_layout.addWidget(plot_widget, 2)
        
        return group

    def create_monitoring_group(self, parent, motor_num, monitor_type, icon="📊"):
        """Create a standardized monitoring group"""
        group = QtWidgets.QGroupBox(parent)
        group.setObjectName(f"motor_{monitor_type.lower()}{motor_num}")
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Main layout for the group
        group_layout = QtWidgets.QVBoxLayout(group)
        group_layout.setContentsMargins(15, 20, 15, 15)
        group_layout.setSpacing(10)
        
        # Status section
        status_layout = QtWidgets.QHBoxLayout()
        status_label = QtWidgets.QLabel(f"{monitor_type} Status:")
        status_label.setObjectName(f"{monitor_type.lower()}_status{motor_num}")
        status_display = QtWidgets.QTextBrowser()
        status_display.setObjectName(f"{monitor_type.lower()}_status_display{motor_num}")
        status_display.setMaximumHeight(40)
        status_layout.addWidget(status_label)
        status_layout.addWidget(status_display)
        group_layout.addLayout(status_layout)
        
        # Monitoring section
        mon_label = QtWidgets.QLabel(f"{monitor_type} Monitoring:")
        mon_label.setObjectName(f"{monitor_type.lower()}_mon{motor_num}")
        group_layout.addWidget(mon_label)
        
        # Monitoring display
        mon_display = QtWidgets.QWidget()
        mon_display.setObjectName(f"{monitor_type.lower()}_mon_display{motor_num}")
        mon_display.setAutoFillBackground(True)
        mon_display.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 4px;")
        mon_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Add placeholder content to monitoring display
        mon_layout = QtWidgets.QVBoxLayout(mon_display)
        mon_layout.setContentsMargins(10, 10, 10, 10)
        placeholder_label = QtWidgets.QLabel(f"{monitor_type} Chart Area")
        placeholder_label.setAlignment(Qt.AlignCenter)
        placeholder_label.setStyleSheet("color: #999; font-size: 14px;")
        mon_layout.addWidget(placeholder_label)
        
        group_layout.addWidget(mon_display)
        
        return group

    def create_control_tab(self):
        """Create the control tab with motor controls"""
        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        
        # Main layout for control tab
        control_layout = QtWidgets.QVBoxLayout(self.control)
        control_layout.setContentsMargins(10, 10, 10, 10)
        control_layout.setSpacing(10)
        
        # Top row - Motors 1 and 2
        top_row = QtWidgets.QHBoxLayout()
        top_row.setSpacing(10)
        
        self.motor_1 = self.create_motor_group(self.control, 1)
        self.motor_2 = self.create_motor_group(self.control, 2)
        
        top_row.addWidget(self.motor_1)
        top_row.addWidget(self.motor_2)
        control_layout.addLayout(top_row)
        
        # Bottom row - Stepper Motors 1 and 2
        bottom_row = QtWidgets.QHBoxLayout()
        bottom_row.setSpacing(10)
        
        self.motor_3 = self.create_motor_group(self.control, 3, "Stepper Motor")
        self.motor_4 = self.create_motor_group(self.control, 4, "Stepper Motor")
        
        bottom_row.addWidget(self.motor_3)
        bottom_row.addWidget(self.motor_4)
        control_layout.addLayout(bottom_row)
        
        self.vibration.addTab(self.control, "")

    def create_temperature_tab(self):
        """Create the temperature monitoring tab"""
        self.temperature = QtWidgets.QWidget()
        self.temperature.setObjectName("temperature")
        
        # Main layout for temperature tab
        temp_layout = QtWidgets.QVBoxLayout(self.temperature)
        temp_layout.setContentsMargins(10, 10, 10, 10)
        temp_layout.setSpacing(10)
        
        # Top row
        top_row = QtWidgets.QHBoxLayout()
        top_row.setSpacing(10)
        
        self.motor_temperature1 = self.create_monitoring_group(self.temperature, 1, "Temperature", "🌡️")
        self.motor_temperature2 = self.create_monitoring_group(self.temperature, 2, "Temperature", "🌡️")
        
        top_row.addWidget(self.motor_temperature1)
        top_row.addWidget(self.motor_temperature2)
        temp_layout.addLayout(top_row)
        
        # Bottom row
        bottom_row = QtWidgets.QHBoxLayout()
        bottom_row.setSpacing(10)
        
        self.motor_temperature3 = self.create_monitoring_group(self.temperature, 3, "Temperature", "🌡️")
        self.motor_temperature4 = self.create_monitoring_group(self.temperature, 4, "Temperature", "🌡️")
        
        bottom_row.addWidget(self.motor_temperature3)
        bottom_row.addWidget(self.motor_temperature4)
        temp_layout.addLayout(bottom_row)
        
        self.vibration.addTab(self.temperature, "")

    def create_current_tab(self):
        """Create the current monitoring tab"""
        self.current = QtWidgets.QWidget()
        self.current.setObjectName("current")
        
        # Main layout for current tab
        current_layout = QtWidgets.QVBoxLayout(self.current)
        current_layout.setContentsMargins(10, 10, 10, 10)
        current_layout.setSpacing(10)
        
        # Top row
        top_row = QtWidgets.QHBoxLayout()
        top_row.setSpacing(10)
        
        self.motor_current1 = self.create_monitoring_group(self.current, 1, "Current", "⚡")
        self.motor_current2 = self.create_monitoring_group(self.current, 2, "Current", "⚡")
        
        top_row.addWidget(self.motor_current1)
        top_row.addWidget(self.motor_current2)
        current_layout.addLayout(top_row)
        
        # Bottom row
        bottom_row = QtWidgets.QHBoxLayout()
        bottom_row.setSpacing(10)
        
        self.motor_current3 = self.create_monitoring_group(self.current, 3, "Current", "⚡")
        self.motor_current4 = self.create_monitoring_group(self.current, 4, "Current", "⚡")
        
        bottom_row.addWidget(self.motor_current3)
        bottom_row.addWidget(self.motor_current4)
        current_layout.addLayout(bottom_row)
        
        self.vibration.addTab(self.current, "")

    def create_vibration_tab(self):
        """Create the vibration monitoring tab"""
        self.vib = QtWidgets.QWidget()
        self.vib.setObjectName("vib")
        
        # Main layout for vibration tab
        vib_layout = QtWidgets.QVBoxLayout(self.vib)
        vib_layout.setContentsMargins(10, 10, 10, 10)
        vib_layout.setSpacing(10)
        
        # Top row
        top_row = QtWidgets.QHBoxLayout()
        top_row.setSpacing(10)
        
        self.motor_vib1 = self.create_monitoring_group(self.vib, 1, "Vibration", "📳")
        self.motor_vib2 = self.create_monitoring_group(self.vib, 2, "Vibration", "📳")
        
        top_row.addWidget(self.motor_vib1)
        top_row.addWidget(self.motor_vib2)
        vib_layout.addLayout(top_row)
        
        # Bottom row
        bottom_row = QtWidgets.QHBoxLayout()
        bottom_row.setSpacing(10)
        
        self.motor_vib3 = self.create_monitoring_group(self.vib, 3, "Vibration", "📳")
        self.motor_vib4 = self.create_monitoring_group(self.vib, 4, "Vibration", "📳")
        
        bottom_row.addWidget(self.motor_vib3)
        bottom_row.addWidget(self.motor_vib4)
        vib_layout.addLayout(bottom_row)
        
        self.vibration.addTab(self.vib, "")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPIKIE ActuMon - Motor Control & Monitoring"))
        
        # Control tab
        self.motor_1.setTitle(_translate("MainWindow", "🛠️ Motor 1"))
        self.motor_2.setTitle(_translate("MainWindow", "🛠️ Motor 2"))
        self.motor_3.setTitle(_translate("MainWindow", "🛠️ Stepper Motor 1"))
        self.motor_4.setTitle(_translate("MainWindow", "🛠️ Stepper Motor 2"))
        self.vibration.setTabText(self.vibration.indexOf(self.control), _translate("MainWindow", "CONTROL"))
        
        # Temperature tab
        self.motor_temperature1.setTitle(_translate("MainWindow", "🌡️ Motor 1 Temperature"))
        self.motor_temperature2.setTitle(_translate("MainWindow", "🌡️ Motor 2 Temperature"))
        self.motor_temperature3.setTitle(_translate("MainWindow", "🌡️ Motor 3 Temperature"))
        self.motor_temperature4.setTitle(_translate("MainWindow", "🌡️ Motor 4 Temperature"))
        self.vibration.setTabText(self.vibration.indexOf(self.temperature), _translate("MainWindow", "TEMPERATURE"))
        
        # Current tab
        self.motor_current1.setTitle(_translate("MainWindow", "⚡ Motor 1 Current"))
        self.motor_current2.setTitle(_translate("MainWindow", "⚡ Motor 2 Current"))
        self.motor_current3.setTitle(_translate("MainWindow", "⚡ Motor 3 Current"))
        self.motor_current4.setTitle(_translate("MainWindow", "⚡ Motor 4 Current"))
        self.vibration.setTabText(self.vibration.indexOf(self.current), _translate("MainWindow", "CURRENT"))
        
        # Vibration tab
        self.motor_vib1.setTitle(_translate("MainWindow", "📳 Motor 1 Vibration"))
        self.motor_vib2.setTitle(_translate("MainWindow", "📳 Motor 2 Vibration"))
        self.motor_vib3.setTitle(_translate("MainWindow", "📳 Motor 3 Vibration"))
        self.motor_vib4.setTitle(_translate("MainWindow", "📳 Motor 4 Vibration"))
        self.vibration.setTabText(self.vibration.indexOf(self.vib), _translate("MainWindow", "VIBRATION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    