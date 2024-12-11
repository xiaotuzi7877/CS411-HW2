# Wildlife Tracker System

This project implements a **Wildlife Tracker System** designed to manage wildlife populations, their habitats, and migration patterns. The system allows users to register, update, and manage animals, habitats, and migration events. The implementation employs a modular design with a **Manager/Mediator Pattern** for clear separation of responsibilities and better maintainability.

## Features
- **Animal Management:** Register, update, and track specific animals.
- **Habitat Management:** Create and manage habitats, assign animals to habitats, and manage habitat properties like size, environment, and location.
- **Migration Management:** Manage migration paths, scheduling, and tracking of animal movements between habitats.

## Directory Structure
The project is structured into modular folders, each handling a specific responsibility:
wildlife-tracker/

├── animal_management/

│   ├── __init__.py
│   ├── animal_manager.py
│   ├── animal.py

├── habitat_management/
│   ├── __init__.py
│   ├── habitat_manager.py
│   ├── habitat.py

├── migration_management/
│   ├── __init__.py
│   ├── migration_manager.py
│   ├── migration_path.py

├── formal_specifications.py

├── README.md

## Late Sumbmission for professor 
![Proof of Late Submission](Prove%20of%20Late%20Submission.png)

