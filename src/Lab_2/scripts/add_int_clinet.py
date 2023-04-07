
import sys
from Lab_2.srv import add_int,Add_intResponse
import rospy
def add_int_client(x, y):
    rospy.wait_for_service('add_int')

    add_int = rospy.ServiceProxy('add_int', add_int)
    resp1 = add_int(x, y)
    return resp1.sum

if __name__ == "__main__":
    
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print ("Requesting %s+%s"%(x, y))
        print ("%s + %s = %s"%(x, y, add_int_client(x, y)))