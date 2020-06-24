import flask
from flask import Blueprint

home_route = Blueprint('home_route',__name__)

@home_route.route('/')

def index():
    print('Visiting About Page')
    print('Effects: Giggly, Mouth, Happy, None, Euphoric, Uplifted, Sleepy, Relaxed, Energetic, Talkative, Dry, Focused, Aroused, Hungry, Creative, Tingly')
    print('Flavors: Tea, Minty, Citrus, Ammonia, Menthol, Tar, Peach, Apricot, Woody, Tobacco, Mango, Honey, Vanilla, Nutty, Skunk, Rose, Butter, Pineapple, Grapefruit, Pungent, Blueberry, Cheese, Chestnut, Chemical, Lime, Coffee, None, Violet, Pepper, Berry, Lavender, Blue, Sweet, Grape, Plum, Orange, Sage, Diesel, Lemon, Strawberry, Earthy, Flowery, Spicy/Herbal, Tropical, Mint, Pine, Tree, Apple, Fruit, Pear')
    return f'/predict?effect=wanted&flavor=wanted  :to the end of the url'
