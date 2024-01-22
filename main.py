from PIL import Image
from enum import IntEnum

class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

  def clockwise(self):
    return Direction( (self + 1) % 4 )

  def counterclockwise(self):
    return Direction( (self - 1) % 4 )

  def get_move(self) -> tuple[int, int]:
    mx = 0
    my = 0
    if self == Direction.UP:
      my = -1
    elif self == Direction.DOWN:
      my = 1
    elif self == Direction.LEFT:
      mx = -1
    elif self == Direction.RIGHT:
      mx = 1
    return (mx, my)

def main():
  width = 1024
  height = 1024

  img = Image.new(mode='1', size=(width, height), color=1)

  pos = [512, 512]
  direction = Direction.UP
  while pos[0] > 0 and pos[0] < width and pos[1] > 0 and pos[1] < height:
    current_pixel = img.getpixel(tuple(pos))
    if current_pixel: # Белая клетка
      direction = direction.clockwise()
      img.putpixel(tuple(pos), 0)
    else:
      direction = direction.counterclockwise()
      img.putpixel(tuple(pos), 1)
    mx, my = direction.get_move()
    pos[0] = pos[0] + mx
    pos[1] = pos[1] + my
  img.save('out.png')

if __name__ == '__main__':
  main()
