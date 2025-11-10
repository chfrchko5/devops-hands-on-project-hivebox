[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---
### installation
- create the kubernetes cluster using terraform (from inside the terraform directory)
  "terraform apply"
- install argocd if not present
  "https://argo-cd.readthedocs.io/en/stable/getting_started/"
- apply argocd manifests via kubectl to automatically deploy all resources (from inside kubernetes-argocd directory)
"kubectl apply -f argocd-manifests"
- due to no dns, append domain in /etc/hosts
"echo hivebox.local >> /etc/hosts"
- forward the port for nginx ingress due to not having any loadbalancers
"kubectl -n ingress-nginx port-forward svc/ingress-nginx-controller 5050:80"
- access the page in browser via https://hivebox.local:5050/(endpoint)


## Implementation

** ADD YOUR IMPLEMENTATION DOCUMENTATION HERE **
Nov 2, 2025
added argocd manifests for auto deployment of the project
using a helm chart ‘kube-prometheus-stack’ alongside service monitors for valkey and app to set up metric tracking in grafana
added a grafana dashboard for hivebox app
added a grafana dashboard for valkey

Nov 1, 2025
organized the files for nginx-ingress to be more clean

Oct 31, 2025
implemented readinessProbe in the kubernetes app yaml file to check if readyz endpoint returns 200 OK to set container status to ready
implemented terraform for the deployment of the kubernetes cluster with kind
implemented venom declarative simple test for the endpoints, ran locally

Oct 30, 2025
fixed readyz endpoint
created a helm chart for the application
added a simple kustomization yaml for valkey that uses the same base file as before
implemented initial code for readinessProbe for app pod in k8s

Oct 28, 2025
added a readyz endpoint for later use in kubernetes that checks if api urls are accessible
extended default prometheus metrics by a simple caching hit/miss collector

Oct 27, 2025
added and fixed valkey caching in python code
fixed github workflow not working after implementing valkey

Oct 25, 2025
fixed nginx ingress on kubernetes cluster (port-forward the ingress controller in order to access the endpoints of the app using a local domain via /etc/hosts)

Oct 23, 2025
added a checkov scan workflow file to scan kubernetes manifest files for vulnerabilities/errors (instead of initial terrascan setup)

Oct 22, 2025
fixed auto versioning in python when deployed in docker
added a simple k8s yaml file to deploy in a cluster

Oct 20, 2025
implemented a prometheus scraped /metrics endpoint
improved pytesting

Oct 18, 2025
added automatic docker push in github workflow, uses the same version for the image as the github repo and the python api application for consistency
added a github workflow for repo code security check (ossf)
implemented additional information display based on the calculation of the temperature

Oct 13, 2025
implemented version sync for the python app, uses git tag as its’ source
implemented auto tag increment in github actions workflow file
implemented creation of the docker image

Oct 12, 2025
implemented /temperature endpoint that takes the temperature value from three senseBox URL’s and calculates the average between them
implemented 2 sample unit tests for /version and /temperature endpoints

Oct 10, 2025
implemented /version endpoint that displays current version of the app

Oct 9, 2025
initialized the python api project with v0.0.1 version
created a simple dockerfile to print app’s version in the container
