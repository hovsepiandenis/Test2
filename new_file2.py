Sample Config
version: 1.0

version: 2.0

name: Windows Python application

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs: 
  build:
    runs-on: windows-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest
