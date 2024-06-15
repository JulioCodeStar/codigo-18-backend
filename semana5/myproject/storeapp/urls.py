# Importar nuestra clase viewset
from .views import ProductViewSet, CategoryViewSet
# importar el router de DRF (Django Rest Framwork)
from rest_framework.routers import DefaultRouter

# crear una instancia de DefaultRouter
router = DefaultRouter()
# agregar una ruta usando router
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

# * significa Array [] Ej: *router
urlpatterns = router.urls