from django.shortcuts import render
from django.http import HttpResponse
import smtplib
# import emoji
from db.models import contact
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os 
@csrf_exempt
def main(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = contact(name = name,email = email,subject=subject,message=message)
        ins.save()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        emoji = "U+1F970"
        server.login("jagadishmuru@gmail.com","ppcquoqztymkmgfj")
        body = f"Dear {name} \n\nI hope details in my portfolio is sufficient for you.\nIf you required futher information. You can contact by email id or phone no. \n\nThankyou For your visit"
        gr = 'Thankyou for visit'
        msg = f"Subject: {gr}\n\n{body}"
        details = f"Subject: Guest Visited\n\n{name}\n\n{email}\n\n{subject}\n\n{message}"
        server.sendmail('jagadishmuru@gmail.com', email, msg)
        server.sendmail('jagadishmuru@gmail.com','jagadishmuru@gmail.com', details)
        server.quit()
    return render(request, 'main.html')

def downloadfile(req):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "JagadishResume.pdf"
    filepath = base_dir + '/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
    content_type=mimetypes.guess_type(thefile)[0])
    response['content-length'] = os.path.getsize(thefile)
    response['content-Disposition'] = "Attachment;filename=%s" % filename
    return response