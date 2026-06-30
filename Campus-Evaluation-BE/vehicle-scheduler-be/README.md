# Vehicle Maintenance Scheduler

A lightweight, optimized microservice built with FastAPI to solve vehicle maintenance allocation. When faced with a daily constraint on mechanic hours, this service uses dynamic programming (0/1 Knapsack) to schedule services in a way that maximizes overall operational impact.

---

## 🛠️ Project Structure
```text
vehicle-scheduler-be/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── scheduler.py      # HTTP routes & external API connections
│   ├── core/
│   │   └── config.py             # App configurations & settings
│   ├── schemas/
│   │   └── schedule.py           # Pydantic data schemas
│   ├── services/
│   │   └── scheduler_service.py  # Knapsack algorithm logic
│   └── main.py                   # App initialization
├── tests/
│   └── test_scheduler.py         # Unit tests
├── requirements.txt              # Project dependencies
└── run.py                        # Dev execution script
```

---

## 🚀 How to Run the App

### 1. Setup the Environment

#### On Windows:
```bash
# Create a virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

#### On Linux/macOS:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python run.py
```
The server will start locally at: `http://127.0.0.1:8000`

### 3. Run Tests
To verify the math behind the scheduler, run:
```bash
pytest
```

---

## 🔌 API Documentation

### Get Optimized Schedule
Runs the knapsack allocation across all depots by fetching current data from the external protected routes.

*   **URL**: `/api/v1/scheduler/optimize`
*   **Method**: `GET`
*   **Headers**:
    *   `Authorization`: `Bearer <YOUR_JWT_TOKEN>` (Required)

#### Example curl Request:
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/scheduler/optimize" \
     -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 📸 Output & Testing Screenshots

Here are the testing execution logs and results for the API:

### 1. Initial Authorization Verification
Unsuccessful access showing the intercepted verification process before the token correction:

![Auth Check](./Output%20Screen%20Shots/Screenshot%202026-06-30%20124605.png)

### 2. Successful Optimal Schedule Generation
Optimization results generating the maximum operational impact within the mechanic hours limit:

![Optimize Run 1](./Output%20Screen%20Shots/Screenshot%202026-06-30%20125836.png)

### 3. Scheduling Detail Mapping
Details of the final optimized task selections across the depots:

![Optimize Run 2](./Output%20Screen%20Shots/Screenshot%202026-06-30%20125852.png)

---

## 💡 How the Scheduler Works Under the Hood
1. **Upstream Data Collection**: The service pulls depot budgets and vehicle workloads from the external evaluation APIs using an async client (`httpx`).
2. **0/1 Knapsack Solver**: For each depot, we compute the optimal set of tasks using a 2D dynamic programming grid. This guarantees the maximum operational impact score without exceeding the mechanic hours.
3. **Sequential Reservation**: Vehicles scheduled at one depot are removed from the shared list to prevent duplicate assignments across other depots.
