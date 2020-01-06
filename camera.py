from load_image_function import width, height, cell_size

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx / cell_size
        obj.rect.y += self.dy / cell_size

    # позиционировать камеру на объекте target
    def update(self, dx, dy):
        self.dx = dx
        self.dy = dy