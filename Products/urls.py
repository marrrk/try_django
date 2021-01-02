from django.urls import path
from .views import (product_detail_view,
                            product_create_view,
                            render_initial_data,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view,
                            product_update_view
                            )

app_name = 'products'

urlpatterns = [
    # path('products/', product_list_view, name='list-products'),  #this was copied from trydjango/urls.py
    # in there all the urls are named /products/<whatever u want>
    # however now i brought it unto this one, and so can remove the products in the url bc that is taken care of in the
    # parent urls.py
    path('', product_list_view, name='list-products'),
    path('create/', product_create_view, name='create-product'),
    path('<int:my_id>/', dynamic_lookup_view, name='single-product'), # thing after the slash is another argument to the view function
    path('<int:my_id>/delete/', product_delete_view, name='delete-product'),
    path('<int:my_id>/update/', product_update_view, name='update-product'),
    path('initial/', render_initial_data, name='initial-data'),
]
