# Big-Red-Backers

Hi our final project is found on this link:
https://github.com/Nicole-sin/Big-Red-Backers-official


Implementation 
app.py routes 
getAllReviews
postReview
getAllDiningHalls
getReviewsByUser
CreateUser

 Review model 
Id
user
Rating
Message
Food: FoodItem
Recommended: FoodItem []
Dining hall

Dining hall model 
Id
name
topItems: FoodItem []

Food Item Model 
ID
Name
Image
Dining Hall

User model 
Id
Posts


Relationships:
Food Item to Review - One to Many - each food item has multiple reviews but each review belongs to one food.
Nicole
User to Review - One to Many - each user has multiple reviews but each review belongs to one user - Mukund
Dining hall to Food - One to Many - each dining hall has multiple food items but each food item belongs to one dining hall.
Samantha 
