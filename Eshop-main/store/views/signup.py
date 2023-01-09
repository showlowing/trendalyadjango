from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Lütfen Adınızı Giriniz!"
        elif len (customer.first_name) < 3:
            error_message = 'Adınız En Az 3 Karakter Uzunluğunda Olmalıdır!'
        elif not customer.last_name:
            error_message = 'Lütfen Soyadınızı Giriniz!'
        elif len (customer.last_name) < 3:
            error_message = 'Soyadınız En Az 3 Karakter Uzunluğunda Olmalıdır!'
        elif not customer.phone:
            error_message = 'Telefon Numarası Giriniz!'
        elif len (customer.phone) < 10:
            error_message = 'Telefon Numarası En Az 11 Karakter Uzunluğunda Olmalı!'
        elif len (customer.password) < 5:
            error_message = 'Şifreniz En Az 5 Karakter Uzunluğunda Olmalı!'
        elif len (customer.email) < 5:
            error_message = 'E-Posta En Az 5 Karakter Uzunluğunda Olmalıdır!'
        elif customer.isExists ():
            error_message = 'E-Posta Adresi Zaten Kayıtlı!'
        # saving

        return error_message
