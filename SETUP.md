

- make sure you have pre-commits
  [installed](https://pre-commit.com/#install)
- use template https://github.com/fastai/nbdev-template
- create env `python -m venv br-env`
- activate env `source br-env/bin/activate`
- install stuff `pip install nbdev pre-commit`
- update settings.ini see
  [this](https://github.com/fastai/nbdev/blob/master/settings.ini)
- added `.pre-commit-config.yaml`
- install pre-commit hooks: `pre-commit install`
- clean up `index.ipynb` (`{{}}` did not get picked up correctly?)
- add dependencies in `settings.ini` and run to install package locally
  `pip install -e '.[dev]'`