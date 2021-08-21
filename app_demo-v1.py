# import modules
import os
import cv2
import numpy as np
from flask import Flask, render_template, request,jsonify
# from python files
from rt_add_del_func import *

# flask app name
app = Flask(__name__)

#html home
@app.route('/')
def home():
	return render_template('home.html')

# post method
@app.route('/startPipeline',methods=['POST', 'GET'])

# helper function
def startPipeline():
        '''
        For rendering results on GUI
        '''
        if request.method == 'POST':

            # get video file
            # Example filename: file:///opt/nvidia/deepstream/deepstream-5.1/samples/streams/classroom.mp4
            global streams_in
            video_file = request.form['text']
            # input streams are separated by ','. Split it and add them to a list
            split_str = video_file.split(',')
            streams_in = []
            # create streams list
            for i in range(len(split_str)):
                    streams_in.append(split_str[i])

            # for complete pipeline        
            if request.form.get('method1') == 'startPipeline':
                    # normal detection pipelines
                    ## for RTSP output
                    #detection_p = main_rtsp_uri_output(streams_in)
                    ## for Video output
                    detection_p = main_add_del_stream(streams_in)
                    
        # render template
        return render_template('result.html', prediction="Success")

# post method
@app.route('/addStream',methods=['POST', 'GET'])
# helper function
def addStream():
        '''
        For rendering results on GUI
        '''
        if request.method == 'POST':
            # get video file
            # Example filename: file:///opt/nvidia/deepstream/deepstream-5.1/samples/streams/classroom.mp4
            video_file = request.form['text']
            # input streams are separated by ','. Split it and add them to a list
            split_str = video_file.split(',')
            streams_in = []
            # create streams list
            for i in range(len(split_str)):
                    streams_in.append(split_str[i])
                    
            # for adding stream        
            if  request.form.get('method2') == 'addStream':
                    # method_add_del -> add_sources, delete_sources
                    detection_p = add_new_src(streams_in)
                    
        # render template
        #return render_template('result.html', prediction="Success")

# post method
@app.route('/delStream',methods=['POST', 'GET'])
# helper function
def delStream():
        '''
        For rendering results on GUI
        '''
        if request.method == 'POST':
            # get video file
            # Example filename: file:///opt/nvidia/deepstream/deepstream-5.1/samples/streams/classroom.mp4
            video_file = request.form['text']
            # input streams are separated by ','. Split it and add them to a list
            # create streams list
            for i in range(len(streams_in)):
                    if video_file == streams_in[i]:
                            del_src_index = i
                            
            # for deleting stream        
            if  request.form.get('method3') == 'delStream':
                    # method_add_del -> add_sources, delete_sources
                    detection_p = del_streaming_src(del_src_index)
                                        
        # render template
        return render_template('result.html', prediction="Success")
                                
if __name__ == '__main__':
	app.run(debug=True)
