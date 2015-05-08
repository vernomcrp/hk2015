from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from account import views as account_views
from order import views as order_views
from dish import views as dish_views
from account import account_login, group_manager

router = routers.DefaultRouter()
router.register('accounts', account_views.AccountViewSet)
router.register('users', account_views.UserViewSet)
router.register('orders', order_views.OrderViewSet)
router.register('order_historys', order_views.OrderHistoryViewSet)
router.register('dishs', dish_views.DishViewSet)
router.register('ingredients', dish_views.IngredientViewSet)
router.register('basedishs', dish_views.BaseDishViewSet)
router.register('meats', dish_views.MeatViewSet)
router.register('group_accounts', account_views.GroupAccountViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'hack2015.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login-with-password/', account_login.login_for_ken),
    url(r'^register-new-account/', group_manager.register_new_account)
]
