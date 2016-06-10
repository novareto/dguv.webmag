# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

from .interfaces import IPageTop, IFooter
from .layer import IAnonymousLayer, IWebmag

from five import grok
from grokcore.layout import Layout
from plone import api as ploneapi
from plone.app.layout.nextprevious.interfaces import INextPreviousProvider
from uvc.api import api
from uvc.shards.components import ShardsAsViews
from uvc.shards.interface import IShardedView
from zope import interface


api.templatedir('templates')


class Footer(api.ViewletManager):
    api.implements(IFooter)
    api.context(interface.Interface)
    grok.layer(IAnonymousLayer)


class PageTop(api.ViewletManager):
    api.implements(IPageTop)
    api.context(interface.Interface)
    grok.layer(IAnonymousLayer)

    def nextprevious(self):
        portal = ploneapi.portal.get()
        nextprev = INextPreviousProvider(portal['web-mag'])
        return {'next': nextprev.getNextItem(self.context),
                'previous': nextprev.getPreviousItem(self.context)}
    

class NewsPaperLayout(Layout):
    api.context(interface.Interface)
    grok.layer(IAnonymousLayer)


class BSPage(api.Page):
    api.implements(IShardedView)
    shards = ShardsAsViews()
    api.baseclass()

    layoutClass = NewsPaperLayout

    def _get_layout(self):
        return self.layoutClass(self.request, self.context)
