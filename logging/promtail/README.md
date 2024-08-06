1. Install promtail
```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm show values grafana/promtail > values.yaml
Change `client` values on values.yaml to url loki gateway `http://loki-distributed-gateway.{{namespace}}.svc.cluster.local/loki/api/v1/push`  (line 413)
helm upgrade --install promtail grafana/promtail -f values.yaml
```