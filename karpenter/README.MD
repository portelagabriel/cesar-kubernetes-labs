### HELM INSTALL COMMANDS
helm registry logout public.ecr.aws
helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter --version "1.4.0" --namespace "karpenter" --create-namespace -f karpenter.values.yaml