#!/bin/bash

CHART_VERSION="4.13.3"
APP_VERSION="1.13.3"

helm template ingress-nginx ingress-nginx \
--repo https://kubernetes.github.io/ingress-nginx \
--version ${CHART_VERSION} \
--namespace ingress-nginx \
> nginx-ingress.${APP_VERSION}.yaml