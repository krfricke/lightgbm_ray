from setuptools import find_packages, setup

setup(
    name="lightgbm_ray",
    packages=find_packages(where=".", include="lightgbm_ray*"),
    version="0.0.1",
    author="Ray Team",
    description="A Ray backend for distributed LightGBM",
    long_description="A distributed backend for LightGBM built on top of "
    "distributed computing framework Ray.",
    url="https://github.com/ray-project/lightgbm_ray",
    install_requires=[
        "lightgbm>=3.2.1", "ray", "numpy>=1.16,<1.20", "pandas", "pyarrow", "xgboost_ray>=0.1.1"
    ])
