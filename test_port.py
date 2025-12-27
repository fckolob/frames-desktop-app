
from logic.opening import Opening
from logic.calculate_materials import CalculateMaterials
import sys

def test_s20_logic():
    print("Testing S20 Logic...")
    # width=1000, height=2000, 1 unit
    op = Opening(1000, 2000, "s20", "anodizado", False, False, 1)
    op.init()
    
    print("Framing output:")
    print(op.to_string())
    
    # Check if we have frames
    if "horizontalFrame" in op.frames:
        print("PASS: Horizontal Frame exists")
    else:
        print("FAIL: Horizontal Frame missing")

    # Materials
    print("\nCalculating Materials...")
    calc = CalculateMaterials([op])
    bars = calc.get_frame_bars()
    for bar in bars:
        print(f"Bar: {bar.name} Qty: {bar.quantity}")

    if len(bars) > 0:
        print("PASS: Materials calculated")
    else:
        print("FAIL: No materials")

if __name__ == "__main__":
    try:
        test_s20_logic()
        print("\nTest Complete.")
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
