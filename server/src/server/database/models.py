import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(default='')
    email = peewee.CharField(default='')
    password = peewee.CharField(default='')
    role = peewee.CharField(default='')
    created_at = peewee.CharField(default='')


class Address(BaseModel):
    user_id = peewee.ForeignKeyField(User, related_name='user_addresses', default=1)
    street = peewee.CharField(default='')
    city = peewee.CharField(default='')
    state = peewee.CharField(default='')
    zip_code = peewee.CharField(default='')
    created_at = peewee.CharField(default='')


class Product(BaseModel):
    name = peewee.CharField(default='')
    description = peewee.CharField(default='')
    price = peewee.FloatField(default=0)
    stock_quantity = peewee.IntegerField(default=0)
    created_at = peewee.CharField(default='')


class Category(BaseModel):
    name = peewee.CharField(default='')
    description = peewee.CharField(default='')
    created_at = peewee.CharField(default='')


class ProductCategory(BaseModel):
    product_id = peewee.ForeignKeyField(Product, related_name='product_categories', default=1)
    category_id = peewee.ForeignKeyField(Category, related_name='category_products', default=1)
    created_at = peewee.CharField(default='')


class Order(BaseModel):
    user_id = peewee.ForeignKeyField(User, related_name='user_orders', default=1)
    address_id = peewee.ForeignKeyField(Address, related_name='address_orders', default=1)
    order_date = peewee.CharField(default='')
    total_amount = peewee.FloatField(default=0)
    status = peewee.CharField(default='')
    created_at = peewee.CharField(default='')


class OrderItem(BaseModel):
    order_id = peewee.ForeignKeyField(Order, related_name='order_items', default=1)
    product_id = peewee.ForeignKeyField(Product, related_name='product_order_items', default=1)
    quantity = peewee.IntegerField(default=1)
    subtotal = peewee.FloatField(default=0)
    created_at = peewee.CharField(default='')


class Review(BaseModel):
    product_id = peewee.ForeignKeyField(Product, related_name='product_reviews', default=1)
    user_id = peewee.ForeignKeyField(User, related_name='user_reviews', default=1)
    rating = peewee.IntegerField(default=1)
    comment = peewee.CharField(default='')
    created_at = peewee.CharField(default='')


class Wishlist(BaseModel):
    user_id = peewee.ForeignKeyField(User, related_name='user_wishlist', default=1)
    product_id = peewee.ForeignKeyField(Product, related_name='product_wishlist', default=1)
    created_at = peewee.CharField(default='')  # Changed to CharField


db.connect()
db.create_tables([
    User,
    Address,
    Product,
    Category,
    ProductCategory,
    Order,
    OrderItem,
    Review,
    Wishlist
])
