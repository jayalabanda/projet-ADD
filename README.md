# projet-ADD

Exploratory data analysis on the Velib bike stations dataset.

## Quick Start

This repository is a collaborative project for our Data Analysis course, in which we have to detect clusters in the data and later predict the loading of a given Velib station in Paris.

<img src=https://vl-media.fr/wp-content/uploads/2018/02/nouveau-Velib-Metropole-25-octobre-2017-Paris_0_729_486.jpg
    title="velib" height=150/>

This project is done in both Python and R.

Link to our report:
[Overleaf](https://www.overleaf.com/5435171335nmvyzcyqdftg).

### If you want to execute the code on your own machine *with Python*

Install [Anaconda](https://www.anaconda.com/distribution/) and [git](https://git-scm.com/downloads).

Next, clone this project by typing the following commands in a terminal:

    $ git clone https://github.com/jayalabanda/projet-ADD.git
    $ cd projet-ADD

Then, run these commands:

    $ conda env create -n project -f requirements.txt
    $ conda activate project

Finally, start Jupyter Notebook.

    $ jupyter notebook

### If you want to execute the code on your own machine *with R*

Install the R kernel for Jupyter. Instructions are here: [IRkernel](https://github.com/IRkernel/IRkernel) and here: [Rich Pauloo](https://richpauloo.github.io/2018-05-16-Installing-the-R-kernel-in-Jupyter-Lab/).

Then launch Jupyter Lab (some code cells don't render in Jupyter Notebook).

Detailed instructions for installing and using the R kernel are [here](https://github.com/jayalabanda/projet-ADD/blob/master/INSTALL.md).

Our to-do list :

- [ ] Commentate PCA graphs
- [ ] Transcribe from Python to R
- [ ] Write our final report on Overleaf, only two months left!
