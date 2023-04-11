# IP App

This application saves the ip on mysql and fetch from table on list page

## Run

Docker
```bash
docker-compose build
docker-compose up
```

Without Docker Run
```bash
pip install -r requirements.txt
./entrypoint.sh
```

Debugging
```bash
pip install -r requirements.txt
./entrypoint.sh debug
```

### ECR Image Push
When code is pushed to master or PR is merged to master, github workflow runs and push the image to ECR

https://github.com/harisahmed001/ip-app/blob/master/.github/workflows/build_push.yml


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.