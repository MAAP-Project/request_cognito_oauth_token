A small python module to quickly get a JSON Web Token (JWT) from an OAuth 2.0 token endpoint activated using AWS Cognito. 

## Requirements

- `python`
- A Cognito client deployed and a secret containing the Cognito client details
- AWS credentials accessible in the environment

## Installation

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

```
python src.py "MY_SECRET"
```