
from uvc.api import api
from five import grok
from zope.interface import Interface
from .layout import BSPage as Page
from .layer import IAnonymousLayer
from uvc.shards.interface import IShardedView
from uvc.shards.components import ShardsAsViews

api.templatedir('templates')

class Titelview(Page):
    api.context(Interface)
    grok.layer(IAnonymousLayer)



#class DocumentView(api.Page):
#    api.implements(IShardedView)
#    api.context(Interface)
#    shards = ShardsAsViews()
#
#    def update(self):
#        self.mydoc = self.request.get('mydoc')
