class StyleSheet:
    @staticmethod
    def main(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QLabel{
        font-family: Nunito Sans 10pt Condensed;
        font-size: 13px;
        }
        QMainWindow,QWidget#centralwidget,QTabWidget,QTabWidget::tab{
            border:none;
            background-color: """
            + backgroundColor
            + """;
        }
        QFrame#titleFrame{
            background-color:"""
            + backgroundColor
            + """;
        }
        QFrame#mainFrame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QWidget#centralwidget{
            border-top-left-radius:8px;
            border-top-right-radius:8px;
            background-color:"""
            + backgroundColor
            + """;
        }
        QLabel{
            color:"""
            + labelColor
            + """;
        }
        QLabel#title{
            font-size:14px;
            font-weight:bold;
        }
        QWidget#tab1,
        QWidget#tab2,
        QWidget#tab2_1,
        QWidget#tab2_2,
        QWidget#tab3,
        QWidget#tab3_1,
        QWidget#tab3_2,
        QWidget#tab3_3,
        QWidget#tab3_4,
        QWidget#tab3_5,
        QWidget#tab3_6,
        QWidget#tab4,
        QScrollArea,
        QWidget#scrollAreaWidgetContents{
            background-color:"""
            + backgroundColor
            + """;
            border:1px solid """
            + secondaryBackgroundColor
            + """;
        }
        QComboBox{
            height:24px;
            padding-left:10px;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QComboBox::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QComboBox::drop-down {
            border-left-width: 1px;
            border-left-color: """
            + textColor
            + """;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }
        QComboBox:on{
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;
        }
        QComboBox::down-arrow {
            width: 20px;
        }
        QComboBox QAbstractItemView{
            border: none;
            color:"""
            + textColor
            + """;
            border-left:1px solid """
            + labelColor
            + """;
            border-right:1px solid """
            + labelColor
            + """;
            border-bottom:1px solid """
            + labelColor
            + """;
            border-bottom-left-radius:8px;
            border-bottom-right-radius:8px;
            selection-background-color:"""
            + backgroundColor
            + """;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        
        }
        QComboBox QAbstractItemView::item:hover{
            background-color:"""
            + labelColor
            + """;
        }
        QLineEdit{
            height:24px;
            padding-left:10px;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QSpinBox{
            padding-left:10px;
            selection-background-color:"""
            + secondaryBackgroundColor
            + """;
            selection-color:"""
            + labelColor
            + """;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QSpinBox::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QSpinBox::focus{
            border:1px solid """
            + labelColor
            + """;
        }
        QSpinBox::up-button, QSpinBox::down-button {
            border: none;
            background-color: none;
            margin-right:4px;
            width:10px;
        }
        QPushButton{
            border-radius:5px;
            width:25px;
            height:25px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        QToolButton#minimizeButton{
            padding:5px;
        }
        QToolButton#minimizeButton::hover{
            background-color:none;
            
        }
        QToolButton#closeButton::hover{
            background-color:red;
            border-top-right-radius:8px;
        }
        QScrollBar:vertical {
            border: 0px solid """
            + labelColor
            + """;
            background:"""
            + secondaryBackgroundColor
            + """;
            width: 8px;
            margin: 0px;
        }
        QScrollBar::handle:vertical{
            background-color: """
            + backgroundColor
            + """;
            border:0px solid """
            + secondaryBackgroundColor
            + """;
            border-radius:4px;
            min-height: 0px;
        }
         QScrollBar::add-line:vertical {       
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QTabWidget::pane{
            border:none;
        }
        QTabBar::pane {
            border: none;
        }
        QToolTip{
            color:"""
            + backgroundColor
            + """;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QToolBox::tab {
            background-color:"""
            + backgroundColor
            + """;
            border-radius: 5px;
            color: """
            + labelColor
            + """;
        }
        QToolBox{
            icon-size:18px;
        }
        QToolBox > QScrollArea{
            border-radius: 5px;
        }
        QToolBox > QScrollArea > #qt_scrollarea_viewport > QWidget{
            border-radius: 5px;
            background-color: """
            + backgroundColor
            + """;
        }
        QPushButton#saveButton,QPushButton#saveButton_2{
            color:"""
            + labelColor
            + """;
            width:70px;
        }
        QPushButton#chooseButton{
            width: 120px;
            color:"""
            + labelColor
            + """;
        }
        QPushButton#downloadButton{
            width: 140px;
            color:"""
            + labelColor
            + """;
        }
        QToolButton#installButton,QToolButton#uninstallButton,QToolButton#runButton,QToolButton#stopButton{
            color:"""
            + labelColor
            + """;
            font-size:14px;
            background-color: """
            + secondaryBackgroundColor
            + """;
            border-radius:10px;
            width:150px;
            height:50px;
            padding-top:30px;
            padding-bottom:30px;
        }
        QToolButton#installButton::hover,QToolButton#uninstallButton::hover,QToolButton#runButton::hover,QToolButton#stopButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QToolButton#installButton::pressed,QToolButton#uninstallButton::pressed,QToolButton#runButton::pressed,QToolButton#stopButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        QToolButton#blockListButton{
            color:"""
            + labelColor
            + """;
            font-size:14px;
            background-color: """
            + secondaryBackgroundColor
            + """;
            border-radius:10px;
            width:150px;
            height:80px;
            padding-top:30px;
            padding-bottom:30px;
            margin-top:40px
        }
        QToolButton#blockListButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QToolButton#blockListButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        QListView{
            
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius: 5px;
        }
        QListView::item{
            color:"""
            + labelColor
            + """;
        }
        QListView::item:selected {
            background-color:"""
            + labelColor
            + """;
            color:"""
            + backgroundColor
            + """;
            border-radius:5px;
            font-weight:bold;

        }
        QLabel#label{
            font-size:14px;
            font-weight:bold;
        }
        """
        )

    @staticmethod
    def appliedWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QFrame#applied_frame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border:1px solid """
            + labelColor
            + """;
            border-radius:8px;
        }
        QLabel#applied_text{
            font-family: Andika;
            font-size: 12;
            font-weight:bold;
        }
        QPushButton#ok_button{
            font-family: Nunito Sans 10pt Condensed;
            font-size:10;
            font-weight:bold;
            background-color:"""
            + backgroundColor
            + """;
            color:"""
            + labelColor
            + """;
            width:50px;
        }
        QPushButton#ok_button::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton#ok_button::pressed{
            background-color:"""
            + labelColor
            + """;
            color:"""
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def disabledListWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QLabel#disabledNote{
            font-family: Andika;
            font-size:11px;
            font-weight: bold;
            color:"""
            + labelColor
            + """;
        }
        QFrame#disabledList_frame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border:1px solid """
            + labelColor
            + """;
            border-radius:8px;
        }
        QLineEdit#lineEdit{
            height:24px;
            padding-left:10px;
            font-family: Andika;
            font-size:14px;
            background-color:"""
            + backgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
            }
        QListWidget#disabledList{
            background-color:"""
            + backgroundColor
            + """;
            font-size:14px;
            padding-left:10px;
            padding-right:10px;
            padding-top:5px;
            padding-bottom:5px;
            font-family: Andika;
        }
        QListWidget#disabledList::item:selected{
            background-color:"""
            + backgroundColor
            + """;
        }
        QPushButton#applyButton, QPushButton#cancelButton{
            font-family: Nunito Sans 10pt Condensed;
            font-size:14px;
            font-weight:bold;
            background-color:"""
            + backgroundColor
            + """;
            color:"""
            + labelColor
            + """;
            width:70px;
        }
        QPushButton#applyButton::hover, QPushButton#cancelButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton#applyButton::pressed, QPushButton#cancelButton::pressed{
            background-color:"""
            + labelColor
            + """;
            color:"""
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def listWidgetItem(
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
            QLabel{
                color:"""
            + textColor
            + """;
                font-size:14px;
                font-weight:normal;
                font-family: Andika;
            }
            QToolButton::hover{
                background-color:none;
                border:none;
            }
            """
        )

    @staticmethod
    def infoWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QFrame#titleFrame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-top-left-radius:8px;
            border-top-right-radius:8px;
            border-top:1px solid """
            + textColor
            + """;
            border-left:1px solid """
            + textColor
            + """;
            border-right:1px solid """
            + textColor
            + """;
        }
        QLabel#title{
            font-family: Nunito Sans 10pt Condensed;
            font-size:14px;
            font-weight:bold;
        }
        QLabel#description{
            font-family: Andika;
        }
        QScrollArea{
            border:1px solid """
            + textColor
            + """;
        }
        QToolButton#closeButton::hover{
            background-color:red;
            border-top-right-radius:8px;
        }
        """
        )

    @staticmethod
    def applyButton(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QPushButton{
            border-radius:5px;
            color:"""
            + labelColor
            + """;
            width:70px;
            height:30px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        """
        )

    @staticmethod
    def disabledListButton(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QPushButton{
            border-radius:5px;
            color:"""
            + labelColor
            + """;
            width:100px;
            height:30px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        """
        )

    @staticmethod
    def resetAllButton(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QPushButton{
            border-radius:5px;
            color:"""
            + labelColor
            + """;
            width:80px;
            height:30px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        """
        )

    @staticmethod
    def mainTabBar(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:"""
            + textColor
            + """;
            padding-left:38px;
            padding-right:38px;
            padding-top:5px;
            padding-bottom:5px;
            margin-left:10px;
         }
        QTabBar::tab:hover{
            color:"""
            + labelColor
            + """;
        }
        QTabBar::tab:selected {
            color: """
            + labelColor
            + """;
            margin-top:3px;
            margin-bottom:3px;
            border:1px solid """
            + textColor
            + """;
            font-weight:bold;
            border-radius: 5px;
            background-color: """
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def menuTabBar(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:"""
            + textColor
            + """;
            padding-left:17px;
            padding-right:17px;
            padding-top:5px;
            padding-bottom:5px;
         }
        QTabBar::tab:hover{
            color:"""
            + labelColor
            + """;
        }
        QTabBar::tab:selected {
            color: """
            + labelColor
            + """;
            font-weight:bold;
            background-color: """
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def buttonColorStylesheet(rgba: tuple | list, secondaryBackgroundColor: str) -> str:
        colorString: str = f"rgb({rgba[0]},{rgba[1]},{rgba[2]})"
        return (
            """QPushButton{background-color:"""
            + colorString
            + """;width:23px;height:23px;border:1px solid """
            + secondaryBackgroundColor
            + """;}"""
        )

    @staticmethod
    def buttoResetStyleSheet(resetColor: str = "#313131") -> str:
        return (
            """QPushButton{background-color:"""
            + resetColor
            + """;width:25px;height:25px;border:0px;}"""
        )

    class ColorPicker:
        @staticmethod
        def titleBar(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "#FFFFFF",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                    QFrame{
                    background-color:"""
                + secondaryBackgroundColor
                + """;
                    border-bottom-left-radius:0px;
                    border-bottom-right-radius:0px;
                    }

                    """
            )

        @staticmethod
        def windowTitle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "#FFFFFF",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                    QLabel{
                    font-size:13px;
                    color:"""
                + labelColor
                + """;
                    font-weight:bold;
                    }

                    """
            )

        @staticmethod
        def buttonTextStyle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "#FFFFFF",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                QDialogButtonBox QPushButton{
                font-size:12px;
                font-weight:normal;
                }
                QDialogButtonBox QPushButton::hover{
                    border:1px solid """
                + labelColor
                + """;
                }
                QDialogButtonBox QPushButton::pressed{
                    color:"""
                + labelColor
                + """;
                    background-color:"""
                + textColor
                + """;
                }
                """
            )

        @staticmethod
        def labelStyle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "#FFFFFF",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                QLabel{
                color:"""
                + labelColor
                + """;
                font-size:12px;
                font-weight:normal;
                }
                """
            )
