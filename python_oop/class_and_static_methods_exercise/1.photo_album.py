from math import ceil
from typing import List
class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    DASH = "-"
    COUNT_DASHES = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]


    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"
            return "No more free slots"

    def display(self):
        result = [self.DASH * self.COUNT_DASHES,]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASH * self.COUNT_DASHES)

        return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

# import unittest
#
#
# class TestsPhotoAlbum(unittest.TestCase):
#     def test_init_creates_all_attributes(self):
#         album = PhotoAlbum(2)
#         self.assertEqual(album.pages, 2)
#         self.assertEqual(album.photos, [[], []])
#
#     def test_from_photos_should_create_instace(self):
#         album = PhotoAlbum.from_photos_count(12)
#         self.assertEqual(album.pages, 3)
#         self.assertEqual(album.photos, [[], [], []])
#
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
#
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
#
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
#
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
#
#
# if __name__ == "__main__":
#     unittest.main()