## Deploying Grafana Loki on Kubernetes Cluster Using Its Helm Chart
The original Loki Scalable Helm chart comes with a wide range of default configurations, but I provided an override file named `loki-scalable-values.yml` to specify the values tailored to our deployment needs. You can review this YAML file to further customize configurations, ensuring they align with the specific requirements of your environment.

     helm install loki -n loki grafana/loki -f loki-scenario/loki-scalable-values.yml --create-namespace

## Adding Grafana Loki Datasource To Grafana
Instead of using the Grafana UI, you can programmatically add a Loki datasource by modifying the Grafana Helm chart. I achieved this by defining the Loki datasource within the `datasources.datasources.yaml` section of the Helm chart's configuration. This allows for automated provisioning of the Loki datasource, ensuring it is consistently deployed with the Grafana instance, avoiding manual intervention. The YAML section includes key configurations such as the datasource name, URL, access method, and authentication, which can be adjusted to suit your environment.

    helm install grafana -n grafana grafana/grafana -f loki-scenario/loki-datasource-values.yml --create-namespace

## Collecting Logs Using Grafana Agent Kubernetes Operator
We can now collect logs from all Kubernetes pods using a log collector, such as the Grafana Agent. To start, we will install the Grafana Agent Kubernetes Operator in our cluster. Once deployed, we'll configure three critical resources: `GrafanaAgent`, `LogsInstance`, and `PodLogs`. These resources enable the Grafana Agent to gather logs from pods in specified namespaces. The `namespaceSelector` field in the `PodLogs` resource defines the namespaces from which logs should be collected. For example, to demonstrate how labels can be added to logs, I configured the `pipelineStages` section of the `PodLogs` resource to append the `http_status_code` and `http_method` labels to all logs from pods in the Nginx namespace. This approach ensures that logs are enriched with useful metadata, aiding in better filtering and analysis.

    helm install collector -n grafana-agent grafana/grafana-agent-operator --create-namespace
    kubectl apply -f grafana-agent-resources/GrafanaAgent.yml
    kubectl apply -f grafana-agent-resources/LogInstance.yml
    kubectl apply -f grafana-agent-resources/PodLogs.yml

## From Agent to Alloy
We are now transitioning from using Grafana Agent to Grafana Alloy for log collection. As part of this migration, I first uninstalled the Grafana Agent Helm chart and cleaned up its associated resources. Next, we will install Grafana Alloy in our Kubernetes cluster. The first step involves applying the `Alloy ConfigMap`, which contains the configuration that directs Alloy to collect logs from all Kubernetes pods and forward them to our `Loki instance`. This configuration specifies key parameters such as log collection endpoints, filtering rules, and the Loki API. After the ConfigMap is applied, we deploy Grafana Alloy using custom settings defined in the `alloy-logs-values.yml` file, which tailors the installation to our needs

    helm uninstall collector -n grafana-agent
    kubectl delete -f grafana-agent-resources/GrafanaAgent.yml
    kubectl delete -f grafana-agent-resources/LogInstance.yml
    kubectl delete -f grafana-agent-resources/PodLogs.yml
    kubectl create ns alloy-logs
    kubectl apply -f grafana-alloy-resources/alloy-logs-configMap.yml -n alloy-logs
    helm install alloy-logs grafana/alloy -n alloy-logs -f alloy-values.yml
    
