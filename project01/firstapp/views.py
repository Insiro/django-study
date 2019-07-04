from django.shortcuts import render
import random
# Create your views here.


def hello(request):
    return render(request, 'hello.html')
    # lotto 변수 = lotto_num 으로 화변에 전송, hello.html을 전송


def lotto(request):
    lotto_num = random.sample(range(1, 46), 6)
    return render(request, 'lotto.html', {'lotto': lotto_num})
