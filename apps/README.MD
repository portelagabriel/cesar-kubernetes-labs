### Multi Arch Build
To build a multi-architecture Docker image that supports ARM processors, follow these steps:

1. Enable buildx (if not already)
   - docker buildx version
   
2. Create and use a new builder (if needed)
   - docker buildx create --name multiarch-builder --use
   - docker buildx inspect --bootstrap

3. Authenticate with Amazon ECR
   - aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

4. Build and Push
   - docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t $REPO:latest \
  --push \
  .

5. Verify the image manifests
   - docker buildx imagetools inspect $REPO:latest
