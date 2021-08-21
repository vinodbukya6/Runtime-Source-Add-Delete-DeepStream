# Runtime-Source-Add-Delete-DeepStream

# Computer Vision Project

NVIDIA's DeepStream SDK delivers a complete streaming analytics toolkit for AI-based multi-sensor processing, video, audio and image understanding.

This Web Application tested on Jetson Nano.

People, Vehicle detection Web application for video streaming using Flask and Deepstream. In this Web Application user can select any video to run the DeepStream pipeline(Detection Models) and user can add or delete any particular video source.

# Inference Pipeline

Run inference pipeline with DeepStream components. We have two models to run each streaming source, People detection and Face detection. We have two other functionalities which can be used on this inference pipeline are add any new source and delete any streaming source.

# Delete Streaming Source Functionality

Delete a particular streaming source during runtime. For deleting a streaming source we need the source_id of that particular source. To find source_id, save all sources in a list and find the index of that source(del_src) and pass that index to the del_sources(). src_index → index of that particular source.

# Add New Source Functionality

Add a new source on runtime sources. We have few parameters(variables) to update. Remove end of streams(EOS) after adding or deleting source if streaming is completed. 
1. g_num_sources → number of sources
2. g_source_bin_list → add create_uridecode_bin for new source
3. g_source_id_list → update source id
4. g_eos_list → end of streams list
5. g_source_enabled → which all sources are running
6. MAX_NUM_SOURCES → we need to increase  number of sources by 1 
7. uri → which particular video to add

# References
1. https://github.com/NVIDIA-AI-IOT/deepstream_python_apps
2. https://spyjetson.blogspot.com/2020/08/xavier-nx-deepstream-50-2-run-python.html
3. https://forums.developer.nvidia.com/t/how-to-create-an-rtsp-sink-with-deepstream-python-program/111175/7
