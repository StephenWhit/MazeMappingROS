# MazeMappingROS

The goal for this project was to create an autonomous mobile robot that can map a certain distance in space using its laser scanner. To accomplish this we used a variety of algorithms such as: Hector Slam, A*, RRT, and self made motion planning. Using a combination of these algorithms we would be able to map a certain area while avoiding obstacles.

Our implementation for autonomous mapping started with collecting the scan data from the Hokuyo laser range finder. The data the hokuyo sensor will give us data that can be used for both our Hector slam and our self made motion planning. After the data is passed through the hector slam algorithm, we should have a map of the surrounding area. 

Now that the robot knows its surrounding area we can use either A* or RRT to determine a path for the robot to take. Because RRT is a branching algorithm we will run the algorithm and then decide our goal. If A* is desired to be implemented we will need to first decide on a goal for the robot to reach. A* will then path the best route to the desired goal. Our goal for both RRT and A* initially is the farthest distanced sensed but the closest mapped. In other words we will chose the farthest scan distance as our threshold and then determine which threshold point in the map we want to reach depending on how far it is from the robot. This will prevent the robot from backtracking over and over again creating a yo yo effect. 

Once the robot successfully moves to that location it attempts another scan of the environment. Again the robot depending on the algorithm implemented, will attempt to move to a new goal and repeat this entire process. Once the robot does not have any more max thresholds to set as goals for RRT or A* then the entire map should be complete. 

Contributions: 
Kyle:
Stephen:
Hiren:
Shan Qamruddin: 
