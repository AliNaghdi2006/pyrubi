from typing import List

class MapView:
	def __init__(self, map_view_data: dict) -> None:
		self.__map_view_data = map_view_data 
	
	@property
	def tile_side_count(self) -> int:
		return self.__map_view_data["tile_side_count"]
	
	@property
	def tile_urls(self) -> List[str]:
		return self.__map_view_data["tile_urls"]
	
	@property
	def x_loc(self) -> float:
		return self.__map_view_data["x_loc"]
	
	@property
	def y_loc(self) -> float:
		return self.__map_view_data["y_loc"]
	
	def __dict__(self) -> dict:
		return self.__map_view_data

class Location:
	def __init__(self, location_data: dict) -> None:
		self.__location_data = location_data
	
	@property
	def longitude(self) -> float:
		return self.__location_data["longitude"]
	
	@property
	def latitude(self) -> float:
		return self.__location_data["latitude"]
	
	@property
	def map_view(self) -> MapView:
		return MapView(self.__location_data["map_view"])
	
	def __dict__(self) -> dict:
		return self.__location_data