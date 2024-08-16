1. Install grafana
```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm show values grafana/grafana  > values.yaml
helm upgrade --install grafana grafana/grafana -f values.yaml
```

line 367, takutnya ngerestart nanti ilang datanya balik lagi ke awal
```
persistence:
  type: pvc
  enabled: true
  # storageClassName: default
  accessModes:
    - ReadWriteOnce
  size: 2Gi
```

get userpass
```
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

victoriametrics query http path
http://vmcluster-victoria-metrics-cluster-vmselect.default.svc.cluster.local:8481/select/0/prometheus/

loki query http path
http://loki-distributed-gateway.default.svc.cluster.local

import kube-state-metrics dashboard
13332