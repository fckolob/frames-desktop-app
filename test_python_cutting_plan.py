
import sys
import os

# Ensure import works
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logic.calculate_materials import CalculateMaterials
from logic.models import Frame, Bar

# Mock opening/frame structure
class MockOpening:
    def __init__(self):
        self.frames = {}
    
    def framing(self):
        pass

def test_cutting_plan():
    print("Testing Python Cutting Plan Logic...")
    
    # Create manual piece list test
    # We can test CalculateMaterials internal methods directly if possible, 
    # but `calculate_frame_bars_quantity_with_custom_length` is the key.
    
    calc = CalculateMaterials()
    
    # Test Greedy
    pieces = [1500.0, 1500.0, 1500.0, 1000.0, 1000.0, 500.0]
    bar_len = 5950.0
    
    qty, method, details = calc.calculate_frame_bars_quantity_with_custom_length(pieces, bar_len)
    
    print(f"Greedy Result: Qty={qty}, Method={method}")
    print(f"Details: {details}")
    
    if qty > 0 and details and len(details) == qty:
        print("PASS: Greedy details present.")
    else:
        print("FAIL: Greedy details missing or mismatch.")
        pass

    # Test Optimal (BnB) - Trigger with small group but force 'Optimal' path?
    # Logic uses count > 40 for greedy. So small group uses BnB.
    # pieces size 6 < 40, so it runs BnB.
    
    if method == "Optimal":
        print("PASS: Method is Optimal.")
    else:
         print(f"WARN: Expected Optimal, got {method}")
         
    # Check structure
    total_len = 0
    for bar_pieces in details:
        bar_sum = sum(bar_pieces)
        print(f"Bar sum: {bar_sum}")
        if bar_sum > bar_len:
            print("FAIL: Bar overflow!")

if __name__ == "__main__":
    test_cutting_plan()
