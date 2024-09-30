## Deploying Grafana Loki on Kubernetes Cluster Using Its Helm Chart
The original Loki Scalable Helm chart comes with a wide range of default configurations, but I provided an override file named `loki-scalable-values.yml` to specify the values tailored to our deployment needs. You can review this YAML file to further customize configurations, ensuring they align with the specific requirements of your environment.

     helm install loki -n loki grafana/loki -f loki-scenario/loki-scalable-values.yml
