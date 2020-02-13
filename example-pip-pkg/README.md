# Example python package

example how to create python package and deploy to pip registory

## Prerequisite

- install wheel

```python
python3 -m pip install --user --upgrade setuptools wheel
```

- intstall twine

```python
python3 -m pip install --user --upgrade twine
```

## Build & Deploy Steps

- Go to setup.py directories and run the following command
  - it will generated a lot of files include *dist* directory which include package

```python
python3 setup.py sdist bdist_wheel
```

- Upload all file to test server
  - after finish uploading try to visit the link *https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE*
  - don't forget to create API token on [website](https://test.pypi.org/account/register/) first

```python
# first upload
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

- Or Upload to the world
  - don't forget to create API token on [website](https://pypi.org/account/register/) first
  
```python
# no need for url twine will use default one
twine upload dist/*
```

## How to use

- for test server

```python
pip3 install -i https://test.pypi.org/simple/ example-pkg-hta-helloworld
```

- for global

```python
pip3 install example-pkg-hta-helloworld
```

- Then use in python3 console

```python
#access python console
python3

import hta_helloworld_pkg
```

### References

- [Official document](https://packaging.python.org/tutorials/packaging-projects/#packaging-your-project)
- [__init__.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html) responsibilities
  