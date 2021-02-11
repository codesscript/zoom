const base64JS = require('js-base64');
const hmacSha256 = require('crypto-js/hmac-sha256');
const encBase64 = require('crypto-js/enc-base64');

function generateSignature(data) {
    let signature = '';
    // Prevent time sync issue between client signature generation and zoom
    const ts = new Date().getTime() - 30000;
    const msg = base64JS.Base64.encode(data.apiKey + data.meetingNumber + ts + data.role);
    const hash = hmacSha256(msg, data.apiSecret);
    signature = base64JS.Base64.encodeURI(`${data.apiKey}.${data.meetingNumber}.${ts}.${data.role}.${encBase64.stringify(hash)}`);
    return signature;
}

const data = {apiKey: "34n5fY-dQAqLjcXZjosfyw" ,
apiSecret: "B7p3dhFTYrLXdwTfJipACMJxhNBYItDm0vxJ",
meetingNumber: 81455534152,
role: 0}

console.log(generateSignature(data));
var s=generateSignature(data);

