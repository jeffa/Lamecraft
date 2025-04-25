import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class GameUI(QMainWindow):
    def __init__(self, world, player, tile_size=16):
        super().__init__()
        self.world = world
        self.player = player
        self.tile_size = tile_size
        self.setWindowTitle('Lamecraft')
        self.setFixedSize(self.world.width * self.tile_size, self.world.height * self.tile_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for y in range(self.world.height):
            for x in range(self.world.width):
                biome = self.world.get_tile(x, y)
                if biome == 'water':
                    color = QColor(0, 0, 255)
                elif biome == 'sand':
                    color = QColor(194, 178, 128)
                elif biome == 'grass':
                    color = QColor(34, 139, 34)
                else:
                    color = QColor(139, 137, 137)
                painter.fillRect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, color)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(self.player.x * self.tile_size, self.player.y * self.tile_size, self.tile_size, self.tile_size)

    def keyPressEvent(self, event):
        key = event.key()
        dx = dy = 0
        if key == Qt.Key_W or key == Qt.Key_Up:
            dy = -1
        elif key == Qt.Key_S or key == Qt.Key_Down:
            dy = 1
        elif key == Qt.Key_A or key == Qt.Key_Left:
            dx = -1
        elif key == Qt.Key_D or key == Qt.Key_Right:
            dx = 1
        else:
            return
        if self.player.move(dx, dy, self.world):
            self.update()

    def run(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
