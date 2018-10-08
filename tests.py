#!/usr/bin/env python
import subprocess
import tempfile


def exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        print(fout.name)
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
# these notebook must be run in order
    exec_notebook('./example1/0-Workflow.ipynb')
    exec_notebook('./example1/1-CreateDataset.ipynb')
    exec_notebook('./example1/2-CalculateFeatures.ipynb')
    exec_notebook('./example1/3-FitModel.ipynb')
    exec_notebook('./example1/4-Predict.ipynb')
    exec_notebook('./example2/0-Workflow.ipynb')
    exec_notebook('./example2/1-SimulateTree.ipynb')
    exec_notebook('./example2/2-SimulateSequences.ipynb')


if __name__ == '__main__':
    test()
