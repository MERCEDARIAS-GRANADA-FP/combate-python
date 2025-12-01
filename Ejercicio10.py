import subprocess
import sys

cmd = [sys.executable, "-m", "pip", "list"]
out = subprocess.check_output(cmd, text=True)
print(out)
