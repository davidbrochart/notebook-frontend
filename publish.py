import sys
from subprocess import check_output

import toml


version = sys.argv[1]
jupyterlab_version = sys.argv[2]

check_output("git clean -fdx".split())
check_output(f"curl -L --output notebook-{version}-py3-none-any.whl https://pypi.org/packages/py3/n/notebook/notebook-{version}-py3-none-any.whl".split())
check_output(f"unzip notebook-{version}-py3-none-any.whl".split())
check_output("mkdir -p share".split())
check_output(f"cp -r notebook-{version}.data/data/share/jupyter share/".split())
check_output("cp -r notebook/static src/notebook_frontend/".split())
check_output("cp -r notebook/templates src/notebook_frontend/".split())

with open("pyproject.toml", "rt") as f:
    data = toml.load(f)

with open("pyproject.toml", "wt") as f:
    data["project"]["version"] = version
    data["project"]["dependencies"] = [f"jupyterlab-js=={jupyterlab_version}"]
    toml.dump(data, f)

check_output("hatch build".split())
check_output("hatch publish".split())
check_output(["git", "commit", "-am", f"Release v{version}"])
check_output("git push".split())
