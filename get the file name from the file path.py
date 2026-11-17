import os
file_name = os.path.basename('/root/file.ext')
print(os.path.splitext(file_name)[0])

import os
print(os.path.splitext(file_name))

from pathlib import Path
print(Path('/root/file.ext').stem)