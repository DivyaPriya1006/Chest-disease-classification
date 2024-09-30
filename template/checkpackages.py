import importlib

# List of packages to check
packages = [
    'tensorflow', 'pandas', 'gdown', 'dvc', 'mlflow', 'notebook', 'numpy', 'matplotlib', 
    'seaborn', 'box', 'yaml', 'tqdm', 'ensure', 'joblib', 'scipy', 'flask', 'flask_cors'
]

# Function to check if a package is installed
def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is installed.")
    except ImportError:
        print(f"{package_name} is NOT installed.")

# Check each package
for package in packages:
    check_package(package)
