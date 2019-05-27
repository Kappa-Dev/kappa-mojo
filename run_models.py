#!/usr/bin/python
##
## Author: Yarden Katz
##
import os
import sys
import time
import glob
from shutil import which
import subprocess

OUTDIR = "./outputs/"
SNAPDIR = "./snapshots/"

def check_KaSim():
    """
    Check if KaSim is available on path.
    Note: we could make this run with kappy, but it seems
    like overkill for now.
    """
    if which("KaSim") is not None:
        print("Found KaSim on path.")
        return
    raise Exception("Need KaSim to be available on path.")

def run_KaSim(model_fname):
    # redundant check for now
    if not model_fname.endswith(".ka"):
        return None
    model_basename = os.path.basename(model_fname)
    model_name = model_basename.split(".ka")[0]
    dir_name = os.path.dirname(model_fname)
    out_fname = os.path.join(OUTDIR, "%s.out" %(model_name))
    snapshot_fname = os.path.join(SNAPDIR, model_basename)
    # remove older output/snapshot files
    older_files = [out_fname, snapshot_fname]
    for old_fname in older_files:
        if os.path.isfile(old_fname):
            print("Removing previous file: %s" %(old_fname))
            os.unlink(old_fname)
    print("Running %s" %(model_basename))
    # run KaSim (and don't generate log files)
    cmd = \
       '''KaSim --no-log -o {out_fname} {model_fname}'''.format(out_fname=out_fname,
                                                                model_fname=model_fname)
    ret_val = os.system(cmd)
    if ret_val != 0:
        raise Exception("Failed to execute %s" %(cmd))
    return ret_val

def run_models():
    t1 = time.time()
    fnames = glob.glob("./models/*.ka")
    num_models = len(fnames)
    print("Running on %d models" %(num_models))
    for fname in fnames:
        run_KaSim(fname)
    t2 = time.time()
    print("Running all models took %.1f seconds" %(t2 - t1))

def main():
    check_KaSim()
    run_models()

if __name__ == "__main__":
    main()
