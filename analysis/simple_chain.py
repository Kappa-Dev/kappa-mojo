##
## Analyze simple chain model
##
## Author: Yarden Katz
##
import matplotlib
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

import mojo_utils
import kappy
import kappy.kappa_snap as kappa_snap

def get_chain_hist(snap_obj, node_type="C"):
    """
    Get chain histogram. 
    Assume that the rest are forming chains, meaning
    the number of components is equal to the chain length
    """
    num_blocks_per_complex = []
    for abundance, comp in snap_obj.complexes:
        agent_types = comp.get_agent_types()
        if node_type not in agent_types:
            # skip over complexes not made up of node type
            continue
        # assume that the rest are forming chains, meaning
        # the number of components is equal to the chain length
        num_blocks = agent_types[node_type]
        # take abundance into account
        num_blocks_per_complex.append([num_blocks] * abundance)
    # flatten list
    num_blocks_per_complex = [elt for sublist in num_blocks_per_complex \
                              for elt in sublist]
    num_blocks_per_complex.sort()
    num_blocks_per_complex = np.array(num_blocks_per_complex)
    complex_sizes = \
      np.arange(num_blocks_per_complex.min(), num_blocks_per_complex.max() + 1)
    histogram, histogram_bins = \
      np.histogram(num_blocks_per_complex, complex_sizes)
    return {"num_blocks_per_complex": num_blocks_per_complex,
            "histogram": histogram,
            "histogram_bins": histogram_bins[0:-1]}

def main():
    info = mojo_utils.get_model_info("simple_chain")
    print("Model information for simple chain: ")
    print(info)
    # load Kappa snapshot (in JSON format)
    snap_obj = kappa_snap.KappaSnapshot(from_fname=info["snap_fname"])
    snapshot_time = snap_obj["snapshot_time"]
    # calculate number of chains we have
    chain_hist = get_chain_hist(snap_obj)
    # make plot of chain length distribution
    plt.figure(figsize=(4,4))
    sns.set_style("ticks")
    # plot without binning
    #plt.bar(chain_hist["histogram_bins"], chain_hist["histogram"], color="k")
    # plot with binning
    plt.hist(chain_hist["num_blocks_per_complex"], color="k", bins=30)
    plt.ylabel("Number of complexes", fontsize=10)
    plt.xlabel("Chain length", fontsize=10)
    plt.title("Chain length distribution (at t = %.1f)" %(snapshot_time))
    plt.savefig("../plots/simple_chain.png")

if __name__ == "__main__":
    main()
