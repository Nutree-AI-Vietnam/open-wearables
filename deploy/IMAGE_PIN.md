# Open Wearables image pin (Nutree)

Nutree deploys the published upstream release images, pinned to an exact tag:

| Role | Image |
| --- | --- |
| Backend (nutree-ow-stg-api, nutree-ow-stg-sync, nutree-ow-stg-scheduler) | `themomentum/open-wearables-backend:0.9.0` |
| Portal (nutree-ow-stg-portal) | `themomentum/open-wearables-frontend:0.9.0` |

Staging and production are separate stacks on the **same tag**. To upgrade, bump the tag
in `render.yaml` (all four services together) in a reviewed PR, verify on staging, then
roll production. Never use `latest` or `nightly`.

Reference: https://openwearables.io/docs/deployment/docker
