
# Challenge Solution


## Problem

Import the physicians from the noteworth_challenge_api service and import them into a database.


## Solution
Uses Django to solve the challenge. It is provided an endpoint that on demand, reads the providers API, manage the authentication and imports the physician data on a database. The service has some tolerance to errors in the connection or in the API.

The service is:
/api/importPhysicians/, accessible by POST

The database engine used is SQLite.


## Improvements
The following changes can be done to improve this solution:
- Add more security, storing the secret_key and other important configuration variables in a json file or environment variables.
- Complete the authentication.
- Change the basic SQLite database for a production database (i.e. Postgres).
- The Vagrant configuration needs more work to be ready at the first initialization without additional steps.
- Fix some format errors during the data importation that may happen sometimes.
- Add more tests.
- Replace prints by logs in console for debugging purpose.
