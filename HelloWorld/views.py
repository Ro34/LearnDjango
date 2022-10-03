from django.shortcuts import render


def run(request):
    view_list = ['a', 'b', 'c']
    context = {'hello': ['a', 'b', 'c']}
    return render(request, 'runoob.html', context)
