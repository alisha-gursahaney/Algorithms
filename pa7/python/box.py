import nest_boxes

class box:
    def __init__(self, length, width, height):
        self.l = length
        self.w = width
        self.h = height

    def __str__(self):
        return str(self.l) + ' x ' + str(self.w) + ' x ' + str(self.h)

    def __repr__(self):
        return str(self)

def main():
    n = int(input())
    boxes = []
    for i in range(n):
        line = input().strip().split()
        length = float(line[0])
        width = float(line[1])
        height = float(line[2])
        b = box(length, width, height)
        boxes.append(b)
    print(nest_boxes.max_depth(boxes))

main()

