from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from time import sleep
import serial

from .models import Log


class WriteComView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if 'number' in request.data and request.data['number']:
            self.write_serial(str(request.data['number']))
            self.write_log(request.data['number'])
            content = {'result': 'Ok!'}
        else:
            content = {'result': 'Send number from 1 to 9'}
        return Response(content)

    def write_serial(self, number):
        ser = serial.Serial('/dev/ttyACM0')
        sleep(2)
        ser.write(str.encode(number))
        sleep(2)
        ser.close()

    def write_log(self, number):
        log = Log(number=number, date=timezone.now())
        log.save()
