from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method=='POST':
        company_symbol=request.POST['companysymbol']
        if company_symbol == "":
            return redirect('/')
        else:
            return redirect (companydetails,company_symbol=company_symbol)
    else:
        return render(request, "templates/home.html", {})

def topgainers(request):
    import requests
    response=requests.get('https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=f4f967ebbf112f52a4d20b565369f075').json()
    return render(request, "templates/topgainers.html", {'response':response})

def toplosers(request):
    import requests
    response=requests.get('https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=f4f967ebbf112f52a4d20b565369f075').json()
    return render(request, "templates/toplosers.html", {'response':response})

def companydetails(request,company_symbol):
    import requests
    url='https://financialmodelingprep.com/api/v3/search?query={company_symbol}&apikey=f4f967ebbf112f52a4d20b565369f075'
    response=requests.get(url.format(company_symbol=company_symbol)).json()
    return render(request, "templates/companydetails.html", {'response':response})

def backhome(request):
    return redirect('/')