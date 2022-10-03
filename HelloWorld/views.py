from django.shortcuts import render


def run(request):
    view_dict = {'name': 'a', 'age': 'b'}
    context = {'hello': view_dict}
    return render(request, 'runoob.html', context)
