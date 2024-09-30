## Deploying Grafana Loki on Kubernetes Cluster Using Its Helm Chart
The original Loki Scalable Helm chart comes with a wide range of default configurations, but I provided an override file named `loki-scalable-values.yml` to specify the values tailored to our deployment needs. You can review this YAML file to further customize configurations, ensuring they align with the specific requirements of your environment.

     helm install loki -n loki grafana/loki -f loki-scenario/loki-scalable-values.yml

## Adding Grafana Loki Datasource To Grafana
Instead of using the Grafana UI, you can programmatically add a Loki datasource by modifying the Grafana Helm chart. I achieved this by defining the Loki datasource within the `datasources.datasources.yaml` section of the Helm chart's configuration. This allows for automated provisioning of the Loki datasource, ensuring it is consistently deployed with the Grafana instance, avoiding manual intervention. The YAML section includes key configurations such as the datasource name, URL, access method, and authentication, which can be adjusted to suit your environment.

    helm install grafana -n grafana grafana/grafana -f loki-scenario/loki-datasource-values.yml
