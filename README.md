# OGC API – Processes Backend

A containerized OGC API – Processes server built with pygeoapi, demonstrating
the full job lifecycle for geospatial processing via a standard REST API.

## What this does

Exposes geospatial processes (functions) as HTTP endpoints following the
OGC API – Processes standard. Clients can submit jobs, poll status, and
retrieve results asynchronously.

## Processes

- **hello-world** — built-in echo process
- **buffer** — draws a polygon around a GeoJSON point at a given distance

## Run locally

**Prerequisites:** Docker
```bash
docker-compose up
```

Server starts at `http://localhost:8080`

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/processes` | GET | List all processes |
| `/processes/{id}` | GET | Describe a process |
| `/processes/{id}/execution` | POST | Execute a process |
| `/jobs` | GET | List all jobs |
| `/jobs/{id}` | GET | Poll job status |
| `/jobs/{id}/results` | GET | Retrieve results |

## Example: Run buffer process

**Synchronous:**
```bash
curl -X POST http://localhost:8080/processes/buffer/execution \
  -H "Content-Type: application/json" \
  -d '{"inputs": {"geom": {"type": "Point", "coordinates": [10.0, 50.0]}, "distance": 0.5}}'
```

**Asynchronous:**
```bash
curl -X POST http://localhost:8080/processes/buffer/execution \
  -H "Content-Type: application/json" \
  -H "Prefer: respond-async" \
  -d '{"inputs": {"geom": {"type": "Point", "coordinates": [10.0, 50.0]}, "distance": 0.5}}'
```

Poll status with the job ID from the `Location` header:
```bash
curl http://localhost:8080/jobs/{jobId}?f=json
```

Retrieve results:
```bash
curl "http://localhost:8080/jobs/{jobId}/results?f=json"
```