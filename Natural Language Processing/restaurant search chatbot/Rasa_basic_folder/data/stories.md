## greet
* greet
    - utter_greet

## happy
* thankyou
    - utter_welcome
    
## deny
* deny
    - utter_deny

## goodbye
* goodbye
    - utter_goodbye


## Generated Story 8493847009816211521
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_get_budget
    - slot{"budget": "300-700"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8493847009816211521-1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_get_budget
    - slot{"budget": "300-700"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8493847009816211521-2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "1"}
    - slot{"option": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_get_budget
    - slot{"budget": "300-700"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8493847009816211521-3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "1"}
    - slot{"option": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getoption{"option": "2"}
    - slot{"option": "2"}
    - action_get_budget
    - slot{"budget": "2"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8493847009816211521-4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "1"}
    - slot{"option": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getoption{"option": "2"}
    - slot{"option": "2"}
    - action_get_budget
    - slot{"budget": "2"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8493847009816211521-5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "1"}
    - slot{"option": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getoption{"option": "2"}
    - slot{"option": "2"}
    - action_get_budget
    - slot{"budget": "2"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -6678318779934039141
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_city
    - slot{"location": null}
    - slot{"location_type": false}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_city
    - slot{"location": "allahabad"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "1"}
    - slot{"option": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_get_budget
    - slot{"budget": ">700"}
    - slot{"price": [700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8294684996560132963
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_city
    - slot{"location": null}
    - slot{"location_type": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_get_budget
    - slot{"budget": "<300"}
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"noresults": true}
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted
    
## Generated Story 7849410713572287568
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"budget": "max 500"}
    - slot{"budget": "max 500"}
    - action_get_budget
    - slot{"budget": "max 500"}
    - slot{"price": [0, 500]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted



## Generated Story 7759759455419804
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"budget": "min 600"}
    - slot{"budget": "min 600"}
    - action_get_budget
    - slot{"budget": "min 600"}
    - slot{"price": [600]}
    - action_restaurant
    - slot{"noresults": true}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1483145256352040305
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "chennai", "budget": "mid"}
    - slot{"budget": "mid"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - action_get_budget
    - slot{"budget": "mid"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 5130841017462640654
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location": "bangalore"}
    - slot{"location_type": true}
    - utter_ask_price
* getoption{"option": "2"}
    - slot{"option": "2"}
    - action_get_budget
    - slot{"budget": "2"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted
    
## Generated Story 5349793593531464529
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "6"}
    - slot{"option": "6"}
    - action_get_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* getoption{"option": "3"}
    - slot{"option": "3"}
    - action_get_budget
    - slot{"budget": "3"}
    - slot{"price": [700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 5349793593531464529
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getoption{"option": "6"}
    - slot{"option": "6"}
    - action_get_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* getoption{"option": "3"}
    - slot{"option": "3"}
    - action_get_budget
    - slot{"budget": "3"}
    - slot{"price": [700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* send_mail{"email": "punitha.girish@gmail.com"}
    - slot{"email": "punitha.girish@gmail.com"}
    - action_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted    
    
## Generated Story 2345284121638789772
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_get_budget
    - slot{"budget": "<300"}
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail
* send_mail{"email": "jddkjmd@kdl.co.in"}
    - slot{"email": "jddkjmd@kdl.co.in"}
    - action_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted
    
## Generated Story 1391576416241737118
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_city
    - slot{"location": "chandigarh"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_get_budget
    - slot{"budget": "<300"}
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": true}
    - utter_noresults
* deny
    - utter_goodbye
    
## Generated Story 1391576416241737114
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	 - action_city
    - slot{"location_type": false}
    - utter_nontier
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted
    
## Generated Story -1555280997735521460
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bengaluru", "budget": "range 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - slot{"budget": "range 300 to 700"}
    - action_city
    - slot{"location_type": true}
    - action_get_budget
    - slot{"budget": "range 300 to 700"}
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail
* send_mail{"email": "jddkjmd@kdl.co.in"}
    - slot{"email": "jddkjmd@kdl.co.in"}
    - action_send_mail
* deny
    - utter_deny
    - action_reset
    - reset_slots
    - action_restarted