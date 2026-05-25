import os
from pathlib import Path

# Define the project name
project_name = "ecommerce_backend"

# List of all files and directories to create
list_of_files = [
    f"{project_name}/app/main.py",
    f"{project_name}/app/database.py",
    f"{project_name}/app/config.py",
    # Routes
    f"{project_name}/app/routes/auth_routes.py",
    f"{project_name}/app/routes/product_routes.py",
    f"{project_name}/app/routes/cart_routes.py",
    f"{project_name}/app/routes/order_routes.py",
    # Services
    f"{project_name}/app/services/auth_service.py",
    f"{project_name}/app/services/product_service.py",
    f"{project_name}/app/services/cart_service.py",
    f"{project_name}/app/services/order_service.py",
    # Repositories
    f"{project_name}/app/repositories/user_repository.py",
    f"{project_name}/app/repositories/product_repository.py",
    f"{project_name}/app/repositories/cart_repository.py",
    f"{project_name}/app/repositories/order_repository.py",
    # Schemas
    f"{project_name}/app/schemas/user_schema.py",
    f"{project_name}/app/schemas/product_schema.py",
    f"{project_name}/app/schemas/order_schema.py",
    # Utils
    f"{project_name}/app/utils/jwt_handler.py",
    f"{project_name}/app/utils/password_handler.py",
    f"{project_name}/app/utils/response_handler.py",
    # Middleware
    f"{project_name}/app/middleware/auth_middleware.py",
    # SQL scripts
    f"{project_name}/sql/tables.sql",
    f"{project_name}/sql/seed.sql",
    # Root level files
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",
]

def create_structure():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        # Create directory if it doesn't exist
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            print(f"Creating directory: {filedir}")

        # Create empty file if it doesn't exist or is empty
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass  # Just creating an empty file
            print(f"Creating empty file: {filepath}")
        else:
            print(f"{filename} already exists")

if __name__ == "__main__":
    print("Starting project structure generation...")
    create_structure()
    print("Project structure created successfully!")