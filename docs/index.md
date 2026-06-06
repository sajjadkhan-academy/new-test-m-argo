# Documentation for new-test-m-argo

## Overview

FastAPI microservice

This microservice has been automatically generated using the Backstage `python-fastapi` template.

## Tech Stack
- **Framework**: FastAPI (Python)
- **Deployments**: Managed via ArgoCD GitOps
- **Metrics**: Prometheus `/metrics` endpoint with ServiceMonitor
- **Portal**: Argo CD and Grafana tabs via Backstage catalog annotations

## Getting Started

### Local Development
To run this service locally:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8070 --reload
   ```

### Metrics

Prometheus metrics are available at `/metrics`:

```bash
curl http://localhost:8070/metrics
```

In Kubernetes, Prometheus discovers this service through scrape annotations on the `Service` and the bundled `ServiceMonitor`. Tag Grafana dashboards with `new-test-m-argo` to surface them on the Backstage **Monitoring** tab.
