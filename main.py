import os
import sys
from PIL import Image

def add_offset(filepath, y_offset):
    src = Image.open(filepath).convert("RGBA")
    size = (src.size[0], src.size[1] + y_offset)
    dst = Image.new(src.mode, size=size)
    dst.paste(src, (0, y_offset))
    dst.save(filepath, format="PNG", quality=100)

def main():
    path = sys.argv[1]
    y_offset = int(sys.argv[2])

    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if not filename.lower().endswith(".png"):
                continue

            filepath = os.path.join(root, filename)
            add_offset(filepath, y_offset)
            print(filepath)

if __name__ == "__main__":
    main()
