# from django.shortcuts import render
from django.http import HttpResponse

# from django.views.generic import TemplateView


# Create your views here.
def myview(request):
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 4:
        del request.session["num_visits"]

    oldval = request.COOKIES.get("zap", None)
    resp = HttpResponse(f"myview: zap was {oldval}, view count={num_visits}, 0b9092db")
    if oldval:
        resp.set_cookie("zap", int(oldval) + 1)  # No expired date = until browser close
    else:
        resp.set_cookie("zap", 42)  # No expired date = until browser close
    resp.set_cookie("sakaicar", 42, max_age=1000)  # seconds until expire
    resp.set_cookie("dj4e_cookie", "0b9092db", max_age=1000)
    return resp
