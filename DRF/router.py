from snippets.api.viewset import SnippetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('snippets', SnippetViewSet,basename='snippet')
