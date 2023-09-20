from e_comm.app import app

from e_comm.admin.url import admin_routes
from e_comm.addresses.url import address_routes
from e_comm.carts.url import cart_routes
from e_comm.coupons.url import coupon_routes
from e_comm.orders.url import order_routes
from e_comm.payments.url import payment_routes
from e_comm.product.url import product_routes
from e_comm.review.url import review_routes


admin_routes(app)
address_routes(app)
cart_routes(app)
coupon_routes(app)
order_routes(app)
payment_routes(app)
product_routes(app)
review_routes(app)