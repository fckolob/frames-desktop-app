import sys
import os
sys.path.append(os.getcwd())

from logic.opening import Opening

def test_gala():
    # 1000x1000 opening, qty 1
    op = Opening(serie="galaCorrediza", color="Anodizado", width=1000, height=1000, quantity=1, dvh=False, preframe="Sin Premarco")
    op.calculate_pieces()
    op.framing()
    
    print("Frames:")
    for key, frame in op.frames.items():
        if isinstance(frame, list):
            for f in frame:
                print(f"{f.name}: {f.width} x {f.height}")
        else:
            print(f"{frame.name}: {frame.lenght} (Qty: {frame.quantity})")
    
    print("\nGlass:")
    print(op.glass)

if __name__ == "__main__":
    test_gala()
