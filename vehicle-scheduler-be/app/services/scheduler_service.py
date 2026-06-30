from functools import total_ordering
from typing import List, Dict, Tuple, Any
from app.schemas.schedule import Depot, Vehicle, ScheduledDepotResult

class SchedulerService:
    @staticmethod
    def solve_knapsack(vehicles: List[Vehicle],budget: int) -> Tuple[int, List[str],int]:
        n = len(vehicles)
        dp = [[0] * (budget+1) for _ in range(n+1)]

        for i in range(1,n+1):
            v = vehicles[i-1]
            for w in range(budget + 1):
                if v.Duration <=w:
                    dp[i][w] = max(dp[i-1][w],dp[i-1][w-v.Duration]+)
                else:
                    dp[i][w] = dp[i-1][w]
        selected_task_ids = []
        w = budget
        total_duration = 0
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_task_ids.append(vehicles[i - 1].TaskID)
                total_duration += vehicles[i - 1].Duration
                w -= vehicles[i - 1].Duration
        
        return dp[n][budget],selected_task_ids,total_duration