import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
import pyqtgraph as pg

class LineGraphWindow(QWidget):
    def __init__(self, xArray, yArray):
        super(LineGraphWindow, self).__init__()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.plot(xArray, yArray)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.graphWidget)

class BarGraphWindow(QWidget):
    def __init__(self, xArray, yArray):
        super(BarGraphWindow, self).__init__()
        bar = pg.BarGraphItem(x=xArray, height=yArray, width=0.6, brush='g')
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.addItem(bar)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.graphWidget)

class GraphGenerator(QWidget):
    def __init__(self):
        super(GraphGenerator, self).__init__()
        self.initUI()

    def initUI(self):
        self.xDataFields = [QLineEdit(self)]  
        self.yDataFields = [QLineEdit(self)]  
        self.dynamic_field_count = 0

        mainVbox = QVBoxLayout()

        self.title = QLabel(self)
        self.title.setText("Data Visualizer")
        font = self.title.font()
        font.setPointSize(36)
        font.setBold(True)
        self.title.setFont(font)
        mainVbox.addWidget(self.title)

        vbox = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText("Data 1 (numeric value only): ")
        mainVbox.addWidget(self.label)

        self.xDataFields[0].setPlaceholderText("Enter X-axis data")
        self.yDataFields[0].setPlaceholderText("Enter Y-axis data")
        hbox = QHBoxLayout()
        hbox.addWidget(self.xDataFields[0])  
        hbox.addWidget(self.yDataFields[0])  
        vbox.addLayout(hbox)

        mainVbox.addLayout(vbox)

        addField = QPushButton("Add Field", self)
        addField.clicked.connect(self.addField)

        lineGraph = QPushButton("Generate Line Graph", self)
        lineGraph.clicked.connect(self.generateLineGraph)
        barGraph = QPushButton("Generate Bar Graph", self)
        barGraph.clicked.connect(self.generateBarGraph)

        button_hbox = QHBoxLayout()
        button_hbox.addWidget(addField)
        button_hbox.addWidget(lineGraph)
        button_hbox.addWidget(barGraph)

        mainVbox.addLayout(button_hbox)

        self.setLayout(mainVbox)
        self.show()

    def addField(self):
        vbox_dynamic = QVBoxLayout()

        label = QLabel(self)
        label.setText(f"Data {self.dynamic_field_count + 2} (numeric value only): ")
        vbox_dynamic.addWidget(label)

        hbox = QHBoxLayout()

        xData = QLineEdit(self)
        xData.setPlaceholderText("Enter X-axis data")
        hbox.addWidget(xData)

        yData = QLineEdit(self)
        yData.setPlaceholderText("Enter Y-axis data")
        hbox.addWidget(yData)

        vbox_dynamic.addLayout(hbox)

        main_vbox = self.layout()
        main_vbox.insertLayout(main_vbox.count() - 1, vbox_dynamic)

        self.xDataFields.append(xData)
        self.yDataFields.append(yData)

        self.dynamic_field_count += 1

    def generateLineGraph(self):
        x_array = [float(x.text()) for x in self.xDataFields if x.text()]
        y_array = [float(y.text()) for y in self.yDataFields if y.text()]

        self.line_graph_window = LineGraphWindow(x_array, y_array)
        self.line_graph_window.show()

    def generateBarGraph(self):
        x_array = [float(x.text()) for x in self.xDataFields if x.text()]
        y_array = [float(y.text()) for y in self.yDataFields if y.text()]

        self.bar_graph_window = BarGraphWindow(x_array, y_array)
        self.bar_graph_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphGenerator()
    sys.exit(app.exec())
