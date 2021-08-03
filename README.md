# picam
This is a python ROS2 node to capture the camera, and publish /image_raw topic of message type sensor_msgs.msg.Image.
It can be used with Rasperry Pi camera.

# Pre-requisites:
- OpenCV (cv2)
- cv_bridge (sudo apt-get install ros-$(rosversion -d)-cv-bridge)
- Enable camera in Pi:
https://ubuntu.com/blog/how-to-stream-video-with-raspberry-pi-hq-camera-on-ubuntu-core
→ But for Pi3 → edit /boot/firmware/config.txt not usrcfg.txt --> add start_x=1


# How to run


## On Pi/Local
As a ROS2 node
`ros2 run picam streamer`

Or as python file:
`python3 picam/picam/streamer.py`
## On remote/PC
`ros2 run rqt_image_view rqt_image_view`

# Known issues

1- Slow on Picam. 
gstreamer + VLC seems the fastest option:
Install gstreamer: https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c
Stream to VLC:
http://www.gaitech.hk/edu/video/video-streaming-vlc.html


2- streamer_compressed.py is used to publish /image_raw_compressed topic from sensor_msgs.msg.CompressedImage. This cannot be decoded successfully in rqt_image_view

3- rviz2--> Add --> By Topic --> /image_raw or Camera, doesn't work.
