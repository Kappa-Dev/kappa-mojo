Contributing models
================

- All models should terminate (ideally with a snapshot); i.e., one should not have to pass a pause
condition to KaSim.

- The basic template for a model would be to have a model name and
generate snapshots/outputs/documentation using that name. For
instance, if the model is called ``simple_chain``, then add the
following:

	* ``models/simple_chain.ka``: Kappa program
	* ``snapshot/simple_chain.json``: snapshot that the Kappa program
outputs
	* ``outputs/simple_chain.out``: outputs (observables) from Kappa program
	* ``docs/simple_chain.md``: documentation for model

