# Namespace Service Template

A reusable template for creating namespace-based microservices with modern web UI.

## Stack
- **FastAPI** - Python web framework
- **HTMX** - Dynamic HTML without JavaScript complexity  
- **Alpine.js** - Lightweight reactivity
- **Tailwind CSS** - Utility-first styling
- **Jinja2** - Server-side templating

## Structure

```
namespace-service/
├── app/                    # Application layer
│   ├── main.py            # FastAPI entry point
│   ├── config.py          # Environment configuration
│   ├── routes/            # API and UI routes
│   ├── services/          # Business logic + external service clients
│   ├── models/            # Data models
│   └── db/                # Database setup
├── frontend/              # UI layer
│   ├── templates/         # Jinja2 templates
│   ├── static/           # CSS, JS, images
│   └── components/       # HTMX partials
├── infra/                # Optional: deployment configs
│   ├── fly.toml          # Fly.io deployment
│   ├── Dockerfile        # Container build
│   └── k8s/             # Kubernetes manifests
├── pyproject.toml        # Dependencies
└── run.py               # Development server
```

## Usage Pattern

1. **Copy this template** to create new namespace services
2. **Customize** app name, routes, and business logic
3. **Copy infra configs** from `~/infra/` as needed
4. **Deploy** standalone or compose with other microservices

## POC Workflow

Create POCs in `~/POCs/` that combine namespace-service with other microservices:

```bash
# Example: Client dashboard POC
cp -r microservices/namespace-service ~/POCs/client-dashboard
# Customize for client management UI
# Connect to client-service backend
```

## Infrastructure Templates

Copy deployment configs from `~/infra/`:
- `~/infra/fly-configs/` → `namespace-service/infra/fly.toml`
- `~/infra/docker-compose/` → `namespace-service/infra/Dockerfile`
- `~/infra/k8s/` → `namespace-service/infra/k8s/`

Each service becomes **completely self-contained** with its own deployment story.