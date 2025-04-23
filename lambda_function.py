import json
import random


def lambda_handler(event, context):
    num = random.randint(1, 5)
    if num == 5:
        return {"statusCode": 500, "body": json.dumps("Erro!")}
    else:
        return {"statusCode": 200, "body": json.dumps("Sucesso!")}