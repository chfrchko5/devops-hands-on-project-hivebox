#!/bin/bash

CHART_VERSION="79.1.0"
APP_VERSION="v0.86.1"

helm template metrics kube-prometheus-stack \
--repo https://prometheus-community.github.io/helm-charts \
--version ${CHART_VERSION} \
--namespace metrics \
> metrics.${APP_VERSION}.yaml