#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from robot_cam_pkg.srv import TurningCamera
import cv2
from cv_bridge import CvBridge

class TurningCameraClient(Node):
    def __init__(self):
        super().__init__("Turn_camera_service_Client_node")
        self.client = self.create_client(TurningCamera,'turning_camera')
        self.req = TurningCamera.Request()
    
    def send_request(self,num):
        self.req.angle = float(num)
        self.client.wait_for_service()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self,self.future)

        self.result = self.future.result()
        return self.result.img

    def display_image(self,image_msg):
        image = CvBridge().imgmsg_to_cv2(image_msg)
        # print("showing img")
        cv2.imshow("Turn camera Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



def main(args=None):
    rclpy.init()
    client_node = TurningCameraClient()
    print("Client Node waiting for server response")
    try:
        user_input = input("Enter your angle(degree): ")
        res = client_node.send_request(user_input)
        client_node.display_image(res)
    except KeyboardInterrupt:
        print("Terminating Node....")
        client_node.destroy_node()

if __name__=='__main__':
    main()