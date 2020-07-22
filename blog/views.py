from django.shortcuts import render

posts = [
    {
        'title': 'Today\'s declining Era',
        'author': 'Gaurav Pandey',
        'date_posted': 'July 22 , 2020',
        'content': 'Lets talk about Us.'
    },
    {
        'title': 'Jogging',
        'author': 'Shraddha Pandey',
        'date_posted': 'July 23 , 2020',
        'content': 'live life to the fullest.'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
