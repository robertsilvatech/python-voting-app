import os
import redis
import json
from flask import Flask
from flask import render_template
from flask import request

def create_app():
    app = Flask(__name__)
    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('app.settings.Development')


    # Redis configurations
    redis_server = os.getenv('REDIS_SERVER', '127.0.0.1')
    redis_port = os.getenv('REDIS_PORT', '6379')

    # Redis Connection
    try:
        r = redis.StrictRedis(host=redis_server, port=redis_port)
        redis_ping = r.ping()
        print('Conected in Redis')
    except redis.ConnectionError:
        exit('Failed to connect to Redis, terminating.')

    @app.route('/')
    def result():
        keys_voting = r.scan_iter('*')
        results = []
        if keys_voting:
            print('Keys found')
        for key in keys_voting:
            key = key.decode('UTF-8')
            temp_dict = {}
            temp_dict['name'] = key.split(':')[-1]
            temp_dict['votes'] = r.get(key).decode('UTF-8')
            results.append(temp_dict)
        return render_template('result.html', results=results)       
    
    return app

app = Flask(__name__)
