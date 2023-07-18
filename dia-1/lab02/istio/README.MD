## Istio Installation using Helm

First step is to install Istio Operator

- Clone this repository
- cd dia-1/lab02/istio
- helm install -f istio-operator/values.yaml istio-operator istio-operator/

Install IstioD and Istio Ingress Gateway
 - cd istio-components
 - change the subnets Ids in the defaul_install.yaml to your public subnets
 - kubectl apply -f defaul_install.yaml