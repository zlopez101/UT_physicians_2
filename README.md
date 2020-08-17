# Call Center

When COVID-19 hit, our practice was enlisted to start administering COVID-19 diagnostic test to the Houston Area. Given the urgency and complete 180 from standard day-to-day operations, our insurance was forced into an uncomfortable position of managing the roll out of the new venture as quick as possible. 

I recently started playing around with the Flask framework and found it really intuitive for building websites. This call center is my attempt to build a fully fledged call center and webite that would allow patients to book appointments, fax in documentation, and connect with employees that could help them answer questions. 

DB considerations:
1. get rid of AppointmentSlots - too many things to load
2. have the appointment carry the referring provider and referral number - patients can have multiple appointment with different clinics from different providers. Creates scalability issues. 
3. Since no more AppointmentSlot, we will have to create all appointments to be preloaded.
4. Create two appointment for each time slot at each location. Will have green, yellow, red for 2, 1, and no appointments left. 
  
Twilio Considerations:
  1. Need to upgrade account to implement fax resource
  2. click to call functionality
  3. appointment reminders

Google Maps locator
https://developers.google.com/maps/solutions/store-locator/clothing-store-locator
