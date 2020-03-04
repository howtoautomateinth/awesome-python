# Binary I/O (also called buffered I/O) expects bytes-like objects and produces bytes objects
import io
import requests

r = requests.get("https://www.howtoautomate.in.th/wp-content/uploads/2016/12/logo-b.png")
# get image as bytes
# RAM to process bytes-like object faster performance
with io.BytesIO() as buf:
    buf.write(r.content)
    # The seek method will move the pointer to 0
    buf.seek(0)
