import os
import requests
import json
import socket
import uvicorn
from fastapi import FastAPI

AWS_URL = "http://169.254.169.254/latest/meta-data"

api = FastAPI()

@api.get("/")
async def root():
    instance_id = requests.get(f"{AWS_URL}/instance-id")
    req_pri_ip = requests.get(f"{AWS_URL}/local-ipv4")
    req_pub_ip = requests.get(f"{AWS_URL}/public-ipv4")
    hostname = socket.gethostname()
    pri_ip = req_pri_ip.text
    pub_ip = req_pub_ip.text
    return {
            "hostname": hostname,
            "priviate_ip": pri_ip,
            "public_ip": pub_ip
            }

def start():
    """ Launch with poetry run start """
    uvicorn.run("whoami.api:api", host="0.0.0.0", port=8000, reload=True)
