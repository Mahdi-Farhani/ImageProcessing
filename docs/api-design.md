## API Design
This document describes the public API surface used to compute distance metrics in a clean, simple, and unified way.

### Distance API
The API for distance computation in this project is intentionally designed using the Strategy Design Pattern.

Distance metrics naturally fit the Strategy model because:

- They share a common interface (compute(a, b))
- Each metric is an independent strategy for solving the same problem
- Users should be able to switch metrics without changing their code structure
- New metrics should be plug‑and‑play, without modifying existing code

In short:

The Strategy Pattern allows distance algorithms to vary independently from the API that uses them.

**Goals of This Architectural Choice**
Goal A — A Unified, Clean API for the User

Users (students, developers, researchers) interact with one simple function:
```
compute(a, b, metric_name)
```

They don’t need to know:

- where the algorithm is implemented
- how objects are instantiated
- how special parameters (like Minkowski’s p) are passed
- how registry or file layout works
- The complexity is fully abstracted away.

This is ideal for classroom settings, quick experiments, and clean public APIs.

---

Goal B — Extensibility Without Modifying the API

When you add a new metric, for example BhattacharyyaDistance, you only:

1. Create a file:bhattacharyya.py
2. Implement a class inheriting from DistanceMetric
3. Register it in registry.py

The API never changes.

This preserves backward compatibility—critical for open‑source projects.

---

Goal C — Decoupling Algorithms from API Logic

The API does not “know” how metrics work.

It only relies on:

- a registry lookup
- instantiating the selected class
- calling compute(a, b)

This decoupling provides:

- testability
- maintainability
- cleaner mental model
- separate responsibility layers
- preventing “God objects” or API bloat

---

**Why Strategy Is the Best Pattern Here (Compared to Alternatives)**

Compared to Factory Pattern

Factory creates objects, but doesn’t standardize computation behavior.

We needed polymorphism + interchangeable computation → Strategy fits better.

**Compared to Inheritance-Only Approaches**

Inheritance alone doesn’t solve:

- runtime switching
- registry mapping
- API decoupling
- discoverability of available strategies

**Compared to switch/if‑else trees (naive)**

Avoids:

- long conditional chains
- code duplication
- brittle logic
- violating Open/Closed Principle

Strategy + registry completely removes if‑else logic.

---

**Overview**
The API exposes functions as follow:

compute(a, b, metric_name)

Where:

- a, b are vectors or numpy arrays
- metric_name is a string (“euclidean”, “manhattan”, etc.)

**Workflow**

- API receives a request
- API fetches the metric class via registry
- API instantiates the class
- API calls compute(a, b)
- Result is returned to the user

**Summary**

The Strategy Pattern is used because:

- distance metrics are interchangeable behaviors
- the API must remain stable and clean
- new metrics should be added without changing existing code
- configurable algorithms (like Minkowski) need clean runtime parameterization
- it enforces SOLID principles
- it delivers a professional, extensible, maintainable architecture
---
