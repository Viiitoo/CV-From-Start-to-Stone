import json
import numpy as np
from pathlib import Path
from scipy.spatial.transform import Rotation as R

src = Path(r"trj_final.json")
out_est = src.parent / "traj_est.txt"
out_gt = src.parent / "traj_gt.txt"

with open(src, "r") as f:
    data = json.load(f)

def mat2tum(trj, out_file):
    with open(out_file, "w") as f:
        for i, T in enumerate(trj):
            T = np.array(T)
            Rm, t = T[:3,:3], T[:3,3]
            q = R.from_matrix(Rm).as_quat()  # (x,y,z,w)
            f.write(f"{i} {t[0]} {t[1]} {t[2]} {q[0]} {q[1]} {q[2]} {q[3]}\n")

mat2tum(data["trj_est"], out_est)
mat2tum(data["trj_gt"], out_gt)

print("✅ Wrote:", out_est, "and", out_gt)
