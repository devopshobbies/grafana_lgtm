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

## Migrate from Grafana Agent Static to Grafana Alloy
In the previous step, we used Grafana Agent in two different modes. Now, it's time to migrate from Grafana Agent to Alloy as the collector. First, let's convert the static mode setup to Alloy. To do this, we need to install Alloy on our environment, such as on the Linux node, and stop the running Grafana Agent service using `systemctl`. Then, we use the `convert` command provided by Alloy to convert our Grafana Agent configuration into `Alloy's configuration format`. Finally, we enable and start the Alloy service on our Linux node using systemctl, ensuring Alloy is now actively collecting metrics.

    sudo mkdir -p /etc/apt/keyrings/
    wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
    echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
    sudo apt-get update && sudo apt-get install alloy
    systemctl stop grafana-agent && systemctl disable grafana-agent
    alloy convert --source-format=static --output=/etc/alloy/config.alloy grafana-agent-resources/grafana-agent.yml
    systemctl enable --now alloy

## Migrate from Grafana Agent Operator to Grafana Alloy
Now, let's migrate from Grafana Agent Kubernetes Operator mode to Grafana Alloy. It's important to note that the monitor types (`PodMonitor, ServiceMonitor, Probe, and PodLogs`) are all natively supported by Alloy, while the components of the Grafana Agent Operator that deploy `GrafanaAgent, MetricsInstance, and LogsInstance` CRDs are deprecated. To gather Kubernetes pod metrics using Grafana Alloy, I deploy `ServiceMonitor` resources and configure an Alloy ConfigMap to serve as the Alloy configuration. This configuration is designed to discover ServiceMonitor and PodMonitor resources. In this example, I use the `X-Scope-OrgID = pods` header in the configuration file `grafana-alloy-resources/alloy-metrics-configMap.yml` to route pod metrics to the `pods tenant` in Mimir

    helm uninstall collector -n grafana-agent
    kubectl delete -f grafana-agent-resources/GrafanaAgent.yml
    kubectl create ns alloy-metrics
    kubectl apply -f mimir-scenario/cadvisor-ServiceMonitor.yml && kubectl apply -f mimir-scenario/kubelet-ServiceMonitor.yml
    kubectl apply -f grafana-alloy-resources/alloy-metrics-configMap.yml -n alloy-metrics
    helm install alloy-metrics grafana/alloy -n alloy-metrics -f mimir-scenario/alloy-metrics-values.yml
