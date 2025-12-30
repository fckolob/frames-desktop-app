
import sys
import os

# Add the current directory to sys.path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logic.opening import Opening
from logic.calculate_materials import CalculateMaterials

def test_unification():
    print("Testing Material Unification across Gala series...")
    
    # Opening 1: Gala Triple Rail
    op1 = Opening(1000, 2000, "galaCorredizaTripleRiel", "anodizado", False, False, 1)
    
    # Opening 2: Gala Quadruple Rail
    op2 = Opening(1000, 2000, "galaCorredizaCuatroRieles", "anodizado", False, False, 1)
    
    calc = CalculateMaterials([op1, op2])
    bars = calc.get_frame_bars()
    
    print("\nMaterial Bars (Gala Simple Glass):")
    shash_bars = [b for b in bars if "Lateral de Hoja" in b.name]
    hook_bars = [b for b in bars if "Enganche" in b.name]
    
    for bar in bars:
        print(f"  {bar.quantity}x {bar.name} ({bar.serie}) Code: {bar.code}")
    
    # Check Lateral Shashes (PN 93007)
    # Currently it should be 2 separate entries because series names are different
    # After fix it should be 1 entry
    print(f"\nFound {len(shash_bars)} entries for Lateral de Hoja")
    print(f"Found {len(hook_bars)} entries for Enganche")
    
    print("\nTesting Probba unification...")
    op3 = Opening(1000, 2000, "probbaCorrediza", "anodizado", False, False, 1)
    op4 = Opening(1500, 2000, "probbaCorredizaTripleRiel", "anodizado", False, False, 1)
    
    calc_probba = CalculateMaterials([op3, op4])
    bars_probba = calc_probba.get_frame_bars()
    
    shash_bars_probba = [b for b in bars_probba if "Lateral de Hoja" in b.name]
    for bar in bars_probba:
         print(f"  {bar.quantity}x {bar.name} ({bar.serie})")
    
    print(f"\nFound {len(shash_bars_probba)} entries for Lateral de Hoja (Probba)")

if __name__ == "__main__":
    test_unification()
