from django.shortcuts import render

def show(a):
    Employee_details={
        "101": {"name": "Rishi", "salary": 185000},
        "102": {"name": "Rishi", "salary":  5000}
            }
    return render(a,"index.html",{"data":Employee_details})