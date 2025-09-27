# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.4.7-py3-none-any.whl https://files.pythonhosted.org/packages/6c/d7/06d13087e20388926e7423d2489e728d2e59f2453039cdb0574a7c070e76/notebook-7.4.7-py3-none-any.whl
unzip notebook-7.4.7-py3-none-any.whl
mkdir -p share
cp -r notebook-7.4.7.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
hatch build
hatch publish
```
