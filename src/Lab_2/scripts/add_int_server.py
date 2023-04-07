
from Lab_2.srv import add_int,Add_intResponse
import rospy

def handle_add_int(req):
    return Add_intResponse(req.a + req.b)

def add_int_server():
    rospy.init_node('add_int_server')
    s = rospy.Service('add_int', add_int, handle_add_int)
    print ("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_int_server()