from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from . import figure_handler as tool

img_path = './Wallpaper/assets/images/'

# Scheduled web crawler
try:
    scheduler = BackgroundScheduler(timezone= 'America/Los_Angeles')
    @scheduler.scheduled_job('cron', hour='17', minute='46')
    def get_background_figure():
        newFigure = tool.get_figure_name()
        tool.releaseSpace()
        tool.download(newFigure)
        print(newFigure)
    @scheduler.scheduled_job('interval', seconds=1)
    def my_job():
        pass
        # newFigure = tool.get_figure_name()
        # print(newFigure)
        # tool.releaseSpace()
        # tool.download(newFigure)
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()



def index(req):
    return HttpResponse("Hello World")

def check_new_image(req):
    imgs = os.listdir(img_path)
    img = open(img_path + imgs[-1], mode = 'rb').read()
    print("Initiating transferring...")
    return HttpResponse(img, content_type="image/jpg")
