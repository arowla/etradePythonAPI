# ETrade API OAuth Dance

From the ETrade API docs, enhanced with URLs and query params:

With the E*TRADE Developer Platform, the process works like this:

* The application uses its own credentials to acquire a temporary request token from E*TRADE by calling the Get Request Token API.
  * https://etws.etrade.com/oauth/request_token
* Using the Authorize Application API, the application redirects the user, along with the request token, to E*TRADE. There the user logs in to E*TRADE and grants the application limited access to the user's account. E*TRADE generates a verification code, which is passed to the application (manually by the user, or automatically via a callback).
* The application uses the verification code to acquire an access token that grants temporary access to that user's account. This is done with the Get Access Token API.
* The access token is included with all requests to the E*TRADE API, identifying the user and authorizing the application.



By default, the token expires at midnight US Eastern time. At that time, the token may be renewed with the Renew Access Token API. When the application terminates or is finished with the token, we recommend that you revoke the token with the Revoke Access Token API.
