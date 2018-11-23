from django.shortcuts import render
from django.views import View
from .models import Coin
# Create your views here.

class QueryPageView(View):
    def get(self, request):
        return render(request, 'coins/home.html',{})

    def post(self, request):
        if request.POST['query_data']:
            query_data = request.POST['query_data']
            # get the model objects
            denominations = Coin.objects.values('denomination')
            l = [den['denomination']for den in denominations]
            from .algo.currency import Currency
            ans = Currency(l,int(query_data)).answer()

            for key,value in ans.items():
                url = Coin.objects.filter(denomination=key)[0].image_url
                value['url'] = url

            context = {
                'query_data': query_data,
                'denominations': denominations,
                'answer': ans,
            }
            return render(request, 'coins/detail.html',context)
        else:
            return render(request, 'coins/detail.html', {'error': 'No input given!!'})



