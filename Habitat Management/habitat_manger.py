from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat


class HabitatManager:
    def __init__(self, path_id: int, species: str, start_location: 'Habitat', destination: 'Habitat', duration: Optional[int] = None):
        self.path_id = path_id
        self.species = species
        self.start_location = start_location  # A Habitat instance
        self.destination = destination  # A Habitat instance
        self.duration = duration
    
    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass

    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

