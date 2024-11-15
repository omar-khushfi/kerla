from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = product_in_order
    extra = 1
    fields = ('product', 'quantity', 'subtotal')
    readonly_fields = ('subtotal',)

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)  

       
        order = form.instance  
        total = 0 

      
        for item in order.product_in_order_set.all():  
            total += item.subtotal()  
           

        order.total = total  
        order.save()  
       

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('name', 'total', 'email', 'phone_number', 'date')
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.update_order_total(obj)

    def update_order_total(self, order):
        total = sum(item.subtotal() for item in order.product_in_order_set.all())
        order.total = total
        order.save()

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(product_in_order)
admin.site.register(Message)