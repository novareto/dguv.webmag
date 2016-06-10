# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

from five import grok
from uvc.api import api
from zope import interface
from .layout import BSPage as Page
from .layer import IAnonymousLayer
from .interfaces import IPageTop, IFooter
from zope.component import getMultiAdapter
from plone.dexterity.interfaces import IDexterityItem
from plone.app.contenttypes.interfaces import IDocument
from plone.app.layout.globals.interfaces import IViewView



api.templatedir('templates')


class SimpleNewspaperView(api.View):
    api.name('newspaperview')
    api.context(interface.Interface)


class NewspaperView(Page):
    grok.implements(IViewView)
    api.context(interface.Interface)
    grok.layer(IAnonymousLayer)
    

class ContentPage(Page):
    grok.context(IDocument)
    grok.name('document_view')
    grok.layer(IAnonymousLayer)

    def render(self):
        return "PLEASE PLEASE FILL ME"


class PageHeader(api.Viewlet):
    grok.layer(IAnonymousLayer)
    api.context(interface.Interface)
    api.viewletmanager(IPageTop)


class PageFooter(api.Viewlet):
    grok.layer(IAnonymousLayer)
    api.context(interface.Interface)
    api.viewletmanager(IFooter)
