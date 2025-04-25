import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
import os
from .crafting import INGREDIENTS

class GameUI(QMainWindow):
    def __init__(self, world, player, tile_size=16):
        # Ensure a QApplication exists before creating any QWidget
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        # store the application instance for later use
        self.app = app
        super().__init__()
        self.world = world
        self.player = player
        self.tile_size = tile_size
        self.setWindowTitle('Lamecraft')
        self.setFixedSize(self.world.width * self.tile_size, self.world.height * self.tile_size)
        # Load sprites for world items
        self.item_sprites = {}
        sprite_dir = os.path.join(os.path.dirname(__file__), 'sprites')
        for ingredient in INGREDIENTS:
            pixmap = QPixmap(os.path.join(sprite_dir, f'{ingredient}.png'))
            self.item_sprites[ingredient] = pixmap

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
        # Draw items on the world map
        for (ix, iy), items in self.world.items.items():
            for ingredient in items:
                pixmap = self.item_sprites.get(ingredient)
                if pixmap and not pixmap.isNull():
                    painter.drawPixmap(ix * self.tile_size, iy * self.tile_size, self.tile_size, self.tile_size, pixmap)
                else:
                    # Fallback: draw a small yellow dot for the item
                    painter.setBrush(QColor(255, 255, 0))
                    size = self.tile_size // 2
                    offset = (self.tile_size - size) // 2
                    painter.drawEllipse(ix * self.tile_size + offset, iy * self.tile_size + offset, size, size)
        # Draw player
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
        # Show the main window and start the event loop using stored QApplication
        self.show()
        sys.exit(self.app.exec_())
