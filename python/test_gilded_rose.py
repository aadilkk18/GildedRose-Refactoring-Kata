# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_degrades_quality_and_sell_in_by_one(self):
        """A normal item loses 1 quality and 1 sell_in per day."""
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_quality_never_negative(self):
        """Quality never drops below 0, even when already at 0."""
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_normal_item_degrades_twice_as_fast_after_sell_in_expired(self):
        """Once sell_in has passed (sell_in < 0), quality degrades by 2 instead of 1."""
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_aged_brie_increases_quality_with_age(self):
        """Aged Brie gains 1 quality per day instead of losing it."""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_aged_brie_quality_never_exceeds_fifty(self):
        """Aged Brie quality is capped at 50, even as it keeps aging."""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


    def test_sulfuras_never_changes(self):
        """Sulfuras never has to be sold and its quality never changes."""
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


    def test_backstage_passes_increase_by_one_when_far_from_concert(self):
        """Backstage passes gain 1 quality/day when sell_in > 10."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)


    def test_backstage_passes_increase_by_two_at_ten_days_or_less(self):
        """Backstage passes gain 2 quality/day when sell_in <= 10."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)


    def test_backstage_passes_increase_by_three_at_five_days_or_less(self):
        """Backstage passes gain 3 quality/day when sell_in <= 5."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)


    def test_backstage_passes_drop_to_zero_after_concert(self):
        """Backstage passes quality drops to 0 once sell_in has passed (concert over)."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


    def test_backstage_passes_quality_capped_at_fifty_even_with_bonus(self):
        """Backstage passes quality never exceeds 50, even with the +2/+3 bonus near the concert."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


    def test_conjured_item_degrades_twice_as_fast_as_normal(self):
        """Conjured items lose 2 quality per day (twice the normal rate) before sell_in expires."""
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)


    def test_conjured_item_degrades_four_times_as_fast_after_expired(self):
        """Conjured items lose 4 quality per day once sell_in has passed (twice the normal expired rate)."""
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)


    def test_conjured_item_quality_never_negative(self):
        """Conjured item quality never drops below 0, even with the doubled degrade rate."""
        items = [Item("Conjured Mana Cake", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()