# Installation

## Download this repository

You will need git to install this repository using these commands:

    $ git clone https://github.com/jayalabanda/projet-ADD.git
    $ git cd projet-ADD

## Install Anaconda

You can download [Anaconda](https://www.anaconda.com/distribution/), which comes included with most necessary libraries for this project, such as NumPy, Pandas and Matplotlib.

## Create an R environment

We recommend you create a new Anaconda environment that has the R kernel. You can do so following these steps:

    $ conda env create -n r_env
    $ conda activate r_env

Note: you need an [installation of R](https://cran.r-project.org/) in your system.

1. Open an elevated Anaconda Prompt (with administrator privileges) with your newly created environment.
2. Type `conda install -c anaconda jupyter_client`
3. Move to your R installation folder. By default, the directory should look something like `C:\Program Files\R\R-4-0-4\bin\x64`. Use `cd path` with the previous path.
4. Run R from the Anaconda Prompt using `R.exe`.
5. You will notice you are in an R session. Now run these commands in order:
    1. `install.packages("devtools")`
    2. `devtools::install_github("IRkernel/IRkernel")`
    3. `IRkernel::installspec()`
6. Open Anaconda Prompt and type `jupyter lab`. You should be able to see both R and Python's kernels.

Now, every time you want to use Jupyter Lab with the R kernel you only need to open Anaconda Prompt and run:

    $ conda activate r_env
    $ jupyter lab

Now you're ready to run this project! :blush:
