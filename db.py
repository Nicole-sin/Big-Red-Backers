from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Review', backref='user')

class DiningHall(db.Model):
    __tablename__ = 'dining_halls'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    food_items = db.relationship('FoodItem', backref='dining_hall')

class FoodItem(db.Model):
    __tablename__ = 'food_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255))
    dining_hall_id = db.Column(db.Integer, db.ForeignKey('dining_halls.id'), nullable=False)
    reviews = db.relationship('Review', backref='food', lazy=True, foreign_keys='Review.food_id')
    recommended_in_reviews = db.relationship('ReviewRecommendedFood', backref='recommended_item')

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text)
    food_id = db.Column(db.Integer, db.ForeignKey('food_items.id'), nullable=False)
    dining_hall_id = db.Column(db.Integer, db.ForeignKey('dining_halls.id'), nullable=False)
    recommended = db.relationship('ReviewRecommendedFood', backref='review')

class ReviewRecommendedFood(db.Model):
    __tablename__ = 'review_recommended_food'
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id'), nullable=False)
