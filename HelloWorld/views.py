from django.shortcuts import render


def run(request):
    view_list = ['a', 'b', 'c']
    context = {'hello': view_list}
    return render(request, 'runoob.html', context)
