import json

from pydantic import BaseModel


class DataSignUpResponseModel(BaseModel):
    userId: int # Optional[int] # int | None
    distanceUnits: str
    currency: str

class SignUpResponseModel(BaseModel):
    status: str
    data: DataSignUpResponseModel
#
# str = ''
# str_2 = ""
# str_3 = """
# kjflkjlksjelkd
# jkrsenfklmklrf
# nfrjniofr
# jrhvik"""



if __name__ == "__main__":
    response_json: str = """{
  "status": "ok",
  "data": {
    "userId": 1,
    "distanceUnits": "km",
    "currency": "usd"
  }
}"""
    response_dict = json.loads(response_json)
    SignUpResponseModel(**response_dict)
