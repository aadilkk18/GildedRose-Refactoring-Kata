# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
CONJURED_PREFIX = "Conjured"

MIN_QUALITY = 0
MAX_QUALITY = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                continue  # legendary item, never sold, never changes

            if item.name == AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == BACKSTAGE_PASSES:
                self._update_backstage_passes(item)
            elif item.name.startswith(CONJURED_PREFIX):
                self._update_conjured(item)
            else:
                self._update_normal(item)

            item.sell_in -= 1

            # Aged Brie and Backstage passes get an extra adjustment
            # once the sell by date has passed.
            if item.sell_in < 0:
                if item.name == AGED_BRIE:
                    self._increase_quality(item)
                elif item.name == BACKSTAGE_PASSES:
                    item.quality = 0
                elif item.name.startswith(CONJURED_PREFIX):
                    self._decrease_quality(item, amount=2)
                else:
                    self._decrease_quality(item)

    def _update_normal(self, item):
        self._decrease_quality(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_conjured(self, item):
        self._decrease_quality(item, amount=2)

    def _update_backstage_passes(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)

    @staticmethod
    def _increase_quality(item, amount=1):
        item.quality = min(MAX_QUALITY, item.quality + amount)

    @staticmethod
    def _decrease_quality(item, amount=1):
        item.quality = max(MIN_QUALITY, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)