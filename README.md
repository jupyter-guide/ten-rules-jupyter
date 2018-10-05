# Ten Simple Rules for Reproducible Research in Jupyter Notebooks

This repository is a supplement to the "Ten Simple Rules for Reproducible Research in Jupyter Notebook" paper [ref].

The example notebooks demonstrate some of rules. 

## Example 1
This example demonstrates a reproducible 4-step workflow for predicting a protein fold classification using a Machine Learning approach.

---

**Rule 8: Expect Your Notebooks to Be Read, Run, and Explored.** The nbviewer links below provide a non-interactive preview of notebooks and ![Binder](https://mybinder.org/badge.svg) buttons launch
notebooks in your web browser using the Binder ([mybinder.org](https://mybinder.org/)) server (may be slow!). The HTML links provide a permanent static record of the notebooks. All notebooks can also be launched directly from the links in the 0-Workflow.ipynb top-level notebook.

---

| Nbviewer | Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
| [0-Workflow.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F0-Workflow.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example1/0-Workflow.html) |
| [1-CreateDataset.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F1-CreateDataset.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F1-CreateDataset.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example1/1-CreateDataset.html) |
| [2-CalculateFeatures.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F2-CalculateFeatures.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F2-CalculateFeatures.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example1/2-CalculateFeatures.html) |
| [3-FitModel.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/3-FitModel.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F3-FitModel.ipynb) |[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F3-FitModel.ipynb)  | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example1/3-FitModel.html) |
| [4-Predict.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example1/4-Predict.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example1%2F4-Predict.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example1%2F4-Predict.ipynb)| [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example1/4-Predict.html) |

---

**Rule 7: Share and Explain Your Data.** To enable reproducibility, we provide a example1/data directory with all data required to run the workflow. A description of the data with download location and download date is [available](./example1/data/Datasets.md).

---

## Example 2

This example demonstrates a reproducible 2-step workflow for simulating a phylogenetic tree and sequences.

| Nbviewer | Jupyter Notebook | Jupyter Lab | HTML |
| ---      | --               | ---         | ---  |
| [0-Workflow.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F0-Workflow.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F0-Workflow.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example2/0-Workflow.html) |
| [1-SimulateTree.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/1-SimulateTree.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F1-SimulateTree.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F1-SimulateTree.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example2/1-SimulateTree.html) |
| [2-SimulateSequences.ipynb](https://nbviewer.jupyter.org/github/jupyter-guide/ten-rules-jupyter/blob/master/example2/2-SimulateSequences.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?filepath=example2%2F2-SimulateSequences.ipynb) | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-guide/ten-rules-jupyter/master?urlpath=lab/tree/example2%2F2-SimulateSequences.ipynb) | [HTML](https://cdn.rawgit.com/jupyter-guide/ten-rules-jupyter/dd3a89ad/example2/2-SimulateSequences.html) |
