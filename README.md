# License Plate Baseline

This repo is a starting point for using License Plate Library

## Dependencies

- Python>=3.6
- CUDA=10.0
- Keras==2.2.0

### Installation

**Virtualenv**

```
python3 -m venv venv
source venv/bin/activate
```

**Anaconda**

```
# create environment 
conda create --name license_test python=3.6
conda activate license_test
```
**Install packages and dependencies**

```
# install dependencies for cpu 
pip install -r requirements-cpu.txt
# or install dependencies for gpu 
pip install -r requirements-gpu.txt

# install face recognition library
pip install --upgrade greenlab-library
```

## Getting Started

**Steps:**

1. Change the image path and parameters in `configs/server_api.yaml` file.
3. Run `main.py` file
3. Check the results at `logs/outputs/output.png`
