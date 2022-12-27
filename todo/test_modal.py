from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModal(TestCase):

    def test_modal_default_done_false(self):
        item = Item.objects.create(name="modal test case")
        self.assertFalse(item.done)

    def test_modal_str_method_return_name(self):
        item = Item.objects.create(name="return name string")
        self.assertEqual(str(item), "return name string")
