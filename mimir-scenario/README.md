## Deploying Grafana Mimir on Kubernetes Cluster Using Its Helm Chart
I created a custom Helm values file named `mimir-distributed-values.yml`, where I configured Mimir to use MinIO as the backend storage for storing metrics and metadata. Additionally, I set up an Alertmanager FallbackConfig, which serves as a default Alertmanager configuration for any tenant that does not have a custom configuration defined. This ensures that alerts are still routed and managed appropriately even when tenant-specific configurations are absent, providing a robust fallback mechanism within the multi-tenant Mimir setup. You can further modify specific sections of this customized Helm values file (`mimir-distributed-values.yml`) to suit the unique requirements of your environmen

    helm install mimir -n mimir grafana/mimir-distributed -f mimir-scenario/mimir-distributed-values.yml --create-namespace

## Adding Grafana Mimir Datasource To Grafana
Now it's time to add the Mimir datasource to Grafana to visualize metrics. In the `mimir-datasources-values.yml` file, you'll see that I've configured three different datasources. One of them is for the Alertmanager, while the other two are Mimir datasources, both defined with the type `Prometheus`, since Mimir itself does not provide a default datasource. Mimir offers a powerful feature called `multi-tenancy`, which allows you to isolate different categories of metrics. In this example, I'm storing metrics from Linux nodes under the `nodes tenant` and Kubernetes pod metrics under the `pods tenant`. To achieve this, I've added the HTTP header `X-Scope-OrgID` to both Mimir datasources, specifying the tenant name for each. By adding this header with any desired tenant name, you can segregate and view the metrics within their respective datasources, ensuring clear isolation between different metric sets.

    helm install grafana -n grafana grafana/grafana -f mimir-scenario/mimir-datasources-values.yml --create-namespace

## Collecting Metrics Using Grafana Agent Kubernetes Operator Mode and Static Mode
We're going to use grafana agent to collect metrics in two different modes to show how the different modes of grafana agent work. the first mode is using grafana agent `kubernetes operator` to collect metrics of kubernetes pods and the second mode is grafana agent `statis mode` which i'm going to use it for exporting the metrics of my linux node . in the previous step we created two different mimir datasource that each of them is using a tenant name . so now for kubernetes pods, i'm going to use `X-Scope-OrgID: pods` as the header in the configuration of `grafana-agent-resources/MetricInstance.yml` (kubernetes operator mode) to send pods metrics to `pods tenant` . and using `X-Scope-OrgID: nodes` as the header in the configuration of `grafana-agent-resources/grafana-agent.yml` (static mode) to send nodes metrics to `nodes tenant`.

    helm install collector -n grafana-agent grafana/grafana-agent-operator --create-namespace
    kubectl apply -f grafana-agent-resources/GrafanaAgent.yml
    kubectl apply -f grafana-agent-resources/MetricInstance.yml
    kubectl apply -f grafana-agent-resources/cadvisor-ServiceMonitor.yml
    kubectl apply -f grafana-agent-resources/kubelet-ServiceMonitor.yml
