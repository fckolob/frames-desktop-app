
import sys
import os

# Add the current directory to sys.path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logic.opening import Opening
from logic.calculate_materials import CalculateMaterials

def test_gala_triple_riel():
    print("Testing Gala Corrediza Triple Riel...")
    
    # Test case: 1000x2000, 1 unit, anodizado, simple glass
    width, height, quantity = 1000, 2000, 1
    op = Opening(width, height, "galaCorredizaTripleRiel", "anodizado", False, False, quantity)
    op.init()
    
    pieces = op.pieces
    print(f"Pieces for {width}x{height} (Simple Glass):")
    for k, v in pieces.items():
        print(f"  {k}: {v}")
    
    # Assertions for some key pieces
    assert abs(pieces["horizontalFrame"]["lenght"] - 964) < 0.1
    assert abs(pieces["lateralShash"]["lenght"] - 1935) < 0.1
    assert abs(pieces["horizontalShashLateral"]["lenght"] - 326.33) < 0.1
    assert abs(pieces["horizontalShashCentral"]["lenght"] - 345.33) < 0.1
    
    # Test materials calculation (bar length check)
    calc = CalculateMaterials([op])
    bars = calc.get_frame_bars()
    
    print("\nMaterial Bars (Simple Glass):")
    shash_bars = [b for b in bars if "Horizontal de Hoja" in b.name]
    for bar in bars:
        print(f"  {bar.quantity}x {bar.name} ({bar.serie})")
    
    # Verify material grouping (should be 1 bar for both types of horizontal shashes)
    assert len(shash_bars) == 1, f"Expected 1 grouped bar for horizontal shashes, found {len(shash_bars)}"
    print("SUCCESS: Material grouping by profile code verified.")

    # Verify report distinction
    report = op.to_string()
    print("\nProduction Report Snippet:")
    print("\n".join(report.split("\n")[:15]))
    assert "Hojas Laterales" in report
    assert "Hoja Central" in report
    print("SUCCESS: Production report distinguishes between lateral and central shashes.")

    print("\nTesting Gala Corrediza Triple Riel (DVH)...")
    op_dvh = Opening(width, height, "galaCorredizaTripleRiel", "anodizado", True, False, quantity)
    op_dvh.init()
    
    calc_dvh = CalculateMaterials([op_dvh])
    bars_dvh = calc_dvh.get_frame_bars()
    
    shash_bars_dvh = [b for b in bars_dvh if "Horizontal de Hoja" in b.name]
    assert len(shash_bars_dvh) == 1, f"Expected 1 grouped bar for horizontal shashes (DVH), found {len(shash_bars_dvh)}"
    
    report_dvh = op_dvh.to_string()
    assert "Hojas Laterales" in report_dvh
    assert "Hoja Central" in report_dvh
    print("SUCCESS: Verification for DVH passed.")

    print("\nAll tests passed!")

if __name__ == "__main__":
    try:
        test_gala_triple_riel()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Test failed: {e}")
        sys.exit(1)
