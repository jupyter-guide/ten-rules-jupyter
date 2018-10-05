import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        print(fout.name)
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
    _exec_notebook('./example1/0-Workflow.ipynb')
    _exec_notebook('./example2/0-Workflow.ipynb')
    _exec_notebook('./example1/Error.ipynb')
