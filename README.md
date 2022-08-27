## API gateway access to Lambda in public subnet of VPC without nat gateway

- `sam package --region us-east-1 --template-file template.yaml --output-template-file packaged.yaml --s3-bucket <some-bucket>`

- `aws cloudformation update-stack --stack-name public-subnet-test --template-body file://./packaged.yaml --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM`

- Get the API endpoint from api gateway. Use stage /dev. CURL endpoint 
