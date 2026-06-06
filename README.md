# new-test-m-argo

FastAPI microservice

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8070 --reload
```

Health endpoint:

```bash
curl http://localhost:8070/health
```

Metrics endpoint (Prometheus format):

```bash
curl http://localhost:8070/metrics
```

## Observability

This service is wired for the platform's Backstage, Argo CD, and Grafana integrations.

| Integration | Catalog annotation | Value |
|-------------|-------------------|-------|
| Argo CD | `argocd/app-name` | `new-test-m-argo-dev` |
| Grafana | `grafana/dashboard-selector` | `new-test-m-argo` |

### Metrics collection

1. The app exposes Prometheus metrics at `/metrics` via `prometheus-fastapi-instrumentator` (HTTP request counts, latency, etc.).
2. The Kubernetes `Service` includes `prometheus.io/*` scrape annotations for annotation-based discovery.
3. A `ServiceMonitor` CR is included for clusters running the Prometheus Operator (e.g. kube-prometheus-stack).

After deployment, Prometheus scrapes `/metrics` on the service. Create a Grafana dashboard tagged with `new-test-m-argo` so it appears on the component's **Monitoring** tab in Backstage.

## CI/CD and GitOps

On every push to `main`, GitHub Actions:

1. Runs lint checks.
2. Builds and pushes `ghcr.io/sajjadkhan-academy/new-test-m-argo:<git-sha>` (immutable tag only).
3. Updates `apps/new-test-m-argo/overlays/dev/kustomization.yaml` in the centralized GitOps repository with that SHA.
4. Argo CD syncs the new image tag from Git and deploys to Kubernetes.

Kubernetes manifests live only in the centralized GitOps repository (`sajjadkhan-academy/argocd-centralized-repo-idp`).

### Required secret

This workflow uses the organization secret `GITOPS_REPO_TOKEN` (must have write access to the centralized GitOps repository). Ensure it is available to service repositories in your GitHub organization.
