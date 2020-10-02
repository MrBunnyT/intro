from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from .models import Tweet
from .forms import PostTweet
from django.utils.http import is_safe_url

def HomeView(request,*args,**kwargs):
    return render(request,'Home.html',context={},status=200)

def Tweet_Create_View(request,*args,**kwargs):
    form = PostTweet(request.POST or None)
    forward_url = request.POST.get('forward_url')
    print('forward_url------>',forward_url)
    if form.is_valid:
        obj = form.save(commit=False)
        obj.save()
        if forward_url!=None and is_safe_url(forward_url,settings.ALLOWED_HOSTS):
            return redirect(forward_url)
        else:
            return HttpResponse('<h1>You Were Being Redirected to An unsafe URL</h1>')
    form = PostTweet
    context={'form':form}
    return render(request,'Form.html',context)

def ListView(request,*args,**kwargs):
    tweets = Tweet.objects.all()
    data = [{'id':x.id,'content':x.content,'likes':x.likes} for x in tweets]
    response = {
        'response':data,
    }
    return JsonResponse(response)

def Tweet_Detail_View(request,tweet_id,*args,**kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    return jsondata 
    """
    tweets = Tweet.objects.all()
    data = {
        'id' : tweet_id,
    }
    status = 200
    try:
        data['content'] = tweets.get(id=tweet_id).content
    except:
        data['message'] = "Not Found"
        status=404
    return JsonResponse(data,status=status)
