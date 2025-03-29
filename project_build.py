import os

def create_file(file_path, content=""):
    """Creates an empty file (or with specified content) at the given path."""
    with open(file_path, "w") as f:
        f.write(content)

def create_structure(base, structure):
    """
    Recursively creates directories and files.
    
    - If structure is a list, each item is considered a file name.
    - If structure is a dict, each key represents a subdirectory.
      Use an empty string key "" for files directly in the folder.
    """
    if isinstance(structure, list):
        # Create files in the current directory
        for file_name in structure:
            file_path = os.path.join(base, file_name)
            create_file(file_path)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            if key == "":
                # Files directly under this directory
                for file_name in value:
                    file_path = os.path.join(base, file_name)
                    create_file(file_path)
            else:
                # Create a subdirectory and recursively add its content
                new_dir = os.path.join(base, key)
                os.makedirs(new_dir, exist_ok=True)
                create_structure(new_dir, value)

def main():
    # Define the base project directory
    base_dir = "your_project"
    
    # Define the project structure
    project_structure = {
        "configs": ["train_config.yaml", "model_config.yaml"],
        "data": {
            "raw": [],
            "processed": []
        },
        "docs": ["design.md", "api.md"],
        "experiments": {
            "tensorboard_logs": [],
            "mlflow_runs": []
        },
        "models": {
            "": ["base_model.py", "resnet.py"],  # Files directly under models/
            "utils": []
        },
        "scripts": ["train.py", "predict.py", "deploy_api.sh"],
        "src": {
            "data": ["datasets.py", "transforms.py", "loaders.py"],
            "utils": ["logger.py", "config.py"],
            "engine": ["trainer.py", "evaluator.py"]
        },
        "tests": ["test_data.py", "test_models.py"],
    }
    
    # Top-level files to be created directly under the project root
    top_level_files = ["requirements.txt", "Dockerfile", "README.md"]
    
    # Create the base project directory
    os.makedirs(base_dir, exist_ok=True)
    
    # Create all defined subdirectories and files
    for folder, content in project_structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        create_structure(folder_path, content)
    
    # Create the top-level files
    for file_name in top_level_files:
        file_path = os.path.join(base_dir, file_name)
        create_file(file_path)

if __name__ == "__main__":
    main()
