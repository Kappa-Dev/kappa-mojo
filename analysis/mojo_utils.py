import os
import sys
import time

OUTDIR = os.path.abspath("../outputs/")
SNAPDIR = os.path.abspath("../snapshots/")

def get_model_info(model_name):
    info = {"snap_fname": None,
            "out_fname": None}
    snap_fname = os.path.join(SNAPDIR, "%s.json" %(model_name))
    out_fname = os.path.join(OUTDIR, "%s.out" %(model_name))
    if os.path.isfile(snap_fname):
        info["snap_fname"] = snap_fname
    else:
        raise Exception("Could not find snapshot %s for %s" %(model_name,
                                                              snap_fname))
    if os.path.isfile(out_fname):
        info["out_fname"] = out_fname
    return info
        
    
