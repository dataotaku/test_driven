from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == "POST":
        item = Item()
        item.text = request.POST["item_text"]
        item.save()
        return redirect("/")

    return render(request, "home.html", {
        "new_item_text": request.POST.get("item_text","")},
    )
