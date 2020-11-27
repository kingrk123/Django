from django.shortcuts import render

def display(a):
    Student_details={
        "101": {"name": "KIRAN", "marks": [86, 82, 89, 85, 31]},
        "102": {"name": "PURU", "marks": [76, 72, 79, 25, 71]},
        "103": {"name": "PANKAJ", "marks": [66, 62, 29, 65, 61]},
        "104": {"name": "SWAT", "marks": [56, 52, 33, 55, 51]},
        "105": {"name": "ABHI", "marks": [46, 42, 49, 34, 41]},
    }
    return render(a, "kingrk.html", {"data": Student_details})









