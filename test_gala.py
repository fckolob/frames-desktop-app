
from logic.opening import Opening
from logic.calculate_materials import CalculateMaterials
import sys

def test_gala_logic():
    print("Testing Gala Corrediza Cuatro Rieles Logic...")
    # width=4000, height=2000, 1 unit, dvh=True
    op = Opening(4000, 2000, "galaCorredizaCuatroRieles", "anodizado", True, False, 1)
    op.init()
    
    print("\nProduction Output:")
    production = op.to_string()
    print(production)
    
    # Check for specific gala frames in production output
    expected_frames = [
        "Horizontal de Marco cuatro Rieles",
        "Lateral de Marco cuatro Rieles",
        "Lateral de Hoja para DVH gala",
        "Enganche para DVH gala",
        "Horizontal de Hoja para DVH gala (hojas laterales)",
        "Horizontal de Hoja para DVH gala (hoja central)"
    ]
    
    for frame_name in expected_frames:
        if frame_name in production:
            print(f"PASS: {frame_name} found in output")
        else:
            print(f"FAIL: {frame_name} missing from output")

    # Materials
    print("\nCalculating Materials...")
    calc = CalculateMaterials([op])
    bars = calc.get_frame_bars()
    for bar in bars:
        print(f"Bar: {bar.name} Qty: {bar.quantity} Serie: {bar.serie}")

    # Check if we have materials
    if len(bars) > 0:
        print("\nPASS: Materials calculated")
    else:
        print("\nFAIL: No materials")
        
    # Check if custom bar length 6700 was likely used (this is harder to check directly without instrumenting CalculateMaterials, 
    # but we can infer if the results seem reasonable or check the code logic again).
    # Specifically, check if the serie in the bar is correct.
    for bar in bars:
        if bar.serie != "galaCorredizaCuatroRieles":
             print(f"FAIL: Bar serie mismatch: {bar.serie}")

if __name__ == "__main__":
    try:
        test_gala_logic()
        print("\nTest Complete.")
    except Exception as e:
        print(f"Test Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
