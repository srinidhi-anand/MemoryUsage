from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail  import EmailMessage
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import numpy as np
import psutil
import base64
import os
from io import BytesIO


def mkdir_p(mypath):
    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise

def home(request):
	x = np.arange(10)
	fig = plt.figure(figsize =(7, 7)) 
	ax1 = plt.subplot(1,1,1)
	w = 0.3
	data = {}	
	ram_data = {}
	for i in range(len(x)):
		data.update({i:psutil.cpu_percent(interval=0.5)})
		ram_data.update({i:int(psutil.virtual_memory().total - psutil.virtual_memory().available)})
		
	Cpu_Utilization = list(data.values()) 
	RAM_Utilization = list(ram_data.values()) 
	plt.xticks(x + w /2, Cpu_Utilization, rotation='vertical')
	cpu =ax1.bar(x, Cpu_Utilization, width=w, color='b', align='center')
	plt.ylabel('CPU')
	ax2 = ax1.twinx()
	ram =ax2.bar(x + w, RAM_Utilization, width=w,color='g',align='center')
	if max(Cpu_Utilization) > 50:
	
		email = EmailMessage(
			'Memory Utilization Warning', 'The Memory Utilization is '+str(max(Cpu_Utilization))+'%', to=['srinidhianand4@gmail.com','anandkeerthi010@gmail.com']
		)
		email.send()
	plt.ylabel('RAM')
	plt.xlabel('Time')
	plt.legend([cpu, ram],['CPU usage', 'RAM usage'])
	response = HttpResponse(content_type = 'image/png')
	canvas = FigureCanvasAgg(fig)
	canvas.print_png(response)
	try:
		os.remove("E://MemoryUsage/front_end/src/graph.png")
	except:
		pass
	output_dir = "E://MemoryUsage/front_end/src"
	mkdir_p(output_dir)

	fig.savefig('{}/graph.png'.format(output_dir))
	
	return response
	
def lineplot(request):
	x = np.arange(10)
	fig = plt.figure(figsize =(7, 7)) 
	ax1 = plt.subplot(1,1,1)
	w = 0.3
	data = {}	
	ram_data = {}
	for i in range(len(x)):
		data.update({i:psutil.cpu_percent(interval=0.5)})
		ram_data.update({i:int(psutil.virtual_memory().total - psutil.virtual_memory().available)})
		
	Cpu_Utilization = list(data.values()) 
	RAM_Utilization = list(ram_data.values()) 
	plt.xticks(x + w /2, Cpu_Utilization, rotation='vertical')
	cpu =ax1.plot(x, Cpu_Utilization,  color='b')
	plt.ylabel('CPU')
	ax2 = ax1.twinx()
	ram =ax2.plot(x + w, RAM_Utilization,color='g')
	plt.ylabel('RAM')
	plt.xlabel('Time')
	plt.legend([cpu, ram],['CPU usage', 'RAM usage'])
	#plt.show()

	response = HttpResponse(content_type = 'image/png')
	canvas = FigureCanvasAgg(fig)
	canvas.print_png(response)
	try:
		os.remove("E://MemoryUsage/front_end/src/plot.png")
	except:
		pass
	output_dir = "E://MemoryUsage/front_end/src"
	mkdir_p(output_dir)

	fig.savefig('{}/plot.png'.format(output_dir))

	return response

