from pydantic import BaseModel
from typing import List

class Depot(BaseModel):
    ID: int
    MechanicHours: int  # Fixed spelling to match external API response

class Vehicle(BaseModel):
    TaskID: str
    Duration: int
    Impact: int 

class DepotListResponse(BaseModel):
    depots: List[Depot]

class VehicleListResponse(BaseModel):
    vehicles: List[Vehicle]

class ScheduledDepotResult(BaseModel):
    depot_id: int
    mechanic_hours_budget: int  # Fixed spelling to match
    hours_used: int
    total_impact_score: int
    scheduled_tasks: List[str]

class ScheduleSummaryResponse(BaseModel):
    total_depots: int
    total_allocated_hours: int
    total_impact_score: int
    results: List[ScheduledDepotResult]
