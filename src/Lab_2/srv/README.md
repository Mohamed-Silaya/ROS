# server and clinet

to start we need to 

Create the srv directory -> Create your srv file ->Modify the package.xml -> Modify the CMakeLists -> write the server code -> Make sure files is executable -> build your package 

edit in CmakeList
uncomment this :
"Declare ROS messages, services and actions "
to work with server and clinet we need to edit some lines
add_service_files(
  FILES
  Service1.srv
  Service2.srv
)

add_service_files(
  FILES
  Add_int.srv
)

----------------
in package.xml 
we need to uncomment some lines
- <build_export_depend>message_generation</build_export_depend>

- <exec_depend>message_runtime</exec_depend>

----------------
we will make a server and clinet to add two numbers you will find it in scripts folder
add_int_server.py
add_int_clinet.py
to make it executable -> chmod u+x 
