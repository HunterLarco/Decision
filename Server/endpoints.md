#Endpoints

* `POST` /decision ~ Saves a new decision to the database
  * title ~ title of the decision (string)
  * options ~ array of options (strings)
  * expiration ~ seconds to expiration of voting (int)
  * data ~ any additional data you wish to store with this decision

* `GET` /decision/**id** ~ Returns a JSON response containing the decision's data

* `POST` /decision/**id**/votes/**index** ~ Votes for the option of the given index

* `GET` /decision/**id**/votes/**index** ~ Returns the votes for the given index