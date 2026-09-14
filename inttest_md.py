import os
import md

md.run_md()

assert os.path.exists("cu.traj")
assert os.path.getsize("cu.traj") > 0
