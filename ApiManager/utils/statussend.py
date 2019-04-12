import requests

url = "http://10.101.12.4:10099/v2/device/event"

querystring = {"token":"0d9962ff210f4e56588c21e90d8b7be70c8cca2b5615c29441be386b6d943803"}

payload = "{\r\n    \"deviceType\": \"CameraPeopleCountingSystem\", \r\n    \"deviceID\": \"HCZ-00108\", \r\n    \"timestamp\": 1554793017, \r\n    \"message\": \"Test\", \r\n    \"data\": {\r\n    \t\"image_data\": {\"blob\":\"iVBORw0KGgoAAAANSUhEUgAAABQAAAAJCAYAAAAywQxIAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\\r\\njwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfZAwwNMCOBavb9AAAADXRFWHRBdXRo\\r\\nb3IAQ29yYmlzYMk7zgAAACB0RVh0Q3JlYXRpb25UaW1lADIwMDg6MDI6MTggMDU6MDc6MzFrfxj\\/\\r\\nAAAAIXRFWHRDcmVhdGlvbiBUaW1lADIwMDg6MDI6MTggMDU6MDc6MzHj8Hs5AAAB40lEQVQoUx2S\\r\\ny5LSQBSGv+4kJCRcJogiNWWpi5kqn8LH8MXVcTFTgyymQAUCcg3pbv+4yKJz+vzXNuXnL2Gz2sHj\\r\\nd5h8hMhCnmKenwjNXucuEKA\\/hsJifj4QjH75VDOHcYbgt1ib4KMIG5zAZk\\/QGcGgBBdjzldCOdCl\\r\\nHtRbMFouNNvXWtBSov8mF+CUYLsYE+ONyEIHe\\/AlZvgWPr0Xq4ODANZ\\/oJGuPEHbAq0wL18x6wec\\r\\n5PnkRoAnSDxm9EaAuuMvhE4X684NYfJaS\\/KxmEmdAAd9KAtCdBTwAeNPUnIRSEsQCUtWfSU1c8Ll\\r\\nKIJcoIpKEVl+z+G4\\/p+h3f0i9DImd3fk4xK73ohZhIkIe7LXGQpQxH6h3Bw+GyjvIZFUt2fqgyKJ\\r\\nFfCugvMOXyjHYZ9lteD47YcSkMLiHUwVx\\/Ei9VqIUoKzUiLgyb3mXZy7CkRcKMOwWunyWUMt3gqw\\r\\nrgmPz7CV8lgNT6bYOMVeKkK4yJ6sxYXgpKSSg6U+qTbxK3wnV5FNDWmbmeTPZX2xIbk6sQ0wxQdM\\r\\n01FJL1L7V61mGDvCRDmubXq\\/FLhyTUtZ1mtxytCPb2FUEB89nKS22XANbT4q5WZCqLb4zax9eOok\\r\\nI2SynOtVBNkMcpZFalugmkOXfwqA1d8ruWxFAAAAAElFTkSuQmCC\\r\\n\",\"contentType\":\"image\\/png\"},\r\n        \"num_leave\": 22,\r\n        \"num_enter\": 20,\r\n        \"num_stay\": 11\r\n    }\r\n}\r\n"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "cedee6b3-b5aa-47b0-bf30-91dffefad62f"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
