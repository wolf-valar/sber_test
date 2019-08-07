from django.http import HttpResponse
from django.views.generic.base import View

#def hello(request):
 #   return HttpResponse("Hello world")

class HomePageView(View):

    def hello(request):

#        response_text = textwrap.dedent('''\
      #      <html>
     #       <head>
    #            <title>Hw title</title>
   #         </head>
  #          <body>
           #    // <h1>Greetings to the world</h1>
          #      <p>Hello, world!</p>
         #   </body>
        #    </html>
       # ''')
        return HttpResponse('Hello World')
    def get(self, request):
        return HttpResponse('<html><title>Hello World Page</title><body><h1>Hello World!</h1></body>')
