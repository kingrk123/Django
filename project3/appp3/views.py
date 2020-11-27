from django.shortcuts import render


def showIndex(req):
    Employee_Details = {
        "101": {"name": "Kiran", "salary":185000},
        "102": {"name": "Ravi", "salary":175000},
        "103": {"name": "Kingrk", "salary":165000},
        "104": {"name": "Puru", "salary": 155000},
        "105": {"name": "Panku", "salary":145000}
    }
    return render(req, "index.html", {"data": Employee_Details})
