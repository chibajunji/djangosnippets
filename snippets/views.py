from snippets.models import Snippet

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def top(request):
    snippets = Snippet.objects.all()  # Snippetの一覧を取得
    context = {'snippets': snippets}

    return render(request, 'snippets/top.html', context)

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html',
            {'snippet': snippet})
