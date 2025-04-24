# 🎥 robot_camera_turn

A ROS 2 Humble package (Python, `rclpy`) to control a robot-mounted camera that can turn to a specific angle.

## 📦 Overview

This package includes:
- A Python node (`camera_turn_node`) that turns the robot's camera based on input parameters.
- Optional parameter configuration via CLI or YAML.
- Suitable for simulations and real robots.

## 🛠️ Installation

1. Clone this package into your ROS 2 workspace:
```bash
cd ~/ros2_ws/src
mkdir robot_cam_pkg
cd robot_cam_pkg
git clone https://github.com/Vishalkm206/Robot_Camera_Turn_Service_using_ROS2_Humble
cd ~/ros2_ws
colcon build

# Terminal 1
source install/setup.bash
ros2 run robot_cam_pkg server.py

# Terminal 2
cd ~/ros2_ws
source install/setup.bash
ros2 run robot_cam_pkg client.py

```

### Angle range --> -30 to +30