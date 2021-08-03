import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge

from sensor_msgs.msg import Image

import time

class Streamer(Node):
    def __init__(self) -> None:
        super().__init__('streamer')
        self.msg = Image()
        self.publisher = self.create_publisher(Image, 'image_raw', 10)
        # Capturing timer
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.frame_id = 0
        self.vc = cv2.VideoCapture(0)
        self.vc.set(3,640)
        self.vc.set(4,480)
        if not self.vc.isOpened(): assert('No camera')

    def timer_callback(self):
        res, img = self.capture()
        if res:
            self.publish(img)
            self.frame_id += 1
        else:
            print('No frame')

        
    def capture(self):
        res, frame = self.vc.read()
        return res, frame
    
    def publish(self, img):
        
        msg = CvBridge().cv2_to_imgmsg(img, 'bgr8')
        msg.encoding = 'bgr8'
        msg.width = 640
        msg.height = 480
        #msg = CvBridge().cv2_to_imgmsg(img, 'rgb8')
        #msg.encoding = 'rgb8'
        msg.header.frame_id = str(self.frame_id)
        

        '''
        msg = Image()
        msg.data = img
        
        msg.encoding = 'rgb8'
        msg.width = 640
        msg.height = 480
        msg.header.frame_id = self.frame_id
        msg.header.stamp = time.time()
        '''    
        self.publisher.publish(msg)
        
    def destroy_node(self) -> bool:
        self.vc.release()
        return super().destroy_node()
        

def main(args=None):
    rclpy.init(args=args)

    streamer = Streamer()

    rclpy.spin(streamer)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    streamer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
