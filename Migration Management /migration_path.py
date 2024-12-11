from typing import Optional

class MigrationPath:
    def __init__(self,
                 path_id: int,
                 species: str,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int] = None) -> None:
        self.path_id = path_id                    # Unique identifier for the migration path
        self.species = species                     # Species involved in the migration
        self.start_location = start_location       # Starting habitat for the migration
        self.destination = destination             # Destination habitat for the migration
        self.duration = duration                   # Duration of the migration path (optional)


    def get_migration_path_details(path_id) -> dict:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass