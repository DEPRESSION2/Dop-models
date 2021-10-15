from django.shortcuts import render

# Create your views here.

import re
import random

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # return HttpResponse('Success!')
    return render(request, 'start_page.html')

def articles(request):
    # return HttpResponse('Article Success!')
    return render(request, 'articles.html')

def archive(request):
    # return HttpResponse('Archive Success!')
    return render(request, 'archive.html')

def users(request):
    # return HttpResponse('Users Success!')
    return render(request, 'users.html')

def article_uniq(request, article_id, name=''):
    # return HttpResponse('Article {} Success! {}'.format(article_id, name if name else ''))
    data = {'article_id': article_id, 'name': name}
    return render(request, 'article-number.html', {
        'check': article_id % 2,
        'slug': name
        })

def archive_uniq(request, article_id):
	return HttpResponse('{} archive Success!'.format(article_id))

def users_num(request, user_number):
	return HttpResponse('User {} Success!'.format(user_number))

def phone_number(request, phone_number):
    code_list= ['039', '067', '068', '096', '097', '098', '050', '066', '095', '099', '063', '093', '091', '092', '094']
    if len(str(phone_number)) == 10:
        for i in code_list:
            result = re.match(i, str(phone_number))
            if result:
                return HttpResponse("ukrainian phone number")
    return HttpResponse("not ukrainian phone number")

def code(request):
	return HttpResponse('Code complete')