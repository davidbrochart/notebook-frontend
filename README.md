# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.5.4-py3-none-any.whl https://files.pythonhosted.org/packages/59/01/05e5387b53e0f549212d5eff58845886f3827617b5c9409c966ddc07cb6d/notebook-7.5.4-py3-none-any.whl
unzip notebook-7.5.4-py3-none-any.whl
mkdir -p share
cp -r notebook-7.5.4.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
hatch build
hatch publish
```
