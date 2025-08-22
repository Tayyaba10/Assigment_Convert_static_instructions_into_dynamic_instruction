from pydantic import BaseModel
from typing import Dict

class HotelInfo(BaseModel):
    owner_name: str
    hotel_location: str
    hotel_room_price: float
    hotel_amenities: list[str]
    hotel_room_available: int
    total_rooms: int

class HotelContext(BaseModel):
    hotels: Dict[str, HotelInfo]
    
data = HotelContext(
    hotels={
        "Sannata": HotelInfo(
            owner_name="Ratan lal",
            hotel_location="123 Beach Rd",
            hotel_room_price=120.0, 
            hotel_amenities=["Free Wi-Fi", "Breakfast", "Pool"],
            hotel_room_available=180,
            total_rooms=300
            ),
        
        "Virana": HotelInfo(
            owner_name="Chaman lal", 
            hotel_location="456 Main St",
            hotel_room_price=90.0, 
            hotel_amenities=["Free Parking", "Gym", "Spa"],
            hotel_room_available=150,
            total_rooms=250
            ),
    }
)
    
class MyDataType(BaseModel):
    is_hotel_sannata_query:bool
    is_hotel_virana_query: bool
    is_hotel_sannata_political_query: bool
    is_hotel_virana_political_query: bool
    reason:str