from app.services.scheduler_service import SchedulerService
from app.schemas.schedule import Vehicle

def test_knapsack_optimization():
    vehicles = [
        Vehicle(TaskID="task-1", Duration=5, Impact=10),
        Vehicle(TaskID="task-2", Duration=3, Impact=6),
        Vehicle(TaskID="task-3", Duration=2, Impact=5)
    ]
    budget = 5

    max_impact,selected,duration = SchedulerService.solve_knapsack(vehicles,budget)

    assert max_impact == 11
    assert "task-2" in selected
    assert "task-3" in selected
    assert duration == 5
    