from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url_menu = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def child_menu(self):
        return self.menu_set.all()

    def get_tree(self):
        if self.parent_menu:
            return self.parent_menu.get_tree() + [self.parent_menu.id]
        else:
            return []
