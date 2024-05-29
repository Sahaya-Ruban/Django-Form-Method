from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,"index.html")


def details(request):
    
    Name=request.GET["Name"]
    Age=request.GET["Age"]
    Mobile_no=request.GET["Mobile_no"]
    Email=request.GET["Email"]
    DOB=request.GET["DOB"]
    Address=request.GET["Address"]
    District=request.GET["District"]
    State=request.GET["State"]
    Country=request.GET["Country"]
    Pincode=request.GET["Pincode"]
    Qualification=request.GET["Qualification"]
    Matrital_status=request.GET["Matrital_status"]
    
    bio_dict={"Name":Name,
              "Age":Age,
              "Mobile_no":Mobile_no,
              "Email":Email,
              "DOB":DOB,
              "Address":Address,
              "District":District,
              "State":State,
              "Country":Country,
              "Pincode":Pincode,
              "Qualification":Qualification,
              "Matrital_status":Matrital_status
              }
    
    return render(request,"table.html",{"data":bio_dict})