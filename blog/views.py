from django.shortcuts import render

# Views definition


def post_list(request):
    print(request)
    return render(request, 'blog/post_list.html', {})
