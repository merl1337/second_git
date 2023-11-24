        self.pushButton.clicked.connect(self.creator)
        canvas = QPixmap(800, 570)
        self.label.setPixmap(canvas)
    def creator(self):
        x, y = [randint(10, 500) for x in range(2)]
        w, h = [randint(10, 100) for x in range(2)]
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.yellow)
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowUI()
    ex.show()
    sys.exit(app.exec_())