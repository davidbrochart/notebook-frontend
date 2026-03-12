# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.5.5-py3-none-any.whl https://files.pythonhosted.org/packages/f8/aa/cbd1deb9f07446241e88f8d5fecccd95b249bca0b4e5482214a4d1714c49/notebook-7.5.5-py3-none-any.whl
unzip notebook-7.5.5-py3-none-any.whl
mkdir -p share
cp -r notebook-7.5.5.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
hatch build
hatch publish
```
