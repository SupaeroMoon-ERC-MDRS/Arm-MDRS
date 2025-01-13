import numpy as np 

# Move these to a config later
L1 = 1
L2 = 1


class joint_angles:
    def __init__(self, t1, t2, t3, t4):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4


def cart_to_joints(position):
    '''
    poition [struct] - vector containing x, y, gamma, theta
    
    returns:
        joint_angles 
    '''
    Px = position.x
    Py = position.y
    gamma = position.gamma
    theta = position.theta

    # Base angle
    t1 = theta

    # Solve for the second joint angle
    t3 = np.arccos((L1**2 + L2**2 - Px**2 - Py**2)/(2*L1*L2))

    # Solve for first joint angle
    M = L1 + L2*np.cos(t3)
    N = L2*np.sin(t3)

    c_t2 = (Px*M + Py*N)/(M**2 + N**2)
    s_t2 = (Py - N*c_t2)/M
    t2 = np.arctan2(s_t2, c_t2)
    
    # Solve last joint angle
    t4 = gamma - t2 - t3
    return joint_angles(t1, t2, t3, t4)

