import os
import pickle
import matplotlib
import matplotlib.pyplot as plt
from mapsloader import AlgorithmicMemory as am
matplotlib.use('WebAgg')

directory = 'dbits'

class WorldLattice:
    def __init__(self, filepath = None):
        self.am = am.AlgorithmicMemory()
        self.filepath = filepath

    def insert(self, data, x, y, z):

        return self.am.insert(data, x, y, z)

    def serialize(self):
        def write(file, dbit, sign, axis = 'data'):
            if sign == 'x' or sign == 'y' or sign == 'z':
                attr = getattr(dbit, sign)
            else:
                attr = getattr(getattr(dbit, sign), axis)
            if attr is not None:
                if axis == 'data':
                    pickle.dump(attr, file)
                else:
                    pickle.dump(attr.tr, file)
            else:
                pickle.dump(None, file)

        for dbit in self.am.dbit_list:
            with open("dbits/" + str(dbit.lbit0.tr) + str(dbit.lbit1.tr) + ".dbit", 'wb') as file:
                write(file, dbit, 'x')
                write(file, dbit, 'y')
                write(file, dbit, 'z')
                
                write(file, dbit, 'lbit0', 'tr')
                write(file, dbit, 'lbit0', 'data')
                write(file, dbit, 'lbit0', 'x')
                write(file, dbit, 'lbit0', 'y')
                write(file, dbit, 'lbit0', 'z')
                write(file, dbit, 'lbit0', 'other')
                
                write(file, dbit, 'lbit1', 'tr')
                write(file, dbit, 'lbit1', 'data')
                write(file, dbit, 'lbit1', 'x')
                write(file, dbit, 'lbit1', 'y')
                write(file, dbit, 'lbit1', 'z')
                write(file, dbit, 'lbit1', 'other')

    @staticmethod
    def deserialize():

        wl = WorldLattice()
        
        # Loop through all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    print(f"Reading {filename}:")
                    
                    x = pickle.load(file)
                    y = pickle.load(file)
                    z = pickle.load(file)
                    
                    lbit0tr = pickle.load(file)
                    lbit0data = pickle.load(file)
                    lbit0x = pickle.load(file)
                    lbit0y = pickle.load(file)
                    lbit0z = pickle.load(file)
                    lbit0other = pickle.load(file)

                    # lbit0 = am.LBit(lbit0tr, lbit0other, lbit0x, lbit0y, lbit0z)

                    lbit1tr = pickle.load(file)
                    lbit1data = pickle.load(file)
                    lbit1x = pickle.load(file)
                    lbit1y = pickle.load(file)
                    lbit1z = pickle.load(file)
                    lbit1other = pickle.load(file)
                    
                    # lbit1 = am.LBit(lbit1tr, lbit1other, lbit1x, lbit1y, lbit1z)

                    rv = wl.am.insert(lbit0data, x, y, z)

        return wl

    def visualize_lattice(self):
        """
        Visualize the 3D lattice using matplotlib, showing altitude as text.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Prepare lists to hold the coordinates
        x_coords = []
        y_coords = []
        z_coords = []
        labels = []

        # Extract coordinates for visualization
        for dbit in self.am.dbit_list:
            # if dbit.lbit0.other.other == dbit.lbit0:
            #     continue
            # dbit = dbit.lbit0.other.dbit

            print("dbit in viz ", dbit.lbit0.data)
            x_coords.append(dbit.lbit0.data['lat'])
            y_coords.append(dbit.lbit0.data['lon'])
            z_coords.append(dbit.lbit0.data['alt'])
            labels.append(f"{dbit.z:.2f}m")  # Display altitude as text

        # Plot each point and add labels to display altitude as text
        ax.scatter(x_coords, y_coords, z_coords, color='blue', s=50)

        for i, txt in enumerate(labels):
            ax.text(x_coords[i], y_coords[i], z_coords[i], txt, size=10, zorder=1, color='black')

        # Set axis labels
        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude')
        ax.set_zlabel('Altitude (m)')

        # Set the title
        ax.set_title('3D Lattice Visualization with Altitude')

        plt.show()


# wl = WorldLattice('wl.wl')

# wl.am.insert("one", 1, 1, 1)
# wl.am.insert("two", 2, 2, 2)
# wl.am.insert("three", 3, 3, 3)

# wl.serialize()

# w2 = WorldLattice.deserialize('wl.wl')

# am.inspectDBit(w2.am.cursor(), w2.am)
