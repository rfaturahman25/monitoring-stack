1. Install vmagent
```
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
helm show values vm/victoria-metrics-agent > values.yaml
helm upgrade --install vmagent vm/victoria-metrics-agent -f values.yaml
```

line 76 enable remotewrite to vminsert
remoteWriteUrls:
  - http://vmcluster-victoria-metrics-cluster-vminsert.default.svc.cluster.local:8480/insert/0/prometheus