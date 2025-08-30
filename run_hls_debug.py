
import os, sys, time
sys.path.insert(0, "src")
sys.path.insert(0, "test") 

from conftest import create_default_ls
from solidlsp.ls_config import Language

print("=== HLS Debug Test ===")
try:
    print("1. Creating HLS language server...")
    ls = create_default_ls(Language.HASKELL)
    print(f"   Created: {type(ls)}")
    
    print("2. Starting HLS...")
    ls.start()
    print("   Started successfully")
    
    print("3. Requesting document symbols...")
    symbols = ls.request_document_symbols("src/Lib.hs")
    print(f"   Raw symbols result: {symbols}")
    print(f"   Type: {type(symbols)}")
    
    if symbols and len(symbols) >= 2:
        hierarchical, flat = symbols
        print(f"   Hierarchical count: {len(hierarchical)}")
        print(f"   Flat count: {len(flat)}")
        print(f"   First few hierarchical: {hierarchical[:2] if hierarchical else 'None'}")
    else:
        print("   Symbols is empty or malformed")
        
    print("4. Shutting down...")
    ls.shutdown()
    print("   Success!")
    
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()
