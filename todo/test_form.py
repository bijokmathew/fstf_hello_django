from django.test import TestCase
from .form import Form_item

# Create your tests here.


class TestForm(TestCase):
   
    def test_item_name_required(self):
        form = Form_item({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], "This field is required.")

    def test_item_done_required(self):
        form = Form_item({'name': "Todo maths exersise"})
        self.assertTrue(form.is_valid())
    
    def test_fields_in_metaclass(self):
        form = Form_item()
        self.assertEqual(form.Meta.fields, ['name', 'done'])