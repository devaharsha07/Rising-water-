# Entity Relationship Diagram

```
User
 │
 │ enters
 ▼
Flood Parameters
 │
 │ processed by
 ▼
Machine Learning Model
 │
 │ generates
 ▼
Prediction
 │
 │ displays
 ▼
Recommendation
```

## Entities

### User
Enters environmental parameters.

### Flood Parameters
Contains rainfall, climate, drainage, and other environmental values.

### Machine Learning Model
Processes the input using the trained XGBoost model.

### Prediction
Calculates flood probability.

### Recommendation
Displays AI-generated safety recommendations.