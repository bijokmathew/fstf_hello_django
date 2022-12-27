from django.test import TestCase
from .models import Item

# Create your tests here.


class TestView(TestCase):

    def test_get_todo_list(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'todo/todo_list.html')

    def test_add_todo_list(self):
        resp = self.client.get('/add')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'todo/todo_list_add.html')

    def test_edit_todo_list(self):
        item = Item.objects.create(name='this is sample test')
        resp = self.client.get(f'/edit/{item.id}')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "todo/todo_list_edit.html")
    
    def test_delete_todo_list(self):
        item = Item.objects.create(name="for testing delete")
        resp = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(resp, "/")
        dele = Item.objects.filter(id=item.id)
        self.assertEqual(len(dele), 0)

    def test_toggle_todo_list(self):
        item = Item.objects.create(name="eg for toggle")
        tog = item.done
        resp = self.client.get(f'/toggle/{item.id}')
        tog2 = Item.objects.get(id=item.id)
        self.assertRedirects(resp, "/")
        self.assertNotEqual(tog, tog2.done)
    
    def test_add_item_todo_list(self):
        resp = self.client.post("/add", {'name': "add item test"})
        self.assertRedirects(resp, "/")
        add = Item.objects.get(name="add item test")
        print(add.name)
        self.assertEquals(add.name, "add item test")
    
    def test_edit_post_todo_list(self):
        item = Item.objects.create(name="edit post eg")
        resp = self.client.post(f'/edit/{item.id}', {'name': "editeddd post eg"})
        self.assertRedirects(resp, "/")
        up_item = Item.objects.get(id=item.id)
        self.assertEqual(up_item.name, "editeddd post eg")