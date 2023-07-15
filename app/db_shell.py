from app.models import Book

Book.objects.create(name="Book_1", price = 200, qty = 4, is_published = True, is_active= True)
Book.objects.create(name="Book_2", price = 150, qty = 20, is_published = True, is_active= True)
Book.objects.create(name="Book_3", price = 40, qty = 30, is_published = True, is_active= True)
# Book.objects.create(name="Book_4", price = 50, qty = 14, is_published = True, is_active= True)


