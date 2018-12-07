# MazeMappingROS

Team D
Autonomous Mapping

Shan Qamruddin, Hiren Patel, Stephen Whitcomb, Kyle Jackson 
7th December, 2018
Project Report

The goal for this project was to create an autonomous mobile robot that can map a certain distance in space using its laser scanner. To accomplish this we could have used a variety of algorithms such as Hector Slam, A*, RRT, or a self-made path-planning. Using a combination of these algorithms we would be able to map a certain area while avoiding obstacles.
Our implementation for autonomous mapping started with collecting the scan data from the Hokuyo laser range finder. The data the hokuyo sensor will give us data that can be used for both our Hector slam and our chosen path-planning algorithm. After the data is passed through the Hector Slam algorithm, we should have a map of the immediate area.  Then the robot will move to another position and repeat this process until the goal area is totally mapped. 
Now that the robot knows its surrounding area we can use any path-planning algorithm to determine a path for the robot to take. We chose the Rapidly Exploring Random Tree (RRT) algorithm as it is designed to efficiently search nonconvex, high-dimensional spaces by randomly building a space-filling tree. Running RRT will provide the best path to our next goal position. Our goal position initially is the farthest distanced sensed but the closest mapped. In other words, we will choose the farthest scan distance as our threshold and then determine which threshold point in the map we want to reach depending on how far it is from the robot. This will prevent the robot from backtracking repeatedly.  
Conceptually, we understood what the project entailed.  However, we were unable to get this to work properly due to several issues.  One issue was the fact that we needed an obstacle list (python list) for path-planning and we did not know how to generate this. Another issue was that we had trouble figuring out how to incorporate the laser scan data into the RRT algorithm.  

Contributions: 
Shan Qamruddin: Focused on the overall path planning algorithm. Preventing yoyoing (aka. Back tracking) of the robot. I also spent a considerable amount of time on trying to get RRT and A* implemented by myself and with the group. 
Hiren Patel: researched path-planning, hokuyo laser scanner/turtlebot and how to use them in ROS
Stephen Whitcomb: path-planning and SLAM algorithms, wrote the code attempts
Kyle Jackson: researched path-planning and SLAM algorithms, wrote the code attempts, paper


Link: https://docs.google.com/document/d/1UDRxcJ9h99YQfEMaOIwnOqjR2RhLgJlVQ0RetpeOc3g/edit#


















