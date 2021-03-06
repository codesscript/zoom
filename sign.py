import hashlib
import hmac
import base64
import time

def generateSignature(data):
    ts = int(round(time.time() * 1000)) - 30000
    msg = data['apiKey'] + str(data['meetingNumber']) + str(ts) + str(data['role'])
    message = base64.b64encode(bytes(msg, 'utf-8'))
    # message = message.decode("utf-8");
    secret = bytes(data['apiSecret'], 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    hash =  base64.b64encode(hash.digest())
    hash = hash.decode("utf-8")
    tmpString = "%s.%s.%s.%s.%s" % (data['apiKey'], str(data['meetingNumber']), str(ts), str(data['role']), hash)
    signature = base64.b64encode(bytes(tmpString, "utf-8"))
    signature = signature.decode("utf-8")
    return signature.rstrip("=")

if __name__ == '__main__':
    data = {'apiKey': "34n5fY-dQAqLjcXZjosfyw",
                'apiSecret': "B7p3dhFTYrLXdwTfJipACMJxhNBYItDm0vxJ",
                'meetingNumber':  85674955580,
                'role': 1}
sign = (generateSignature(data))
print(sign)
