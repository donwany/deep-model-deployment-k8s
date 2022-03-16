### Using Curl to test REST API
```shell
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'

curl -X POST -F image=@/Users/tsiameh/Desktop/1623427094850.jpg \
'http://localhost:5001/predict'

```
### Consuming REST API Programmatically
```python
# import the necessary packages
import requests

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5001/predict"
IMAGE_PATH = "/Users/tsiameh/Desktop/1623427094850.jpg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

# ensure the request was successful
if r["success"]:
    # loop over the predictions and display them
    for (i, result) in enumerate(r["predictions"]):
        print("{}. {}: {:.4f}".format(i + 1, result["label"],
            result["probability"]))

# otherwise, the request failed
else:
    print("Request failed")

```