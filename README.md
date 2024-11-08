# grafana_lgtm
![Grafana LGTM Image](Grafana_lgtm_logo.png)

This repository contains various resources related to Loki, Grafana, Tempo, and Mimir. These tools are key components in modern observability and monitoring stacks, providing capabilities for logging, metrics, and tracing in cloud-native environments.

## Tools we are going to learn together
* [Grafana Loki](https://grafana.com/oss/loki/) - Log Aggregation System
* [Grafana](https://grafana.com/oss/grafana/) - Data Visualization
* [Grafana Tempo](https://grafana.com/oss/tempo/) - Distributed Tracing Backend
* [Grafana Mimir](https://grafana.com/oss/mimir/) - TSDB for Long-term Storage for Prometheus
* [Grafana Agent](https://grafana.com/docs/agent/latest/) -  OpenTelemetry Collector Distribution
* [Grafana Alloy](https://grafana.com/docs/alloy/latest/) -  OpenTelemetry Collector Distribution | As a replacement for Grafana Agent

   
## Scenarios and Setup Guide
  - Grafana Loki Scenario
    - [Deploying Grafana Loki on Kubernetes Cluster Using Its Helm Chart](https://github.com/devopshobbies/grafana_lgtm/tree/main/loki-scenario#deploying-grafana-loki-on-kubernetes-cluster-using-its-helm-chart)
    - [Adding Grafana Loki Datasource To Grafana](https://github.com/devopshobbies/grafana_lgtm/tree/main/loki-scenario#adding-grafana-loki-datasource-to-grafana)
    - [Collecting Logs Using Grafana Agent Kubernetes Operator](https://github.com/devopshobbies/grafana_lgtm/tree/main/loki-scenario#collecting-logs-using-grafana-agent-kubernetes-operator)
    - [From Agent to Alloy](https://github.com/devopshobbies/grafana_lgtm/tree/main/loki-scenario#from-agent-to-alloy)
  - Grafana Mimir Scenario
    - [Deploying Grafana Mimir on Kubernetes Cluster Using Its Helm Chart](https://github.com/devopshobbies/grafana_lgtm/tree/main/mimir-scenario#deploying-grafana-mimir-on-kubernetes-cluster-using-its-helm-chart)
    - [Adding Grafana Mimir Datasource To Grafana](https://github.com/devopshobbies/grafana_lgtm/tree/main/mimir-scenario#adding-grafana-mimir-datasource-to-grafana)
    - [Collecting Metrics Using Grafana Agent Kubernetes Operator Mode and Static Mode](https://github.com/devopshobbies/grafana_lgtm/tree/main/mimir-scenario#collecting-metrics-using-grafana-agent-kubernetes-operator-mode-and-static-mode)
    - [Migrate from Grafana Agent Static to Grafana Alloy](https://github.com/devopshobbies/grafana_lgtm/tree/main/mimir-scenario#migrate-from-grafana-agent-static-to-grafana-alloy)
    - [Migrate from Grafana Agent Operator to Grafana Alloy](https://github.com/devopshobbies/grafana_lgtm/tree/main/mimir-scenario#migrate-from-grafana-agent-operator-to-grafana-alloy)
  - Grafana Tempo Scenario
    - WILL BE UPDATED SOON

## About the Author
  - **Mohammad Madanipour**
    - [GitHub](https://github.com/mohammadll)
    - [Linkedin](https://linkedin.com/in/mohammad-madanipour)


## LGTM-Stack Course on DevOps Hobbies YouTube Channel
 - Grafana loki + Grafana + Grafana Agent
    - [Getting Started with Grafana Loki](https://www.youtube.com/watch?v=YG1UiiSygyA&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=3)
    - [Enhancing Application Logs with Grafana Agent Pipeline Stages](https://www.youtube.com/watch?v=7NZd5DyFFp0&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=2)
    - [Working with LogQL and Setting up Alerting](https://www.youtube.com/watch?v=boS5enCeszU&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=1)
 - Grafana Mimir + Grafana + Grafana Agent + Grafana Alloy
   - [Getting Started with Grafana Mimir](https://www.youtube.com/watch?v=MS_ZlnDPj3E&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=4)
   - [Implementing Grafana Agent to Write Metrics in Mimir with Multi-Tenant Architecture](https://www.youtube.com/watch?v=avmhMu0Y9N0&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=5)
   - [Migrating from Grafana Agent to Grafana Alloy](https://www.youtube.com/watch?v=wph1taa1viE&list=PLYrn63eEqAzZL2TaS0pXXw-_DEl3SsAF_&index=6)
 - Grafana Tempo + Grafana + Grafana Alloy + OpenTelemetry
   - WILL BE UPDATED SOON
