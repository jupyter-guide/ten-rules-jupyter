# Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks
[![Build Status](https://api.travis-ci.com/jupyter-guide/ten-rules-jupyter.svg?branch=master)](https://www.travis-ci.org/jupyter-guide/ten-rules-jupyter)
[![GitHub License](https://img.shields.io/github/license/jupyter-guide/ten-rules-jupyter.svg)](https://github.com/sbl-sdsc/mmtf-spark/blob/master/LICENSE)

This repository is a supplement to

["Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks"](https://doi.org/10.1371/journal.pcbi.1007007) 

[![Tweets](https://img.shields.io/badge/dynamic/json.svg?url=https://api.altmetric.com/v1/id/64040119&label=Altmetric&query=$.score&style=social)](https://www.altmetric.com/details/64040119)

[![Twitter](https://img.shields.io/badge/Tweet--lightgrey.svg?logo=twitter&style=social)](https://twitter.com/fperez_org/status/1159903342249701377)
[![Tweets](https://img.shields.io/badge/dynamic/json.svg?url=https://api.altmetric.com/v1/id/64040119&label=Tweets&query=$.cited_by_tweeters_count&style=social)](https://www.altmetric.com/details/64040119) 



and its preprint

["Ten Simple Rules for Reproducible Research in Jupyter Notebook"](https://arxiv.org/abs/1810.08055) 

[![Tweets](https://img.shields.io/badge/dynamic/json.svg?url=https://api.altmetric.com/v1/id/49908150&label=Altmetric&query=$.score&style=social)](https://www.altmetric.com/details/49908150)

[![Twitter](https://img.shields.io/badge/Tweet--lightgrey.svg?logo=twitter&style=social)](https://twitter.com/peterwrose/status/1053156027602878465)
[![Tweets](https://img.shields.io/badge/dynamic/json.svg?url=https://api.altmetric.com/v1/id/49908150&label=Tweets&query=$.cited_by_tweeters_count&style=social)](https://www.altmetric.com/details/49908150)

Explore the example notebooks below for an application of the Ten Simple Rules.

In addition, we have setup [jupyter-guide](https://github.com/jupyter-guide/jupyter-guide) to crowdsource more technical and in-depth tutorials and to keep up with the rapidly evolving Jupyter ecosystem. We encourage you to contribute and share your expertise.

## Example 1
This example demonstrates a reproducible 4-step workflow for predicting a protein fold classification using a Machine Learning approach.

---

**Rule 9: Design Your Notebooks to Be Read, Run, and Explored.** The nbviewer links below provide a non-interactive preview of notebooks and ![Binder](https://mybinder.org/badge_logo.svg) buttons launch
Jupyter Notebook or Jupyter Lab in your web browser using the Binder ([mybinder.org](https://mybinder.org/)) server (may be slow!). (See the Binder website how to setup links to a Git repository.) The HTML links provide a permanent static record of the notebooks. All notebooks can also be launched directly from the links in the 0-Workflow.ipynb top-level notebook.

---

| Nbviewer | Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
| [0-Workflow.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F0-Workflow.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/0-Workflow.html) |
| [1-CreateDataset.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F1-CreateDataset.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/1-CreateDataset.html) |
| [2-CalculateFeatures.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F2-CalculateFeatures.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/2-CalculateFeatures.html) |
| [3-FitModel.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/3-FitModel.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F3-FitModel.ipynb) |[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F3-FitModel.ipynb)  | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/3-FitModel.html) |
| [4-Predict.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/4-Predict.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F4-Predict.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F4-Predict.ipynb)| [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example1/4-Predict.html) |

---

**Rule 8: Share and Explain Your Data.** To enable reproducibility, we provide a example1/data directory with all data required to run the workflow. A description of the data with download location and download date is [available](./example1/data/Datasets.md).

---

## Example 2

This example demonstrates a reproducible 2-step workflow for simulating a phylogenetic tree and sequences.

| Nbviewer | Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
| [0-Workflow.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F0-Workflow.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example2/0-Workflow.html) |
| [1-SimulateTree.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/1-SimulateTree.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F1-SimulateTree.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F1-SimulateTree.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example2/1-SimulateTree.html) |
| [2-SimulateSequences.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/2-SimulateSequences.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F2-SimulateSequences.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F2-SimulateSequences.ipynb) | [HTML](https://rawgit.com/jupyter-guide/ten-rules-jupyter/master/example2/2-SimulateSequences.html) |

## Runnning Jupyter Notebooks on CyVerse/VICE
The new [VICE (Visual Interactive Computing Environment)](https://cyverse-visual-interactive-computing-environment.readthedocs-hosted.com/en/latest/index.html) in the [CyVerse Discovery Environment](https://www.cyverse.org/discovery%20environment) enables users to run Jupyter Lab in a production environment. To use VICE, sign up for a free [CyVerse account](https://www.cyverse.org/create-account).

[![Vice](vice/vice_badge.png)](https://de.cyverse.org/de/?type=apps&app-id=8ec235d8-f173-11e9-a56f-008cfa5ae621&system-id=de)

[Follow these step to run Jupyter Lab on VICE](https://cyverse-visual-interactive-computing-environment.readthedocs-hosted.com/en/latest/user_guide/quick-jupyter.html)

## Contact Us
If you encounter any problems with this repository, please report them [here](https://github.com/jupyter-guide/ten-rules-jupyter/issues).
