from typing import List, Dict, Tuple, Any
from app.schemas.schedule import Depot, Vehicle, ScheduledDepotResult

class SchedulerService:
    @staticmethod
    def solve_knapsack(vehicles: List[Vehicle], budget: int) -> Tuple[int, List[str], int]:
        n = len(vehicles)
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            v = vehicles[i - 1]
            for w in range(budget + 1):
                if v.Duration <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - v.Duration] + v.Impact)
                else:
                    dp[i][w] = dp[i - 1][w]
                    
        selected_task_ids = []
        w = budget
        total_duration = 0
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_task_ids.append(vehicles[i - 1].TaskID)
                total_duration += vehicles[i - 1].Duration
                w -= vehicles[i - 1].Duration
        
        return dp[n][budget], selected_task_ids, total_duration

    def schedule_depots(self, depots: List[Depot], vehicles: List[Vehicle]) -> Dict[str, Any]:
        results = []
        total_impact = 0
        total_hours = 0

        available_vehicles = list(vehicles)

        for depot in depots:
            total_hours += depot.MechanicHours  # Fixed spelling
            max_impact, selected_task, hours_used = self.solve_knapsack(available_vehicles, depot.MechanicHours)

            available_vehicles = [v for v in available_vehicles if v.TaskID not in selected_task]

            results.append(
                ScheduledDepotResult(
                    depot_id=depot.ID,
                    mechanic_hours_budget=depot.MechanicHours,  # Fixed spelling
                    hours_used=hours_used,
                    total_impact_score=max_impact,
                    scheduled_tasks=selected_task
                )
            )
            total_impact += max_impact

        return {
            "total_depots": len(depots),
            "total_allocated_hours": total_hours,
            "total_impact_score": total_impact,
            "results": results
        }
