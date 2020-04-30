from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views import View
from .models import Employee
import io, csv


class EmployeeUploadView(View):
    def get(self, request):
        template_name = 'employee/importemployee.html'
        return render(request, template_name)

    def post(self, request):
        user = request.user  # get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            Employee(
                first_name=row['first_name'],
                last_name=row['last_name'],
                gender=('F' if row['gender'] == 'Female' else ('M' if row['gender'] == 'Male' else 'F')),
                dob=(row['dob'] if row['dob'] != '' else '1970-01-01'),
                village=row['village'],
                district=row['district'],
                phone_number=row['phone_number'],
                father_name=row['father_name'],
                preferred_language=row['preferred_language'],
                created_by=user,  # This is foreignkey value
                updated_by=user,  # This is foreignkey value

            )
            for row in list_of_dict
        ]
        try:
            msg = Employee.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}

        return JsonResponse(returnmsg)