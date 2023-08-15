import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/')
    network_stats = psutil.net_io_counters(pernic=True)
    network_interface = 'Wi-Fi'  
    network_usage = network_stats[network_interface]
    num_processes = len(psutil.pids())

    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"

    return render_template( "index.html",message=Message,
                           cpu_metric=cpu_metric, 
                           mem_metric=mem_metric, 
                           disk_usage=disk_usage,
                           network_usage=network_usage,
                           num_processes=num_processes 
                          )

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
