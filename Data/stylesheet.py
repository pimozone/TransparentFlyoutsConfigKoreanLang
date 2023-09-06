class StyleSheet:
    @staticmethod
    def main(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
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
            border-radius:8px;
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
        }
        QWidget#tab1,
        QWidget#tab2,
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
            image: url("Assets/icons/down-arrow.png");
        }
        QComboBox QAbstractItemView{
            border: none;
            color:"""
            + textColor
            + """;
            selection-background-color:"""
            + backgroundColor
            + """;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        
        }
        QComboBox QAbstractItemView::item:hover{
            background-color:"""
            + backgroundColor
            + """;
        }
        QLineEdit{
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
        QSpinBox::up-button, QSpinBox::down-button {
            border: none;
            background-color: transparent;
            margin-right:4px;
            width:10px;
        }
        QSpinBox::up-button{
            image: url("Assets/icons/up-arrow.png");
        }
        QSpinBox::down-button{
            image: url("Assets/icons/down-arrow.png");
        }
        QPushButton{
            border-radius:5px;
            width:25px;
            height:25px;
            background-color:"""
            + secondaryBackgroundColor
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
            border: none;
            background:"""
            + secondaryBackgroundColor
            + """;
            width: 10px;
        }
        QScrollBar::handle:vertical{
            background: """
            + textColor
            + """;
            border-radius:4px;
            margin:1px;
        }
        QTabWidget::pane {
            border-top: 2px solid #C2C7CB;
        }
        """
        )

    @staticmethod
    def applyButton(secondaryBackgroundColor: str = "#313131", labelColor: str = "white", textColor: str = "#7A7A7A") -> str:
        return (
            """
        QPushButton{
            border:1px solid """
            + labelColor
            + """;
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
    def mainTabbar(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:#7A7A7A;
            padding-left:38px;
            padding-right:38px;
            padding-top:5px;
            padding-bottom:5px;
            border:1px solid """
            + secondaryBackgroundColor
            + """;
            margin-left:4px;
            margin-right:4px;
            border-radius: 0px;
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
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:#7A7A7A;
            padding-left:17px;
            padding-right:17px;
            padding-top:5px;
            padding-bottom:5px;
            border-radius: 0px;
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
    def buttonColorStylesheet(rgba: tuple) -> str:
        colorString: str = f"rgb({rgba[0]},{rgba[1]},{rgba[2]})"
        return "QPushButton{background-color:" + colorString + ";width:25px;height:25px;}"

    @staticmethod
    def buttoResetStyleSheet(resetColor: str = "#313131") -> str:
        return """QPushButton{background-color:""" + resetColor + """;width:25px;height:25px;}"""
