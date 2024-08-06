1. Install vmalert
```
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
helm show values vm/victoria-metrics-alert > values.yaml
helm upgrade --install vmagent vm/victoria-metrics-alert -f values.yaml
```