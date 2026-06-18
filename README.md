# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.6.0-py3-none-any.whl https://files.pythonhosted.org/packages/93/d1/e617c40db57ff40e75f43a7d4d1c305e3a54c053ab5cb0534a6c314664f9/notebook-7.6.0-py3-none-any.whl
unzip notebook-7.6.0-py3-none-any.whl
mkdir -p share
cp -r notebook-7.6.0.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
# update version in `pyproject.toml`, and also `jupyterlab-js` version
hatch build
hatch publish
```
