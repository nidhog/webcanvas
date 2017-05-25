from django.http import HttpResponse


def index(request):
    return HttpResponse("""Hello, is it me you're looking for...<br/>
    <a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>
        You are the 1 Millionth visitor! Click here to claim your prize!
    </a>""")
