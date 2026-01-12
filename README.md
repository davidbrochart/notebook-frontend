# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.5.2-py3-none-any.whl https://files.pythonhosted.org/packages/32/55/b754cd51c6011d90ef03e3f06136f1ebd44658b9529dbcf0c15fc0d6a0b7/notebook-7.5.2-py3-none-any.whl
unzip notebook-7.5.2-py3-none-any.whl
mkdir -p share
cp -r notebook-7.5.2.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
hatch build
hatch publish
```
