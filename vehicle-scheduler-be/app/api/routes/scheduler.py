from fastapi import APIRouter, Header, HTTPException
import httpx
from app.core.config import settings
from app.schemas.schedule import DepotListResponse, VehicleListResponse, ScheduleSummaryResponse
from app.services.scheduler_service import SchedulerService

router = APIRouter(prefix="/scheduler", tags=["Scheduler"])
scheduler_service = SchedulerService()

@router.get("/optimize", response_model=ScheduleSummaryResponse)
async def optimize_schedule(authorization: str = Header(...)):
    headers = {"Authorization": authorization}
    
    async with httpx.AsyncClient() as client:
        # Fetch depots
        depots_res = await client.get(f"{settings.EVALUATION_API_BASE_URL}/depots", headers=headers)
        if depots_res.status_code != 200:
            raise HTTPException(
                status_code=depots_res.status_code, 
                detail=f"Failed to fetch depots: {depots_res.text}"
            )
            
        # Fetch vehicles
        vehicles_res = await client.get(f"{settings.EVALUATION_API_BASE_URL}/vehicles", headers=headers)
        if vehicles_res.status_code != 200:
            raise HTTPException(
                status_code=vehicles_res.status_code, 
                detail=f"Failed to fetch vehicles: {vehicles_res.text}"
            )
            
    depot_data = DepotListResponse(**depots_res.json())
    vehicle_data = VehicleListResponse(**vehicles_res.json())
    
    summary = scheduler_service.schedule_depots(depot_data.depots, vehicle_data.vehicles)
    return summary
