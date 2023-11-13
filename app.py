import pandas as pd
from google.cloud import storage
from flask import Flask

app = Flask(__name__)



@app.route('/save_csv')
def save_csv():
    data = {
        'column1': [1, 2, 3],
        'column2': ['a', 'b', 'c']
    }
    df = pd.DataFrame(data)

    # Convert DataFrame to CSV
    csv_path = 'my_data.csv'
    df.to_csv(csv_path, index=False)

    info={
    "type": "service_account",
    "project_id": "store-data-361116",
    "private_key_id": "730985954320975102d1144eb1ee5ec032702fa6",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvUoGkAWF+Wdjd\nzYJRtsNgWs3p9r0+Eih28sT3mZ5UJNPNa572U3i3eA6MDWMkCcgRxOms45dS3Bxb\nhXSBrUwyP4K7JaLQInAA2fBNh5Svw58fxChKEnKDvJRj9/KygJ/zvNEf3xTN125l\nuvsjm1htWT7IjJQ4dOgWHtE3DYTlCBOg3C52GskvoPqaWPpRvBUOdqosya5t3V0i\nt+tWvcU/oai8/m0srcXAfS+RB6FONf1hPCvwayt7fbNV0GP7TQ+KEnuFwp+IZIl3\n9IpQPc/8l2uXAdNBojQ243mlR412aSOlitkgE6uZ/cg2uutTOIlNHNC7yL2jHh+a\n8capuQV9AgMBAAECggEABkvVUzVn0dYPsKgpT95wpfSfiaaztUzeePvEdkDlJk/x\nRE1jDCUYxCaoB8BmU6cUm+DBZJUC0aC31aiVXnUsXpnty7ibtX5QcpNhFXkIQ7H9\nNF1Cy3rd88cGtuVdaQAvXl06TxBKSrnRIY76vGoJ3a7IugKPGHedqx0IYJdYHbJ3\nwEeGa4ZeK7IHL/P8ZGaKn+YmrO0XiZGQhOmac4+CVwdWOGer+PGATLYaXCiIEH1b\n2XGfeD2ZMPoyM/oe8FnBLtZ2Myj+QdymSpv08ssUZPT66W/S2x40lx/zpOH0trH7\nu1AUHofoEkEP+rW8eeF9u2dKuH75z5L1S9NOs7J68QKBgQD2SVfpisT5xS/N0ZcX\n+VdR3pmOTIUBm8Jcs/KU5a2vGv3Okg5qSTKi9CvOisRLjpXkJTCgDSljlYTxUQS1\nXCweTWpBPipY4Syle4eA32gl+NmAe9jDkzcIdWkq+sz8dL0LcPKKtpxrpzwFy589\nlrjN87RCskgZvwPmyCXF+Jv+7QKBgQC2PKpqtibF4eeX3uHhJJ35D9rxibG6+Hjh\nCW3NKi0TVpLWvgsCO4Y9hf/ZD3Kih206zXcHrJMH1oU7tsEDfiQjalMu7Vb8jRG2\nsPnMKrOwcjra+MgPiJidP7XPyQX2lzNwoXVaZFnOp9OnaepXFDd6WjHEM1uSDmvL\nsingqJK+0QKBgQCNI2ja8GiDTopfo6230m9E/pD3KEjMrCtNHt50j87h21D58V+L\nb1kyY0U7fvCQ8Cxb6ygbgI9of0YJWMme+SxbTTgIHYz9FEWWq9zycJTptdtHMzH8\nmj/efBKBy+pu/qNbjCWicpXfZ54RICiojdhoRjHWSv7gqkOdHLPw6NDU3QKBgBAO\nPD12mufoRU0+F8yMO1bMLNAG/5+ncI7zE7d1tc70W6+LwtCJigQ1oBrxn3nuUJNT\nst78N2ADaG2gZlT2chykq3uA8Z8ClsLvyLJSOM6c4c6VCJtFv5xrFoud/GaDX8bW\nks5J9Red9anUTQ8q+tBOzf+pPrIZjym9Iq9mardhAoGALvVU/9oCyXdqEjPUxuFI\nCNnlwXswq4AY80SCy+zwN/QYZpVjamF3nFONEjh8cHfpZwcgbYyo00Z25yrRiSNh\n/fsqZmPHtZvhYFwC7F4habF7QKbZ874piA81BxkcZ3mab14nP1ablBUOP+BF9TGO\nBMruDn1zoiDbkLqxdCu9/SY=\n-----END PRIVATE KEY-----\n",
    "client_email": "coder-410@store-data-361116.iam.gserviceaccount.com",
    "client_id": "104236093715382732737",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/coder-410%40store-data-361116.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
    }


    # Initialize GCS client
    client = storage.Client.from_service_account_info(info)

    # Define your bucket name
    bucket_name = 'hol_test'

    # Get your bucket
    bucket = client.get_bucket(bucket_name)

    # Create a blob object
    blob = bucket.blob(csv_path)

    # Upload the CSV file to GCS
    blob.upload_from_filename(csv_path)

    print(f"File {csv_path} uploaded to {bucket_name}.")


from flask import Flask



@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

