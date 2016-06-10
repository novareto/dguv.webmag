# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

from uvc.api import api
from plone import api as papi
from uvc.shards import BaseShard as Shard


api.templatedir('templates')


class BaseShard(Shard):
    api.baseclass()

    @property
    def css(self):
        return self._namespace.get('class', '')


class DocumentShard(BaseShard):
    api.name('document')

    def banner(self):
        doc = self._namespace.get('document')
        obj = self.context.get(doc)
        banner = {}
        if obj:
            banner['subject'] = ''
            if obj.subject:
                banner['subject'] = obj.subject[0] 
            banner['title'] = obj.title
            banner['description'] = obj.description
            banner['richtext'] = ''
            if obj.text:
                banner['richtext'] = obj.text.output
        return banner


class StoryShard(BaseShard):
    api.name('story')

    def banner(self):
        doc = self._namespace.get('mystory')
        obj = self.context.get(doc)
        banner = {}
        if obj:
            banner['title'] = obj.title
            banner['description'] = obj.description
            banner['banner_image'] = ('%s/@@images/newsimage' %
                                      obj.absolute_url())
            banner['url'] = obj.absolute_url()
        return banner


class EditorialShard(BaseShard):
    api.name('editorial')

    def banner(self):
        doc = self._namespace.get('myeditorial')
        obj = self.context.get(doc)
        banner = {}
        if obj:
            banner['subject'] = ''
            if obj.subject:
                banner['subject'] = obj.subject[0]
            banner['newstext'] = obj.newstext
            banner['url'] = obj.absolute_url()
            banner['banner_image'] = None
            if getattr(obj, 'newsimage', False):
                banner['banner_image'] = ('%s/@@images/newsimage' %
                                          obj.absolute_url())
                banner['newstitle'] = obj.newstitle
            banner['newsrichtext'] = None
            if obj.newsrichtext:
                banner['newsrichtext'] = obj.newsrichtext.output
        return banner


class RichTextShard(BaseShard):
    api.name('richtext')

    def banner(self):
        doc = self._namespace.get('document')
        obj = self.context.get(doc)
        banner = {}
        if obj:
            if obj.subject:
                banner['subject'] = obj.subject[0]
            if obj.newsrichtext:
                banner['newsrichtext'] = obj.newsrichtext.output
            banner['url'] = obj.absolute_url()
        return banner


class EventListShard(BaseShard):
    api.name('eventlist')

    def banner(self):
        folder = self._namespace.get('eventfolder')
        obj = self.context.get(folder)
        eventlist = []
        for i in obj.getFolderContents():
            if i.portal_type == 'Event':
                event = {}
                event['eventtext'] = i.Title.decode('utf-8')
                if i.start.date() == i.end.date():
                    event['date'] = i.start.strftime("%d.%m.%Y")
                else:
                    if i.start.year == i.end.year:
                        if i.start.month == i.end.month:
                            event['date'] = "%s. - %s" % (
                                i.start.day, i.end.strftime("%d.%m.%Y"))
                        else:
                            event['date'] = "%s - %s" % (
                                i.start.strftime("%d.%m"),
                                i.end.strftime("%d.%m.%Y"))
                    else:
                        event['date'] = "%s - %s" % (
                            i.start.strftime("%d.%m.%Y"),
                            i.end.strftime("%d.%m.%Y"))
                eventlist.append(event)
        return eventlist


class TitleShard(BaseShard):
    api.name('title')
    name = "TEST"

    def banner(self):
        return self._namespace.get('var', '') * 4


class NewsListingShard(BaseShard):
    api.name('newslisting')
    name = "News Listing"

    def get_news(self):
        print papi.content.find(portal_type='Document')
        return papi.content.find(portal_type='Document')


class ImageShard(BaseShard):
    api.name('image')

    def banner(self):
        """ return banner of this object """
        image = self._namespace.get('image', 'NN')
        obj = self.context.get(image)
        if obj:
            banner = {}
            if getattr(obj, 'newsimage', False):
                banner['banner_image'] = '%s/@@images/newsimage' \
                    % obj.absolute_url()
            if obj.newstitle:
                banner['banner_title'] = obj.newstitle
            if obj.newstext:
                banner['banner_description'] = obj.newstext
            if obj.newsrichtext:
                banner['banner_text'] = obj.newsrichtext.output
            banner['banner_link'] = obj.absolute_url()
            #banner['banner_linktext'] = obj.Title()
            if obj.newsurl:
                to_obj = obj.newsurl.to_object
                if to_obj:
                    banner['banner_link'] = to_obj.absolute_url()
                    banner['banner_linktext'] = to_obj.Title()
            if hasattr(obj, 'newslinktitle'):
                banner['banner_linktext'] = obj.newslinktitle
            if getattr(obj, 'banner_fontcolor', False):
                banner['banner_fontcolor'] = obj.banner_fontcolor
            print banner
            return banner
